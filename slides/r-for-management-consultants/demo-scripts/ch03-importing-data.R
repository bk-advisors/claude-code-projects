# ============================================================
#  Chapter 3: Importing & Exploring Data
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
#
#  Note: read_csv() / read_excel() examples show the syntax;
#  we create facility_data inline for the exploration demos.
# ============================================================

library(tidyverse)
library(readxl)


## ── Reading CSV Files ─────────────────────────────────────────

# Basic import
# facility_data <- read_csv("facility_data.csv")

# Specify column types explicitly (avoids surprises)
# facility_data <- read_csv(
#   "facility_data.csv",
#   col_types = cols(
#     facility_id     = col_character(),
#     country         = col_character(),
#     facility_type   = col_character(),
#     delivery_volume = col_integer(),
#     nmr             = col_double(),
#     has_cpap        = col_logical()
#   )
# )

# Handle messy DHIS2 exports
# facility_data <- read_csv(
#   "dhis2_export_2024.csv",
#   skip   = 2,
#   na     = c("", "NA", ".", "--", "N/A"),
#   locale = locale(encoding = "UTF-8")
# )


## ── Reading Excel Files ───────────────────────────────────────

# facility_data   <- read_excel("mnh_indicators.xlsx")
# delivery_data   <- read_excel("mnh_indicators.xlsx", sheet = "Deliveries")
# staffing_data   <- read_excel("mnh_indicators.xlsx", sheet = 3)

# Skip header rows (common in government reports)
# facility_data <- read_excel(
#   "ministry_report.xlsx",
#   sheet = "FacilityData",
#   skip  = 4
# )

# List all sheets
# excel_sheets("ministry_report.xlsx")


## ── Data Frames & Tibbles ────────────────────────────────────

# Create our demo dataset inline
facility_data <- tibble(
  facility_id     = c("ETH-001", "ETH-002", "KEN-001", "MWI-001", "TZA-001"),
  country         = c("Ethiopia", "Ethiopia", "Kenya", "Malawi", "Tanzania"),
  facility_type   = c("Hospital", "Health Center", "Hospital", "Hospital", "Health Center"),
  delivery_volume = c(245, 58, 312, 189, 73),
  nmr             = c(28.5, NA, 19.2, 35.1, 22.8),
  has_cpap        = c(TRUE, FALSE, TRUE, FALSE, FALSE)
)
facility_data

# Tibble vs data.frame behaviour
facility_data$nmr      # dollar sign
facility_data[["nmr"]] # double bracket — same result

# Row/column subsetting
facility_data[1, ]
facility_data[, c(2, 3)]
facility_data[1:3, c("country", "nmr")]


## ── Exploring Your Data ───────────────────────────────────────

# Dimensions
nrow(facility_data)
ncol(facility_data)
dim(facility_data)

# First few rows
head(facility_data)
head(facility_data, 10)

# Column-by-column overview
glimpse(facility_data)

# Statistical summary
summary(facility_data)


## ── Handling Missing Values ───────────────────────────────────

# NA is contagious
5 + NA
mean(c(10, 20, NA))
mean(c(10, 20, NA), na.rm = TRUE)  # 15

# Count NAs per column
colSums(is.na(facility_data))

# Percentage missing
colMeans(is.na(facility_data)) * 100

# Remove rows where nmr is NA (targeted — preferred)
clean_data <- facility_data |>
  filter(!is.na(nmr))
clean_data

# Remove rows missing any of several key columns
clean_data2 <- facility_data |>
  filter(!is.na(nmr), !is.na(delivery_volume))

# na.rm in calculations
mean(facility_data$nmr)                 # NA
mean(facility_data$nmr, na.rm = TRUE)   # 26.4
sum(facility_data$delivery_volume, na.rm = TRUE)
median(facility_data$nmr, na.rm = TRUE)
sd(facility_data$nmr, na.rm = TRUE)
min(facility_data$nmr, na.rm = TRUE)
max(facility_data$nmr, na.rm = TRUE)
