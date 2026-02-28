# ============================================================
#  Chapter 1: Why R for Management Consultants
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================


## ── The Limits of Spreadsheets ──────────────────────────────

# R as a calculator
2 + 3
10 * 5.5
100 / 7

# Storing a value
maternal_deaths <- 45
total_deliveries <- 1200

# Computing a rate
mmr <- (maternal_deaths / total_deliveries) * 100000
mmr


## ── What Makes R Different ───────────────────────────────────

# Good names — descriptive, lowercase, underscores
neonatal_deaths <- 23
facility_count  <- 48
anc_coverage_pct <- 0.72

# Bad names — unclear, inconsistent
x     <- 23       # What is x?
FC    <- 48       # Abbreviations confuse
ANCcov <- 0.72   # Mixed case is hard to read


## ── Scripts vs. Console ──────────────────────────────────────

# ── MNH Indicator Calculation ──────────────────────
# This script calculates key MNH indicators
# from facility-level delivery data.

# Input data
live_births      <- 1150
stillbirths      <- 50
neonatal_deaths  <- 28
maternal_deaths  <- 3
total_deliveries <- live_births + stillbirths

# Calculate indicators
stillbirth_rate <- (stillbirths / total_deliveries) * 1000
nmr             <- (neonatal_deaths / live_births) * 1000
mmr             <- (maternal_deaths / live_births) * 100000

# Display results
stillbirth_rate  # per 1,000 total deliveries
nmr              # per 1,000 live births
mmr              # per 100,000 live births


## ── Packages — Extending R ───────────────────────────────────

# Install the tidyverse (run once, then comment out)
# install.packages("tidyverse")

# Load it every session
library(tidyverse)
