# ============================================================
#  Chapter 5: Reshaping & Joining Datasets
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================

library(tidyverse)


## ── Wide vs. Long Format ─────────────────────────────────────

# Wide: one row per facility, months as columns
wide_data <- tibble(
  facility_id = c("F001", "F002", "F003"),
  country     = c("Ethiopia", "Tanzania", "Malawi"),
  jan         = c(45, 120, 33),
  feb         = c(52, 115, 38),
  mar         = c(48, 130, 35)
)
wide_data

# Long: one row per facility per month (ready for ggplot2)
long_data <- wide_data |>
  pivot_longer(
    cols      = jan:mar,
    names_to  = "month",
    values_to = "deliveries"
  )
long_data


## ── pivot_longer() ───────────────────────────────────────────

# Quarterly NMR (DHIS2 export — wide format)
quarterly <- tibble(
  facility_id = c("F001", "F002", "F003"),
  nmr_q1      = c(22.1, 31.7, 45.3),
  nmr_q2      = c(20.8, 29.5, 42.0),
  nmr_q3      = c(19.5, 28.1, 38.8),
  nmr_q4      = c(18.2, 27.0, 36.5)
)

quarterly_long <- quarterly |>
  pivot_longer(
    cols        = starts_with("nmr_"),
    names_to    = "quarter",
    names_prefix = "nmr_",    # strip the "nmr_" prefix
    values_to   = "nmr"
  )
quarterly_long


## ── pivot_wider() ────────────────────────────────────────────

# Long: indicator values per country (one row per indicator)
indicators_long <- tibble(
  country   = rep(c("Ethiopia", "Tanzania", "Malawi"), each = 3),
  indicator = rep(c("nmr", "mmr", "anc_coverage"), 3),
  value     = c(25.3, 353, 0.62,
                31.7, 524, 0.51,
                19.8, 439, 0.71)
)
indicators_long

# Wide: summary table (one row per country)
indicators_wide <- indicators_long |>
  pivot_wider(
    names_from  = indicator,
    values_from = value
  )
indicators_wide


## ── Joining Datasets ─────────────────────────────────────────

# Base tables
facilities <- tibble(
  facility_id   = c("F001", "F002", "F003", "F004"),
  country       = c("Ethiopia", "Tanzania", "Malawi", "Kenya"),
  facility_type = c("Hospital", "Health Center", "Health Post", "Hospital")
)

country_data <- tibble(
  country                = c("Ethiopia", "Tanzania", "Malawi", "Mozambique"),
  gdp_per_capita         = c(936, 1136, 625, 504),
  health_expenditure_pct = c(3.3, 3.6, 9.3, 4.9)
)

# left_join: keep all facilities, add country data where it exists
facilities |>
  left_join(country_data, by = "country")
# Kenya gets NA (no match in country_data)
# Mozambique is dropped (no match in facilities)

# Monthly deliveries joined with facility characteristics
monthly <- tibble(
  facility_id = rep(c("F001", "F002"), each = 3),
  month       = rep(c("Jan", "Feb", "Mar"), 2),
  deliveries  = c(45, 52, 48, 120, 115, 130)
)

monthly |>
  left_join(facilities, by = "facility_id")

# bind_rows: stack quarterly files
q1_data <- tibble(facility_id = c("F001", "F002"), quarter = "Q1", deliveries = c(135, 365))
q2_data <- tibble(facility_id = c("F001", "F002"), quarter = "Q2", deliveries = c(148, 350))
q3_data <- tibble(facility_id = c("F001", "F002"), quarter = "Q3", deliveries = c(141, 378))

annual_data <- bind_rows(q1_data, q2_data, q3_data)
annual_data

# anti_join: find non-reporters
all_facilities <- tibble(facility_id = c("F001", "F002", "F003", "F004", "F005"))
reported       <- tibble(facility_id = c("F001", "F003", "F005"), deliveries = c(45, 33, 120))

all_facilities |>
  anti_join(reported, by = "facility_id")
# F002 and F004 didn't report — follow up!


## ── String Basics with stringr ────────────────────────────────

library(stringr)

facility_names <- c("Addis Ababa Hospital", "addis ababa hospital",
                    "  Dar es Salaam HC  ", "Lilongwe Health Centre")

# Fix inconsistent formatting
str_to_title(facility_names)
str_trim(facility_names)
str_detect(facility_names, "Hospital|hospital")
str_replace(facility_names, "HC", "Health Center")

# Chained cleaning
facility_names |>
  str_trim() |>
  str_to_title() |>
  str_replace_all("Hc\\b", "Health Center") |>
  str_replace_all("Hp\\b", "Health Post")
