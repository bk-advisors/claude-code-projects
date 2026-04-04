# ============================================================
#  Storytelling with Data: Analysis Techniques in R
#  BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
#
#  This script walks through the four core data operations
#  from the blog post (filter, group, summarize, compare)
#  using real WHO measles surveillance data for 46 African
#  countries (1980-2023).
#
#  Data: data/africa_measles.csv
#  Source: WHO Global Health Observatory (cases) +
#          World Bank (population)
# ============================================================

library(tidyverse)
library(scales)


## ── 0. Load & Enrich the Data ──────────────────────────────

# Real WHO measles data: 46 African countries, 1980-2023
# Cases per million = (reported cases / population) * 1,000,000

measles_raw <- read_csv("data/africa_measles.csv", show_col_types = FALSE)

glimpse(measles_raw)

# Add region, income group, and era classifications
measles <- measles_raw |>
  mutate(
    region = case_when(
      country %in% c("Algeria") ~ "North Africa",
      country %in% c("Benin", "Burkina Faso", "Cabo Verde", "Cote d'Ivoire",
                      "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia",
                      "Mali", "Mauritania", "Niger", "Nigeria", "Senegal",
                      "Sierra Leone", "Togo") ~ "West Africa",
      country %in% c("Cameroon", "Central African Republic", "Chad", "Congo",
                      "Democratic Republic of the Congo", "Equatorial Guinea",
                      "Gabon", "Sao Tome and Principe") ~ "Central Africa",
      country %in% c("Burundi", "Comoros", "Eritrea", "Ethiopia", "Kenya",
                      "Madagascar", "Malawi", "Mauritius", "Mozambique",
                      "Rwanda", "Seychelles", "Uganda",
                      "United Republic of Tanzania", "Zambia",
                      "Zimbabwe") ~ "East Africa",
      country %in% c("Angola", "Botswana", "Eswatini", "Lesotho",
                      "Namibia", "South Africa") ~ "Southern Africa"
    ),
    income_group = case_when(
      country %in% c("Algeria", "Botswana", "Equatorial Guinea", "Gabon",
                      "Mauritius", "Namibia", "South Africa") ~ "Upper-middle",
      country %in% c("Angola", "Cabo Verde", "Cameroon", "Comoros", "Congo",
                      "Cote d'Ivoire", "Eswatini", "Ghana", "Kenya",
                      "Lesotho", "Mauritania", "Nigeria",
                      "Sao Tome and Principe", "Senegal",
                      "United Republic of Tanzania", "Zambia",
                      "Zimbabwe") ~ "Lower-middle",
      TRUE ~ "Low"
    ),
    era = if_else(year < 2001, "Pre-Initiative (1980-2000)",
                  "Post-Initiative (2001-2023)")
  )

head(measles, 12)


## ── BKA Brand Colors ──────────────────────────────────────

bka_navy       <- "#242852"
bka_gray       <- "#606060"
bka_blue       <- "#005CB9"
bka_light_blue <- "#ACCBF9"
bka_green      <- "#83BD00"
bka_teal       <- "#3E9B6E"
bka_amber      <- "#F8A623"
bka_orange     <- "#FA7650"
bka_red        <- "#E24A3F"


## ── 1. FILTER — Which countries? Which years? ──────────────

# The first operation: narrow down to what matters.
# "How bad is measles in Africa?" is too broad.
# "What happened in East African countries after 2001?" is answerable.

# Filter to East Africa, post-initiative years
east_africa_post <- measles |>
  filter(region == "East Africa", year >= 2001)

east_africa_post |>
  select(country, year, cases_per_million) |>
  head(10)

# Filter for the peak-burden observations
high_burden <- measles |>
  filter(cases_per_million > 2000)

# Which countries dominate high-burden observations?
high_burden |>
  count(country, sort = TRUE)


## ── 2. GROUP — By meaningful categories ─────────────────────

# Grouping turns a flat table into structured comparisons.
# "By region" or "by time period" immediately adds dimension.

# Average cases per million by region AND era
by_region_era <- measles |>
  group_by(region, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million, na.rm = TRUE)),
    median_cases = round(median(cases_per_million, na.rm = TRUE)),
    n_observations = n(),
    .groups = "drop"
  )

by_region_era

# Every region declined, but the magnitude varies.
# That variation is where the diagnostic question lives.


## ── 3. SUMMARIZE — Simple statistics that reveal patterns ──

# Summary by country: before vs. after the 2001 initiative
country_summary <- measles |>
  group_by(country, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million, na.rm = TRUE)),
    .groups = "drop"
  ) |>
  pivot_wider(
    names_from = era,
    values_from = mean_cases
  ) |>
  rename(
    pre  = `Pre-Initiative (1980-2000)`,
    post = `Post-Initiative (2001-2023)`
  ) |>
  filter(!is.na(pre), !is.na(post)) |>
  mutate(
    pct_change = round((post - pre) / pre * 100, 1)
  ) |>
  arrange(pct_change)

country_summary

# The range is wide — some countries improved 90%+, others far less.
# That gap IS the story.


## ── 4. COMPARE — Before/after, across groups ────────────────

# Compare income groups
income_comparison <- measles |>
  group_by(income_group, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million, na.rm = TRUE)),
    .groups = "drop"
  ) |>
  pivot_wider(
    names_from = era,
    values_from = mean_cases
  ) |>
  rename(
    pre  = `Pre-Initiative (1980-2000)`,
    post = `Post-Initiative (2001-2023)`
  ) |>
  mutate(
    pct_change = round((post - pre) / pre * 100, 1)
  )

income_comparison

# Compare decline rates: fast vs. moderate vs. slow
country_summary |>
  mutate(decline_speed = case_when(
    pct_change < -80 ~ "Fast decline (>80%)",
    pct_change < -50 ~ "Moderate decline (50-80%)",
    TRUE ~ "Slow decline (<50%)"
  )) |>
  group_by(decline_speed) |>
  summarize(
    n_countries = n(),
    countries = paste(country, collapse = ", "),
    avg_pct_change = round(mean(pct_change), 1)
  )


## ── 5. VISUALIZE — Let the form follow the finding ─────────

# ---- Multi-stop gradient: cool (safe) → warm (danger) ----
measles_gradient <- c(
  colorRampPalette(c(bka_light_blue, bka_blue, bka_green, bka_amber))(15),
  colorRampPalette(c(bka_amber, bka_orange, bka_red))(5)
)

# 5a. The heatmap — real WHO data, all 46 countries

# Sort countries by pre-2001 average (highest burden at top)
country_order <- measles |>
  filter(year < 2001) |>
  group_by(country) |>
  summarise(avg_rate = mean(cases_per_million, na.rm = TRUE), .groups = "drop") |>
  arrange(avg_rate) |>
  pull(country)

measles_ordered <- measles |>
  mutate(country = factor(country, levels = country_order))

ggplot(measles_ordered, aes(x = year, y = country, fill = cases_per_million)) +
  geom_tile(colour = "white", linewidth = 0.4,
            width = 0.9, height = 0.9) +
  scale_fill_gradientn(
    colours = measles_gradient,
    limits = c(0, 5000),
    breaks = seq(0, 5000, by = 1000),
    labels = c("0", "1K", "2K", "3K", "4K", "5K"),
    na.value = "#F5F5F5",
    name = "Reported cases per million population",
    oob = scales::squish,
    guide = guide_colourbar(
      barwidth = 15, barheight = 0.6,
      title.position = "top",
      title.hjust = 0.5,
      ticks = TRUE, nbin = 50
    )
  ) +
  scale_x_continuous(expand = c(0, 0),
                     breaks = seq(1980, 2020, by = 5)) +
  geom_vline(xintercept = 2001, color = bka_navy,
             linewidth = 1.2, alpha = 0.8) +
  annotate("text", label = "WHO/UNICEF\nMeasles Initiative",
           x = 2001, y = length(country_order) + 0.5,
           hjust = -0.05, vjust = 1,
           size = 3.5, fontface = "bold",
           color = bka_navy) +
  coord_cartesian(clip = "off") +
  labs(
    title = "Mass immunization campaigns cut African measles\ncases by over 90% — but outbreaks persist",
    subtitle = "Reported measles cases per million population by country, 1980-2023",
    x = NULL, y = NULL,
    caption = paste0(
      "Source: WHO Global Health Observatory (cases) & World Bank (population) | ",
      "Countries with 15+ years of reporting shown\n",
      "Visualization: BK Advisors"
    )
  ) +
  theme_minimal(base_size = 11) +
  theme(
    panel.grid = element_blank(),
    axis.line = element_blank(),
    axis.text.y = element_text(size = 8, face = "bold", hjust = 1),
    axis.text.x = element_text(size = 8),
    legend.position = "bottom",
    legend.direction = "horizontal",
    legend.title = element_text(size = 9, face = "bold", color = bka_navy),
    legend.text = element_text(size = 8, color = bka_gray),
    plot.title = element_text(face = "bold", color = bka_navy, lineheight = 1.15),
    plot.subtitle = element_text(color = bka_gray, margin = margin(t = 2, b = 14)),
    plot.caption = element_text(color = bka_gray, size = 7, hjust = 1),
    plot.title.position = "plot",
    plot.caption.position = "plot",
    plot.margin = margin(15, 15, 10, 5)
  )


# 5b. Before-vs-after bar chart — top 15 highest-burden countries
top_15 <- country_summary |>
  arrange(desc(pre)) |>
  head(15)

top_15 |>
  pivot_longer(cols = c(pre, post), names_to = "period", values_to = "mean_cases") |>
  mutate(period = if_else(period == "pre", "Pre-Initiative", "Post-Initiative"),
         period = fct_relevel(period, "Pre-Initiative")) |>
  ggplot(aes(x = fct_reorder(country, mean_cases, .desc = TRUE),
             y = mean_cases, fill = period)) +
  geom_col(position = "dodge", width = 0.7) +
  scale_fill_manual(values = c("Pre-Initiative" = bka_red,
                                "Post-Initiative" = bka_teal)) +
  scale_y_continuous(labels = comma) +
  labs(
    title = "Average Measles Cases: Before vs. After the 2001 Initiative",
    subtitle = "Top 15 highest-burden countries — every one improved, but the magnitude varies widely",
    x = NULL, y = "Cases per million", fill = NULL
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = bka_navy),
    plot.subtitle = element_text(color = bka_gray),
    plot.title.position = "plot",
    axis.text.x = element_text(angle = 45, hjust = 1, size = 8)
  )


# 5c. Decline rate dot plot — top 20 fastest-improving countries
top_20_change <- country_summary |>
  head(20)

ggplot(top_20_change, aes(x = pct_change,
                           y = fct_reorder(country, pct_change))) +
  geom_segment(aes(xend = 0, yend = country), color = "grey70") +
  geom_point(size = 4, color = bka_blue) +
  geom_text(aes(label = paste0(pct_change, "%")), hjust = -0.3, size = 3.2) +
  labs(
    title = "Percent Change in Measles Cases After 2001 Initiative",
    subtitle = "Top 20 fastest-improving countries",
    x = "% change in mean cases per million", y = NULL
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", color = bka_navy),
    plot.subtitle = element_text(color = bka_gray),
    plot.title.position = "plot"
  )


## ── 6. THE DIAGNOSTIC QUESTION ──────────────────────────────

# We've shown WHAT happened. Now ask: WHY?

# Compare snapshot years by region
diagnostic <- measles |>
  filter(year %in% c(2000, 2005, 2010, 2020)) |>
  group_by(region, year) |>
  summarize(
    mean_rate = round(mean(cases_per_million, na.rm = TRUE)),
    .groups = "drop"
  ) |>
  pivot_wider(names_from = year, values_from = mean_rate, names_prefix = "y")

diagnostic

# The fastest improvers tend to be in regions with stronger
# health systems and sustained campaign coverage. The slowest
# are often in conflict-affected areas or where campaign
# delivery is logistically harder.
#
# That's not proof of causation — it's a causal hypothesis
# grounded in data.


## ── 7. THE PREDICTIVE QUESTION ──────────────────────────────

# What happens if current trends continue?
# What happens if coverage drops?

# Pick 10 high-burden countries for projection
projection_countries <- country_summary |>
  arrange(desc(pre)) |>
  head(10) |>
  pull(country)

projections <- measles |>
  filter(year >= 2010, country %in% projection_countries) |>
  group_by(country) |>
  do({
    model <- lm(log(pmax(cases_per_million, 1)) ~ year, data = .)
    future_years <- tibble(year = 2024:2030)
    future_years$projected_cases <- round(exp(predict(model, future_years)))
    future_years$country <- unique(.$country)
    future_years
  }) |>
  ungroup()

# Show projected cases for 2030
projections |>
  filter(year == 2030) |>
  arrange(projected_cases) |>
  select(country, projected_cases)

# Scenario comparison: what if decline slows by 50%?
scenario_slowdown <- projections |>
  mutate(scenario = "Current trend") |>
  bind_rows(
    projections |>
      mutate(projected_cases = round(projected_cases * 1.5),
             scenario = "50% slower decline")
  )

# Visualize the two scenarios
ggplot(scenario_slowdown, aes(x = year, y = projected_cases, color = scenario)) +
  geom_line(linewidth = 0.8) +
  facet_wrap(~country, scales = "free_y", ncol = 5) +
  scale_color_manual(values = c("Current trend" = bka_teal,
                                 "50% slower decline" = bka_red)) +
  scale_y_continuous(labels = comma) +
  labs(
    title = "Projected Measles Cases per Million, 2024-2030",
    subtitle = "What happens if progress slows? The gap widens fast in high-burden countries.",
    x = NULL, y = "Projected cases per million", color = NULL
  ) +
  theme_minimal(base_size = 10) +
  theme(
    plot.title = element_text(face = "bold", color = bka_navy),
    plot.subtitle = element_text(color = bka_gray),
    plot.title.position = "plot",
    strip.text = element_text(face = "bold", size = 8),
    legend.position = "top"
  )


## ── Recap ───────────────────────────────────────────────────

# The four core operations map directly to the four quadrants:
#
#   DESCRIPTIVE:  filter + group + summarize → what does the data show?
#   DIAGNOSTIC:   compare (before/after, across groups) → why did it happen?
#   PRESCRIPTIVE: the 5-step process → how to find, analyze, and present
#   PREDICTIVE:   project + model scenarios → what happens next?
#
# You don't need advanced statistics. You need:
#   - A clear question
#   - The discipline to let data surprise you
#   - The courage to say something specific
#
# Start with filter. End with a story.
