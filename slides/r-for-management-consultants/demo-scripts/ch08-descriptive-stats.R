# ============================================================
#  Chapter 8: Descriptive Statistics for Consultants
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================

library(tidyverse)

# ── Shared dataset ─────────────────────────────────────────────
set.seed(42)
facility_data <- tibble(
  facility_id      = paste0("F", sprintf("%03d", 1:30)),
  country          = rep(c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"), 6),
  facility_type    = sample(c("Hospital", "Health Center", "Health Post"),
                            30, replace = TRUE, prob = c(0.2, 0.5, 0.3)),
  staffing_level   = sample(c("High", "Medium", "Low"), 30, replace = TRUE),
  has_cpap         = sample(c(TRUE, FALSE), 30, replace = TRUE, prob = c(0.4, 0.6)),
  delivery_volume  = sample(20:350, 30, replace = TRUE),
  nmr              = round(runif(30, 12, 55), 1),
  mmr              = round(runif(30, 150, 600), 0),
  anc_coverage     = round(runif(30, 0.35, 0.95), 2),
  training_completed = sample(c(TRUE, FALSE), 30, replace = TRUE)
)


## ── Measures of Central Tendency ─────────────────────────────

nmr_values <- c(12.5, 18.3, 22.1, 25.0, 27.5, 31.7, 35.2, 42.1, 45.3, 68.0)

mean(nmr_values)    # pulled up by the 68.0 outlier
median(nmr_values)  # resistant to outliers

# When to use which?
# Mean:   symmetric distributions, no extreme outliers
# Median: skewed distributions, outliers present

# Spread: standard deviation and IQR
sd(nmr_values)   # standard deviation
IQR(nmr_values)  # interquartile range

# Quantiles
quantile(nmr_values, probs = c(0.25, 0.50, 0.75))

# Range
range(nmr_values)

# Summary statistics by group
facility_data |>
  group_by(country) |>
  summarise(
    n          = n(),
    mean_nmr   = round(mean(nmr, na.rm = TRUE), 1),
    median_nmr = round(median(nmr, na.rm = TRUE), 1),
    sd_nmr     = round(sd(nmr, na.rm = TRUE), 1),
    min_nmr    = min(nmr, na.rm = TRUE),
    max_nmr    = max(nmr, na.rm = TRUE)
  )


## ── Proportions & Cross-Tabulations ──────────────────────────

# Proportion of facilities with CPAP
mean(facility_data$has_cpap, na.rm = TRUE)  # mean() on logical = proportion

# Proportion by country
facility_data |>
  group_by(country) |>
  summarise(
    n           = n(),
    pct_cpap    = round(mean(has_cpap, na.rm = TRUE) * 100, 1),
    pct_trained = round(mean(training_completed, na.rm = TRUE) * 100, 1)
  )

# Two-way frequency table
table(facility_data$country, facility_data$facility_type)

# Row percentages
prop.table(table(facility_data$country, facility_data$facility_type),
           margin = 1) |>
  round(2)

# Tidyverse alternative
facility_data |>
  count(country, facility_type) |>
  group_by(country) |>
  mutate(pct = round(n / sum(n) * 100, 1))


## ── Confidence Intervals ──────────────────────────────────────

# 95% CI for mean NMR
t.test(facility_data$nmr)

# Extract just the confidence interval
t.test(facility_data$nmr)$conf.int

# CI by country (manual formula: mean ± 1.96 × SE)
facility_data |>
  group_by(country) |>
  summarise(
    n        = n(),
    mean_nmr = mean(nmr, na.rm = TRUE),
    se       = sd(nmr, na.rm = TRUE) / sqrt(n()),
    ci_lower = mean_nmr - 1.96 * se,
    ci_upper = mean_nmr + 1.96 * se
  )

# Visualizing confidence intervals with error bars
country_ci <- facility_data |>
  group_by(country) |>
  summarise(
    mean_nmr = mean(nmr, na.rm = TRUE),
    se       = sd(nmr, na.rm = TRUE) / sqrt(n()),
    ci_lower = mean_nmr - 1.96 * se,
    ci_upper = mean_nmr + 1.96 * se
  )

ggplot(country_ci, aes(x = reorder(country, mean_nmr), y = mean_nmr)) +
  geom_point(size = 3, color = "#005CB9") +
  geom_errorbar(aes(ymin = ci_lower, ymax = ci_upper),
                width = 0.2, color = "#005CB9") +
  coord_flip() +
  labs(title = "Mean NMR by Country (with 95% CI)",
       x = NULL, y = "NMR (per 1,000 live births)") +
  theme_minimal(base_size = 14)


## ── Correlation ───────────────────────────────────────────────

# Pearson correlation between delivery volume and NMR
cor(facility_data$delivery_volume, facility_data$nmr,
    use = "complete.obs")

# Correlation test with p-value and CI
cor.test(facility_data$delivery_volume, facility_data$nmr)

# Correlation matrix for multiple variables
facility_data |>
  select(delivery_volume, nmr, mmr, anc_coverage) |>
  cor(use = "complete.obs") |>
  round(2)

# Interpreting r:
# 0.0 – 0.3: Weak
# 0.3 – 0.6: Moderate
# 0.6 – 1.0: Strong
# Remember: correlation ≠ causation


## ── Simple Linear Regression ──────────────────────────────────

# Does delivery volume predict NMR?
model <- lm(nmr ~ delivery_volume, data = facility_data)
summary(model)

# Reading the output:
# Estimate (slope):  "For each additional delivery, NMR changes by ___."
# Std. Error:        Uncertainty around the estimate
# t value / p-value: Statistical significance (p < 0.05 = "significant")
# R-squared:         Proportion of variance explained

# Multiple predictors
model2 <- lm(nmr ~ delivery_volume + has_cpap + staffing_level + anc_coverage,
             data = facility_data)
summary(model2)

# Compare models with AIC (lower = better)
AIC(model, model2)

# Visualize the regression line
ggplot(facility_data, aes(x = delivery_volume, y = nmr)) +
  geom_point(alpha = 0.5, color = "#005CB9") +
  geom_smooth(method = "lm", color = "#E24A3F", fill = "#E24A3F", alpha = 0.2) +
  labs(title    = "NMR vs. Delivery Volume",
       subtitle = paste("R\u00b2 =", round(summary(model)$r.squared, 3)),
       x        = "Monthly Delivery Volume",
       y        = "NMR (per 1,000 live births)") +
  theme_minimal(base_size = 14)
