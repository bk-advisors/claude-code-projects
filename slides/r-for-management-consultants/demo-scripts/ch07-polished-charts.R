# ============================================================
#  Chapter 7: Publication-Quality Charts
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================

library(tidyverse)
library(scales)
library(patchwork)

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
          18.5, 23.2, 20.7, 32.8),
  anc_coverage = c(0.85, 0.72, 0.78, 0.55, 0.88, 0.70, 0.75, 0.52,
                   0.90, 0.68, 0.73, 0.48, 0.82, 0.65, 0.70, 0.45,
                   0.92, 0.74, 0.79, 0.58)
)

country_trends <- tibble(
  month   = rep(seq(as.Date("2024-01-01"), as.Date("2024-12-01"), by = "month"), 5),
  country = rep(c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"), each = 12),
  nmr     = c(
    29.1, 28.5, 27.8, 27.2, 26.5, 26.0, 25.3, 24.8, 24.1, 23.5, 23.0, 22.4,
    25.3, 25.0, 24.6, 24.1, 23.7, 23.2, 22.8, 22.3, 21.9, 21.4, 21.0, 20.5,
    22.7, 22.3, 21.8, 21.4, 20.9, 20.5, 20.0, 19.6, 19.1, 18.7, 18.2, 17.8,
    31.8, 31.2, 30.7, 30.1, 29.6, 29.0, 28.5, 27.9, 27.4, 26.8, 26.3, 25.7,
    20.4, 20.0, 19.6, 19.1, 18.7, 18.3, 17.9, 17.5, 17.1, 16.7, 16.3, 15.9
  )
)


## ── Themes ───────────────────────────────────────────────────

p <- ggplot(country_summary, aes(x = reorder(country, avg_nmr), y = avg_nmr)) +
  geom_col(fill = "#005CB9") +
  labs(title = "NMR by Country", x = NULL, y = "NMR")

# Default theme (gray background, grid lines)
p + theme_gray()

# Clean white theme (recommended for presentations)
p + theme_minimal(base_size = 14)

# Classic theme (axes only, no grid)
p + theme_classic(base_size = 14)

# Customizing individual theme elements
p + theme_minimal(base_size = 14) +
  theme(
    plot.title       = element_text(face = "bold", color = "#005CB9"),
    plot.subtitle    = element_text(color = "#666666"),
    axis.title       = element_text(face = "bold"),
    axis.text.x      = element_text(angle = 0),
    panel.grid.major.x = element_blank(),
    panel.grid.minor   = element_blank(),
    legend.position  = "bottom"
  )

# A reusable BKA theme function — define once, use everywhere
theme_bka <- function(base_size = 14) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title    = element_text(face = "bold", color = "#005CB9", size = rel(1.2)),
      plot.subtitle = element_text(color = "#666666", size = rel(0.9)),
      plot.caption  = element_text(color = "#999999", size = rel(0.7)),
      axis.title    = element_text(face = "bold"),
      panel.grid.major.x = element_blank(),
      panel.grid.minor   = element_blank(),
      legend.position    = "bottom",
      strip.text  = element_text(face = "bold", color = "#005CB9")
    )
}

ggplot(country_summary, aes(x = reorder(country, avg_nmr), y = avg_nmr)) +
  geom_col(fill = "#005CB9") +
  labs(title    = "Neonatal Mortality Rate by Country",
       subtitle = "Average across all reporting facilities",
       caption  = "Source: Facility-level data, 2024") +
  theme_bka()


## ── Labels & Scales ──────────────────────────────────────────

# labs(): titles, subtitles, captions, axis labels, legend titles
ggplot(facility_data, aes(x = delivery_volume, y = nmr, color = country)) +
  geom_point(size = 2, alpha = 0.7) +
  labs(
    title    = "Facility Delivery Volume vs. Neonatal Mortality",
    subtitle = "Each point is one health facility (n = 20)",
    x        = "Monthly Delivery Volume",
    y        = "Neonatal Mortality Rate (per 1,000 live births)",
    color    = "Country",
    caption  = "Source: MNH Program Data, 2024 | BK Advisors"
  )

# Format y-axis as percentage
ggplot(facility_data, aes(x = country, y = anc_coverage)) +
  geom_boxplot(fill = "#00A1DF", alpha = 0.5) +
  scale_y_continuous(labels = percent, limits = c(0, 1)) +
  labs(title = "ANC Coverage Distribution by Country",
       y = "ANC Coverage (%)")

# Format y-axis with commas for large numbers
ggplot(country_summary, aes(x = country, y = total_deliveries)) +
  geom_col(fill = "#83BD00") +
  scale_y_continuous(labels = comma) +
  labs(title = "Total Deliveries by Country", y = "Deliveries")


## ── Color Palettes ───────────────────────────────────────────

# BKA brand colors
bka_blue       <- "#005CB9"
bka_light_blue <- "#00A1DF"
bka_green      <- "#83BD00"
bka_teal       <- "#3E9B6E"
bka_red        <- "#E24A3F"
bka_orange     <- "#FA7650"
bka_amber      <- "#F8A623"
bka_yellow     <- "#FED141"

# Named palette for countries
bka_country_colors <- c(
  "Ethiopia"   = bka_blue,
  "Tanzania"   = bka_teal,
  "Malawi"     = bka_green,
  "Mozambique" = bka_orange,
  "Kenya"      = bka_light_blue
)

# Apply to a line chart
ggplot(country_trends, aes(x = month, y = nmr, color = country)) +
  geom_line(linewidth = 1.2) +
  scale_color_manual(values = bka_country_colors) +
  labs(title = "NMR Trends by Country",
       x = "Month", y = "NMR", color = NULL) +
  theme_bka()

# Apply fill scale to bar chart
ggplot(facility_data, aes(x = facility_type, fill = facility_type)) +
  geom_bar() +
  scale_fill_manual(values = c("Hospital"      = bka_blue,
                                "Health Center" = bka_teal,
                                "Health Post"   = bka_green)) +
  labs(title = "Facilities by Type") +
  theme_bka() +
  theme(legend.position = "none")


## ── Faceting — Small Multiples ───────────────────────────────

# facet_wrap(): one variable
ggplot(facility_data, aes(x = nmr)) +
  geom_histogram(binwidth = 5, fill = "#005CB9", color = "white") +
  facet_wrap(~ country, ncol = 3) +
  labs(title = "NMR Distribution by Country",
       x = "NMR (per 1,000 live births)",
       y = "Facilities") +
  theme_bka()

# facet_grid(): two variables (rows ~ columns)
ggplot(facility_data, aes(x = delivery_volume, y = nmr)) +
  geom_point(color = "#005CB9", alpha = 0.6) +
  geom_smooth(method = "lm", se = FALSE, color = "#E24A3F") +
  facet_grid(country ~ facility_type) +
  labs(title    = "Delivery Volume vs. NMR",
       subtitle = "By country and facility type") +
  theme_bka()

# Fixed scales (default) — same axis range for all panels
ggplot(facility_data, aes(x = nmr)) +
  geom_histogram(binwidth = 5, fill = "#005CB9", color = "white") +
  facet_wrap(~ country, ncol = 3) +
  labs(title = "Fixed Scales: Easy to Compare Magnitudes") +
  theme_bka()

# Free y-axis — each panel gets its own range
ggplot(facility_data, aes(x = nmr)) +
  geom_histogram(binwidth = 5, fill = "#005CB9", color = "white") +
  facet_wrap(~ country, ncol = 3, scales = "free_y") +
  labs(title = "Free Y-Axis: Better for Seeing Each Distribution") +
  theme_bka()


## ── Multi-Panel Layouts with patchwork ───────────────────────

# Create individual charts
p1 <- ggplot(country_summary, aes(x = reorder(country, avg_nmr), y = avg_nmr)) +
  geom_col(fill = "#005CB9") +
  labs(title = "NMR by Country", x = NULL, y = "NMR") +
  theme_bka()

p2 <- ggplot(facility_data, aes(x = nmr)) +
  geom_histogram(binwidth = 5, fill = "#3E9B6E", color = "white") +
  labs(title = "NMR Distribution", x = "NMR", y = "Count") +
  theme_bka()

p3 <- ggplot(facility_data, aes(x = delivery_volume, y = nmr)) +
  geom_point(color = "#00A1DF", alpha = 0.5) +
  labs(title = "Volume vs. NMR", x = "Deliveries", y = "NMR") +
  theme_bka()

# Side by side
p1 + p2

# Stack vertically
p1 / p2

# Complex layout: two on top, one below
(p1 + p2) / p3 +
  plot_annotation(title    = "MNH Program Dashboard",
                  subtitle = "Facility-Level Analysis")

# Add panel labels (A, B, C)
(p1 + p2) / p3 +
  plot_annotation(
    title      = "MNH Program Dashboard",
    subtitle   = "Facility-Level Analysis",
    caption    = "Source: MNH Data, 2024",
    tag_levels = "A"
  )


## ── Exporting Charts ─────────────────────────────────────────

# Save the last plot
ggsave("nmr_by_country.png",
       width = 10, height = 6, dpi = 300)

# Save a specific plot object
ggsave("dashboard.png", plot = (p1 + p2) / p3,
       width = 14, height = 10, dpi = 300)

# PDF for print
ggsave("nmr_trend.pdf", width = 10, height = 6)

# SVG for web
ggsave("nmr_trend.svg", width = 10, height = 6)

# Sizing for specific outputs
ggsave("slide_chart.png",  width = 12,  height = 6.75, dpi = 300)  # 16:9 slide
ggsave("half_chart.png",   width = 6,   height = 5,    dpi = 300)  # half-width
ggsave("report_chart.pdf", width = 7,   height = 9)                # A4 portrait
ggsave("square_chart.png", width = 8,   height = 8,    dpi = 300)  # square
