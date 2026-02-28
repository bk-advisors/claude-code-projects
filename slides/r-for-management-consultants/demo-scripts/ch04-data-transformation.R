# ============================================================
#  Chapter 4: Data Transformation with dplyr
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================

library(tidyverse)

# Build the dataset we'll use throughout
set.seed(42)
facility_data <- tibble(
  facility_id      = paste0("F", sprintf("%03d", 1:30)),
  country          = rep(c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"), 6),
  region           = paste0("Region-", sample(1:5, 30, replace = TRUE)),
  facility_type    = sample(c("Hospital", "Health Center", "Health Post"),
                            30, replace = TRUE, prob = c(0.2, 0.5, 0.3)),
  staffing_level   = sample(c("High", "Medium", "Low"), 30, replace = TRUE),
  has_cpap         = sample(c(TRUE, FALSE), 30, replace = TRUE, prob = c(0.4, 0.6)),
  has_ultrasound   = sample(c(TRUE, FALSE), 30, replace = TRUE, prob = c(0.5, 0.5)),
  delivery_volume  = sample(20:350, 30, replace = TRUE),
  nmr              = round(runif(30, 12, 55), 1),
  mmr              = round(runif(30, 150, 600), 0),
  anc_coverage     = round(runif(30, 0.35, 0.95), 2),
  training_completed = sample(c(TRUE, FALSE), 30, replace = TRUE)
)


## ── The Pipe Operator ─────────────────────────────────────────

# Without pipe — reads inside-out
round(mean(facility_data$nmr, na.rm = TRUE), 1)

# With pipe — reads top to bottom
facility_data$nmr |>
  mean(na.rm = TRUE) |>
  round(1)

# A typical workflow reads like English
facility_data |>
  filter(country == "Ethiopia") |>
  filter(!is.na(nmr)) |>
  summarise(
    n_facilities    = n(),
    avg_nmr         = mean(nmr),
    avg_deliveries  = mean(delivery_volume)
  )


## ── filter() — Subset Rows ────────────────────────────────────

# Single condition
facility_data |> filter(country == "Ethiopia")
facility_data |> filter(nmr > 30)
facility_data |> filter(facility_type == "Hospital")

# Combining conditions
facility_data |> filter(country == "Tanzania", nmr > 25)
facility_data |> filter(country == "Ethiopia" | country == "Kenya")
facility_data |> filter(country %in% c("Ethiopia", "Kenya", "Malawi"))
facility_data |> filter(facility_type != "Health Post")

# Practical filters
facility_data |> filter(nmr > 30, has_cpap == FALSE)
facility_data |> filter(delivery_volume >= 20, !is.na(nmr))
facility_data |> filter(training_completed == TRUE)


## ── select() — Pick Columns ───────────────────────────────────

facility_data |> select(facility_id, country, nmr, delivery_volume)
facility_data |> select(-has_ultrasound, -region)
facility_data |> select(facility_id:facility_type)

# Helper functions
facility_data |> select(starts_with("has_"))
facility_data |> select(where(is.numeric))

# Rename
facility_data |>
  rename(
    neonatal_mortality = nmr,
    maternal_mortality = mmr,
    facility           = facility_id
  )


## ── mutate() — Create New Columns ────────────────────────────

facility_data |>
  mutate(
    anc_pct   = anc_coverage * 100,
    high_risk = nmr > 30
  )

# case_when: conditional categories
facility_data |>
  mutate(
    nmr_category = case_when(
      nmr <= 12  ~ "On Track (SDG Target)",
      nmr <= 25  ~ "Needs Improvement",
      nmr <= 40  ~ "High Risk",
      nmr > 40   ~ "Critical",
      TRUE       ~ "Unknown"
    ),
    size = case_when(
      delivery_volume >= 150 ~ "High Volume",
      delivery_volume >= 50  ~ "Medium Volume",
      TRUE                   ~ "Low Volume"
    )
  )

# Practical derived columns
facility_data |>
  mutate(
    equip_score = as.integer(has_cpap) + as.integer(has_ultrasound),
    anc_gap     = pmax(0.80 - anc_coverage, 0),
    priority    = (nmr > 25) & (staffing_level == "Low")
  )


## ── summarise() + group_by() — Aggregate Data ────────────────

# Overall summary
facility_data |>
  summarise(
    n                = n(),
    avg_nmr          = mean(nmr, na.rm = TRUE),
    median_nmr       = median(nmr, na.rm = TRUE),
    avg_deliveries   = mean(delivery_volume, na.rm = TRUE),
    total_deliveries = sum(delivery_volume, na.rm = TRUE),
    pct_with_cpap    = mean(has_cpap, na.rm = TRUE) * 100
  )

# By country
facility_data |>
  group_by(country) |>
  summarise(
    n_facilities = n(),
    avg_nmr      = round(mean(nmr, na.rm = TRUE), 1),
    avg_deliveries = round(mean(delivery_volume, na.rm = TRUE), 0),
    pct_trained  = round(mean(training_completed, na.rm = TRUE) * 100, 1)
  )

# By two groups
facility_data |>
  group_by(country, facility_type) |>
  summarise(
    n       = n(),
    avg_nmr = mean(nmr, na.rm = TRUE),
    .groups = "drop"
  )

# arrange() — sort results
facility_data |> arrange(nmr)
facility_data |> arrange(desc(nmr))
facility_data |> arrange(country, desc(nmr))

# count() — frequency tables
facility_data |> count(country)
facility_data |> count(country, facility_type)
facility_data |> count(country, sort = TRUE)


## ── Full Pipeline ─────────────────────────────────────────────

facility_data |>
  filter(!is.na(nmr), delivery_volume >= 10) |>
  mutate(
    nmr_status = case_when(
      nmr <= 12 ~ "On Track",
      nmr <= 25 ~ "Progress",
      TRUE      ~ "Off Track"
    )
  ) |>
  group_by(country) |>
  summarise(
    facilities       = n(),
    avg_nmr          = round(mean(nmr), 1),
    pct_on_track     = round(mean(nmr_status == "On Track") * 100, 1),
    total_deliveries = sum(delivery_volume)
  ) |>
  arrange(desc(avg_nmr))
