# ============================================================
#  Chapter 6: Data Visualization with ggplot2
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================

library(tidyverse)

# ── Shared datasets ───────────────────────────────────────────
country_summary <- tibble(
  country          = c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"),
  avg_nmr          = c(29.1, 25.3, 22.7, 31.8, 20.4),
  total_deliveries = c(12500, 9800, 7200, 5400, 11300)
)

facility_data <- tibble(
  facility_id   = paste0("F", sprintf("%03d", 1:20)),
  country       = rep(c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"), each = 4),
  facility_type = rep(c("Hospital", "Health Center", "Health Center", "Health Post"), 5),
  delivery_volume = c(320, 145, 160, 45, 280, 130, 155, 38,
                      210, 95, 110, 32, 175, 80, 90, 28,
                      290, 125, 140, 42),
  nmr = c(25.3, 31.7, 28.9, 42.1, 22.8, 27.5, 24.3, 38.6,
          19.8, 25.1, 22.4, 35.3, 28.7, 33.9, 30.1, 45.2,
          18.5, 23.2, 20.7, 32.8)
)

monthly_trends <- tibble(
  month   = rep(seq(as.Date("2024-01-01"), as.Date("2024-12-01"), by = "month"), 3),
  country = rep(c("Ethiopia", "Tanzania", "Malawi"), each = 12),
  nmr     = c(
    29.1, 28.5, 27.8, 27.2, 26.5, 26.0, 25.3, 24.8, 24.1, 23.5, 23.0, 22.4,
    25.3, 25.0, 24.6, 24.1, 23.7, 23.2, 22.8, 22.3, 21.9, 21.4, 21.0, 20.5,
    22.7, 22.3, 21.8, 21.4, 20.9, 20.5, 20.0, 19.6, 19.1, 18.7, 18.2, 17.8
  )
)


## ── The Grammar of Graphics ───────────────────────────────────

# Three layers: DATA + AESTHETICS + GEOMETRY
ggplot(data = facility_data,
       aes(x = country, y = nmr)) +
  geom_col()

# Add color as an aesthetic mapping
ggplot(facility_data, aes(x = delivery_volume, y = nmr, color = country)) +
  geom_point()

# Add size to encode a third variable
ggplot(facility_data, aes(x = delivery_volume, y = nmr,
                           color = country, size = delivery_volume)) +
  geom_point(alpha = 0.7)


## ── Bar Charts ───────────────────────────────────────────────

# geom_col: your data already has the values
ggplot(country_summary, aes(x = country, y = avg_nmr)) +
  geom_col(fill = "#005CB9") +
  labs(
    title = "Average Neonatal Mortality Rate by Country",
    x     = NULL,
    y     = "NMR (per 1,000 live births)"
  )

# geom_bar: ggplot counts the rows for you
ggplot(facility_data, aes(x = facility_type)) +
  geom_bar(fill = "#3E9B6E") +
  labs(title = "Number of Facilities by Type", x = NULL, y = "Count")

# Stacked bars
ggplot(facility_data, aes(x = country, fill = facility_type)) +
  geom_bar() +
  scale_fill_manual(values = c(
    "Hospital"      = "#005CB9",
    "Health Center" = "#3E9B6E",
    "Health Post"   = "#FA7650"
  )) +
  labs(
    title = "Facility Type Distribution by Country",
    x     = NULL,
    y     = "Number of Facilities",
    fill  = "Facility Type"
  )

# Horizontal bars ordered by value (consulting standard)
ggplot(country_summary, aes(x = reorder(country, avg_nmr), y = avg_nmr)) +
  geom_col(fill = "#005CB9") +
  coord_flip() +
  labs(title = "NMR by Country (Ranked)", x = NULL, y = "NMR")


## ── Scatter Plots ─────────────────────────────────────────────

# Basic scatter
ggplot(facility_data, aes(x = delivery_volume, y = nmr)) +
  geom_point(color = "#005CB9", size = 3, alpha = 0.7) +
  labs(
    title = "Delivery Volume vs. Neonatal Mortality Rate",
    x     = "Monthly Delivery Volume",
    y     = "NMR (per 1,000 live births)"
  )

# Color by country
ggplot(facility_data, aes(x = delivery_volume, y = nmr, color = country)) +
  geom_point(size = 3, alpha = 0.7) +
  scale_color_manual(values = c(
    "Ethiopia"   = "#005CB9",
    "Tanzania"   = "#3E9B6E",
    "Malawi"     = "#00A1DF",
    "Mozambique" = "#FA7650",
    "Kenya"      = "#E24A3F"
  )) +
  labs(
    title  = "Delivery Volume vs. NMR by Country",
    x      = "Monthly Delivery Volume",
    y      = "NMR (per 1,000 live births)",
    color  = "Country"
  )

# Add a linear trend line
ggplot(facility_data, aes(x = delivery_volume, y = nmr)) +
  geom_point(color = "#005CB9", size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = TRUE, color = "#E24A3F", linewidth = 1) +
  labs(
    title    = "Delivery Volume vs. NMR with Trend Line",
    subtitle = "Linear regression fit with 95% confidence interval",
    x        = "Monthly Delivery Volume",
    y        = "NMR (per 1,000 live births)"
  )

# Separate trend per country
ggplot(facility_data, aes(x = delivery_volume, y = nmr, color = country)) +
  geom_point(size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, linewidth = 1) +
  scale_color_manual(values = c(
    "Ethiopia"   = "#005CB9",
    "Tanzania"   = "#3E9B6E",
    "Malawi"     = "#00A1DF",
    "Mozambique" = "#FA7650",
    "Kenya"      = "#E24A3F"
  )) +
  labs(
    title    = "Volume-NMR Relationship by Country",
    subtitle = "Each line is a separate linear fit per country",
    x        = "Monthly Delivery Volume",
    y        = "NMR (per 1,000 live births)",
    color    = "Country"
  )


## ── Line Charts ───────────────────────────────────────────────

# Single country trend
ethiopia_trends <- monthly_trends |> filter(country == "Ethiopia")

ggplot(ethiopia_trends, aes(x = month, y = nmr)) +
  geom_line(color = "#005CB9", linewidth = 1.2) +
  geom_point(color = "#005CB9", size = 2) +
  labs(
    title    = "Neonatal Mortality Rate Trend — Ethiopia",
    subtitle = "Monthly NMR, January–December 2024",
    x        = NULL,
    y        = "NMR (per 1,000 live births)"
  )

# Multiple countries
ggplot(monthly_trends, aes(x = month, y = nmr, color = country)) +
  geom_line(linewidth = 1.2) +
  geom_point(size = 2) +
  scale_color_manual(values = c(
    "Ethiopia" = "#005CB9",
    "Tanzania" = "#3E9B6E",
    "Malawi"   = "#00A1DF"
  )) +
  labs(
    title    = "NMR Trends by Country",
    subtitle = "Monthly neonatal mortality rate, 2024",
    x        = NULL,
    y        = "NMR (per 1,000 live births)",
    color    = NULL
  )

# Add SDG target reference line
ggplot(monthly_trends, aes(x = month, y = nmr, color = country)) +
  geom_line(linewidth = 1.2) +
  geom_hline(yintercept = 12, linetype = "dashed", color = "#999999") +
  annotate("text", x = as.Date("2024-10-01"), y = 13,
           label = "SDG Target: 12", color = "#999999", size = 3.5) +
  scale_color_manual(values = c(
    "Ethiopia" = "#005CB9",
    "Tanzania" = "#3E9B6E",
    "Malawi"   = "#00A1DF"
  )) +
  labs(
    title    = "NMR Trends vs. SDG Target",
    subtitle = "All countries still above the SDG 3.2 target of 12 per 1,000",
    x        = NULL,
    y        = "NMR (per 1,000 live births)",
    color    = NULL
  )


## ── Histograms & Box Plots ────────────────────────────────────

# Histogram: distribution of NMR across facilities
ggplot(facility_data, aes(x = nmr)) +
  geom_histogram(binwidth = 5, fill = "#005CB9", color = "white") +
  labs(
    title    = "Distribution of Neonatal Mortality Rates",
    subtitle = "Across all reporting facilities (n = 20)",
    x        = "NMR (per 1,000 live births)",
    y        = "Number of Facilities"
  )

# Overlapping histograms by facility type
ggplot(facility_data, aes(x = nmr, fill = facility_type)) +
  geom_histogram(binwidth = 5, alpha = 0.6, position = "identity", color = "white") +
  scale_fill_manual(values = c(
    "Hospital"      = "#005CB9",
    "Health Center" = "#3E9B6E",
    "Health Post"   = "#FA7650"
  )) +
  labs(
    title = "NMR Distribution by Facility Type",
    x     = "NMR (per 1,000 live births)",
    y     = "Number of Facilities",
    fill  = "Facility Type"
  )

# Box plot by country
ggplot(facility_data, aes(x = country, y = nmr, fill = country)) +
  geom_boxplot(alpha = 0.7, show.legend = FALSE) +
  scale_fill_manual(values = c(
    "Ethiopia"   = "#005CB9",
    "Tanzania"   = "#3E9B6E",
    "Malawi"     = "#00A1DF",
    "Mozambique" = "#FA7650",
    "Kenya"      = "#E24A3F"
  )) +
  labs(title = "NMR Distribution by Country", x = NULL, y = "NMR (per 1,000 live births)")

# Box plot by country AND facility type
ggplot(facility_data, aes(x = country, y = nmr, fill = facility_type)) +
  geom_boxplot(alpha = 0.7) +
  scale_fill_manual(values = c(
    "Hospital"      = "#005CB9",
    "Health Center" = "#3E9B6E",
    "Health Post"   = "#FA7650"
  )) +
  labs(
    title    = "NMR by Country and Facility Type",
    subtitle = "Health posts consistently show higher NMR across countries",
    x        = NULL,
    y        = "NMR (per 1,000 live births)",
    fill     = "Facility Type"
  )
