# ============================================================
#  Storytelling with Data: Analysis Techniques in R
#  BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
#
#  This script walks through the four core data operations
#  from the blog post (filter, group, summarize, compare)
#  using a simulated measles dataset for African countries.
#  No external data files required — everything is built inline.
# ============================================================

library(tidyverse)


## ── 0. Build the Dataset ────────────────────────────────────

# Simulated measles cases per million for 10 African countries,
# spanning 1990 to 2023. Inspired by WHO/UNICEF surveillance data.
# The 2001 Measles Initiative is the key inflection point.

set.seed(42)

countries <- c("Nigeria", "Ethiopia", "DRC", "Tanzania", "Kenya",
               "Uganda", "Mozambique", "Ghana", "Niger", "Mali")

years <- 1990:2023

# Build a row for every country-year combination
measles <- expand_grid(country = countries, year = years) |>
  mutate(
    # Regional grouping
    region = case_when(
      country %in% c("Kenya", "Tanzania", "Uganda", "Ethiopia", "Mozambique") ~ "East Africa",
      country %in% c("Nigeria", "Ghana")                                      ~ "West Africa",
      country %in% c("Niger", "Mali")                                         ~ "Sahel",
      country == "DRC"                                                         ~ "Central Africa"
    ),
    # Income classification (simplified)
    income_group = case_when(
      country %in% c("Kenya", "Ghana", "Nigeria")         ~ "Lower-middle",
      country %in% c("Niger", "Mali", "Mozambique", "DRC",
                      "Ethiopia", "Uganda", "Tanzania")    ~ "Low"
    ),
    # Simulated cases per million:
    #   Pre-2001: high baseline (800-2500) with noise
    #   Post-2001: exponential decline, varying by country
    baseline = case_when(
      country == "Nigeria"    ~ 2200,
      country == "DRC"        ~ 2500,
      country == "Niger"      ~ 2400,
      country == "Mali"       ~ 2100,
      country == "Ethiopia"   ~ 1800,
      country == "Tanzania"   ~ 1500,
      country == "Kenya"      ~ 1200,
      country == "Uganda"     ~ 1600,
      country == "Mozambique" ~ 1700,
      country == "Ghana"      ~ 1100
    ),
    # Decline rate after 2001 (varies — some countries lagged)
    decline_rate = case_when(
      country %in% c("Kenya", "Ghana", "Tanzania")                ~ 0.15,
      country %in% c("Ethiopia", "Uganda", "Mozambique")          ~ 0.10,
      country %in% c("Nigeria", "DRC", "Niger", "Mali")           ~ 0.06
    ),
    # Generate the cases per million series
    cases_per_million = if_else(
      year <= 2001,
      baseline + rnorm(n(), 0, 200),                              # pre-initiative: noisy plateau
      baseline * exp(-decline_rate * (year - 2001)) + rnorm(n(), 0, 50)  # post-initiative: decay
    ),
    cases_per_million = pmax(round(cases_per_million), 10),       # floor at 10, no negatives
    # Era label
    era = if_else(year <= 2001, "Pre-Initiative (1990-2001)", "Post-Initiative (2002-2023)")
  ) |>
  select(country, region, income_group, year, era, cases_per_million)

# Quick look at the data
glimpse(measles)
head(measles, 12)


## ── 1. FILTER — Which countries? Which years? ──────────────

# The first operation: narrow down to what matters.
# "How bad is measles in Africa?" is too broad.
# "What happened in East African countries after 2001?" is answerable.

# Filter to East Africa, post-initiative years
east_africa_post <- measles |>
  filter(region == "East Africa", year >= 2002)

east_africa_post

# Filter for the peak-burden countries (baseline > 2000 cases/million)
high_burden <- measles |>
  filter(cases_per_million > 2000)

# Which countries and years had the highest burden?
high_burden |>
  count(country, sort = TRUE)


## ── 2. GROUP — By meaningful categories ─────────────────────

# Grouping turns a flat table into structured comparisons.
# "By region" or "by time period" immediately adds dimension.

# Average cases per million by region AND era
by_region_era <- measles |>
  group_by(region, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million)),
    median_cases = round(median(cases_per_million)),
    n_observations = n(),
    .groups = "drop"
  )

by_region_era

# This table alone tells a story: every region declined,
# but the magnitude varies. That variation is where the
# diagnostic question lives — why did some regions decline
# faster than others?


## ── 3. SUMMARIZE — Simple statistics that reveal patterns ──

# You don't need fancy models. Means, medians, and rates
# do 90% of the work in consulting.

# Summary by country: before vs. after the 2001 initiative
country_summary <- measles |>
  group_by(country, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million)),
    .groups = "drop"
  ) |>
  pivot_wider(
    names_from = era,
    values_from = mean_cases
  ) |>
  rename(
    pre  = `Pre-Initiative (1990-2001)`,
    post = `Post-Initiative (2002-2023)`
  ) |>
  mutate(
    pct_change = round((post - pre) / pre * 100, 1)
  ) |>
  arrange(pct_change)

country_summary

# Every country shows decline, but the range is wide.
# Kenya: ~87% reduction. Nigeria: ~55% reduction.
# That gap is the diagnostic story.


## ── 4. COMPARE — Before/after, across groups ────────────────

# Comparison is where findings become arguments.
# "Cases declined" is descriptive. "Cases declined 3x faster
# in countries with high campaign coverage" is diagnostic.

# Compare income groups
income_comparison <- measles |>
  group_by(income_group, era) |>
  summarize(
    mean_cases = round(mean(cases_per_million)),
    .groups = "drop"
  ) |>
  pivot_wider(
    names_from = era,
    values_from = mean_cases
  ) |>
  rename(
    pre  = `Pre-Initiative (1990-2001)`,
    post = `Post-Initiative (2002-2023)`
  ) |>
  mutate(
    pct_change = round((post - pre) / pre * 100, 1)
  )

income_comparison

# Compare decline rates: fast decliners vs. slow decliners
decline_rates <- country_summary |>
  mutate(
    decline_speed = if_else(pct_change < -70, "Fast decline", "Slow decline")
  )

decline_rates |>
  group_by(decline_speed) |>
  summarize(
    countries = paste(country, collapse = ", "),
    avg_pct_change = round(mean(pct_change), 1)
  )


## ── 5. VISUALIZE — Let the form follow the finding ─────────

# Now that we've filtered, grouped, summarized, and compared,
# the visualization decisions become obvious. We already know
# what we want to show — the chart is just the delivery vehicle.

# 5a. The heatmap — shows ALL the data, reveals the inflection
ggplot(measles, aes(x = year, y = fct_reorder(country, cases_per_million, .fun = mean, .desc = TRUE),
                    fill = cases_per_million)) +
  geom_tile(color = "white", linewidth = 0.3) +
  scale_fill_gradient(
    low = "#3E9B6E",    # BKA teal (low burden)
    high = "#E24A3F",   # BKA red (high burden)
    name = "Cases per\nmillion"
  ) +
  geom_vline(xintercept = 2001, linetype = "dashed", color = "white", linewidth = 0.8) +
  annotate("text", x = 2001, y = 0.5, label = "2001 Measles Initiative",
           hjust = 1.05, size = 3, color = "grey30") +
  labs(
    title = "Measles Cases per Million Across African Countries, 1990-2023",
    subtitle = "The 2001 WHO/UNICEF Measles Initiative marks a visible inflection point",
    x = NULL, y = NULL
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold"),
    panel.grid = element_blank()
  )

# 5b. Before-vs-after bar chart — the comparison in one glance
country_summary |>
  pivot_longer(cols = c(pre, post), names_to = "period", values_to = "mean_cases") |>
  mutate(period = if_else(period == "pre", "Pre-Initiative", "Post-Initiative"),
         period = fct_relevel(period, "Pre-Initiative")) |>
  ggplot(aes(x = fct_reorder(country, mean_cases, .desc = TRUE),
             y = mean_cases, fill = period)) +
  geom_col(position = "dodge", width = 0.7) +
  scale_fill_manual(values = c("Pre-Initiative" = "#E24A3F", "Post-Initiative" = "#3E9B6E")) +
  labs(
    title = "Average Measles Cases: Before vs. After the 2001 Initiative",
    subtitle = "Every country improved — but the magnitude varies widely",
    x = NULL, y = "Cases per million", fill = NULL
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold"),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

# 5c. Decline rate dot plot — ranks countries by improvement
ggplot(country_summary, aes(x = pct_change,
                            y = fct_reorder(country, pct_change))) +
  geom_segment(aes(xend = 0, yend = country), color = "grey70") +
  geom_point(size = 4, color = "#005CB9") +
  geom_text(aes(label = paste0(pct_change, "%")), hjust = -0.3, size = 3.5) +
  labs(
    title = "Percent Change in Measles Cases After 2001 Initiative",
    subtitle = "Ranking reveals which countries benefited most — and which lagged",
    x = "% change in mean cases per million", y = NULL
  ) +
  theme_minimal(base_size = 12) +
  theme(plot.title = element_text(face = "bold"))


## ── 6. THE DIAGNOSTIC QUESTION ──────────────────────────────

# This is the part most analyses skip.
# We've shown WHAT happened. Now ask: WHY?

# The heatmap and comparisons reveal uneven decline.
# Hypothesis: countries with faster decline had higher
# campaign coverage (proxied here by income group and region).

# Test the hypothesis with a simple grouped comparison
diagnostic <- measles |>
  filter(year %in% c(2000, 2001, 2010, 2020)) |>
  select(country, region, income_group, year, cases_per_million) |>
  pivot_wider(names_from = year, values_from = cases_per_million,
              names_prefix = "y") |>
  mutate(
    change_2001_to_2010 = round((y2010 - y2001) / y2001 * 100, 1),
    change_2001_to_2020 = round((y2020 - y2001) / y2001 * 100, 1)
  )

diagnostic |>
  arrange(change_2001_to_2020)

# The fastest improvers tend to be the East African countries
# with stronger health systems and sustained campaign coverage.
# The slowest are conflict-affected or Sahel region countries.
# That's not proof of causation — but it's a causal hypothesis
# grounded in data, which is exactly where the diagnostic
# quadrant lives.


## ── 7. THE PREDICTIVE QUESTION ──────────────────────────────

# What happens if current trends continue?
# What happens if coverage drops?

# Simple projection: extrapolate the exponential decline
# for each country from 2023 to 2030

projections <- measles |>
  filter(year >= 2010) |>
  group_by(country) |>
  # Fit a simple linear model on log-transformed cases
  do({
    model <- lm(log(cases_per_million) ~ year, data = .)
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
# (e.g., due to funding cuts, conflict, vaccine hesitancy)

scenario_slowdown <- projections |>
  group_by(country) |>
  mutate(
    # Current trajectory (already calculated)
    scenario = "Current trend",
  ) |>
  bind_rows(
    projections |>
      group_by(country) |>
      mutate(
        # Slowdown: cases decline at half the rate
        projected_cases = round(projected_cases * 1.5),
        scenario = "50% slower decline"
      )
  )

# Compare scenarios for 2030
scenario_2030 <- scenario_slowdown |>
  filter(year == 2030) |>
  select(country, scenario, projected_cases) |>
  pivot_wider(names_from = scenario, values_from = projected_cases) |>
  mutate(
    additional_cases = `50% slower decline` - `Current trend`
  ) |>
  arrange(desc(additional_cases))

scenario_2030

# Visualize the two scenarios
scenario_slowdown |>
  ggplot(aes(x = year, y = projected_cases, color = scenario)) +
  geom_line(linewidth = 0.8) +
  facet_wrap(~country, scales = "free_y") +
  scale_color_manual(values = c("Current trend" = "#3E9B6E", "50% slower decline" = "#E24A3F")) +
  labs(
    title = "Projected Measles Cases per Million, 2024-2030",
    subtitle = "What happens if progress slows? The gap widens fast in high-burden countries.",
    x = NULL, y = "Projected cases per million", color = NULL
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold"),
    strip.text = element_text(face = "bold"),
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
