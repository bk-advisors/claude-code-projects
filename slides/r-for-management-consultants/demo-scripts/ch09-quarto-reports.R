# ============================================================
#  Chapter 9: Reproducible Reports with Quarto
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
#
#  Note: Most of this chapter is about .qmd file structure.
#  This script demonstrates the R code that goes INSIDE a Quarto
#  document. The commented blocks show the .qmd syntax around it.
# ============================================================

library(tidyverse)
library(knitr)

# ── Demo dataset ───────────────────────────────────────────────
set.seed(42)
facility_data <- tibble(
  facility_id        = paste0("F", sprintf("%03d", 1:30)),
  country            = rep(c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya"), 6),
  facility_type      = sample(c("Hospital", "Health Center", "Health Post"),
                              30, replace = TRUE, prob = c(0.2, 0.5, 0.3)),
  has_cpap           = sample(c(TRUE, FALSE), 30, replace = TRUE, prob = c(0.4, 0.6)),
  delivery_volume    = sample(20:350, 30, replace = TRUE),
  nmr                = round(runif(30, 12, 55), 1),
  anc_coverage       = round(runif(30, 0.35, 0.95), 2),
  training_completed = sample(c(TRUE, FALSE), 30, replace = TRUE)
)


## ── What Is Quarto? ───────────────────────────────────────────

# A Quarto document (.qmd) has three parts:
#
# 1. YAML header (between --- markers): metadata and output format
# 2. Markdown text: narrative, headings, bullet points
# 3. Code chunks (between ```{r} and ``` markers): R analysis
#
# Example YAML header:
# ---
# title: "MNH Program Brief"
# author: "BK Advisors"
# date: today
# format: html
# ---


## ── Document Structure ────────────────────────────────────────

# A minimal Quarto document looks like this:
#
# ---
# title: "MNH Program Brief"
# author: "BK Advisors"
# date: today
# format: html
# ---
#
# ## Executive Summary
#
# This report summarizes maternal and newborn health indicators
# across **five program countries** for Q4 2024.
#
# ```{r}
# library(dplyr)
# library(ggplot2)
#
# facility_data |>
#   group_by(country) |>
#   summarise(avg_nmr = mean(nmr, na.rm = TRUE))
# ```
#
# ## Key Findings
#
# The average NMR across all facilities is declining.


## ── Code Chunks ───────────────────────────────────────────────

# Key chunk options (set with #| syntax at the top of each chunk):
#
# #| echo: true     Show the code in the output
# #| echo: false    Hide the code (show only results)
# #| eval: true     Run the code
# #| eval: false    Show code but don't run it
# #| warning: false Suppress warning messages
# #| fig-width: 10  Set figure width (inches)
# #| fig-height: 6  Set figure height (inches)
# #| tbl-cap: "..."  Add a table caption
#
# For donor reports: set echo: false globally so stakeholders
# see only results. For internal documents: keep echo: true.


## ── Tables with knitr::kable() ────────────────────────────────

# Build a summary table
country_summary <- facility_data |>
  group_by(country) |>
  summarise(
    Facilities   = n(),
    `Mean NMR`   = round(mean(nmr, na.rm = TRUE), 1),
    `Median NMR` = round(median(nmr, na.rm = TRUE), 1),
    `% with CPAP` = round(mean(has_cpap, na.rm = TRUE) * 100, 1)
  )

# Render as a clean table
kable(country_summary, caption = "MNH Indicators by Country")


## ── Charts in Documents ───────────────────────────────────────

# This chart renders directly into a rendered Quarto report
# (In a .qmd file, add: #| fig-width: 8 and #| fig-height: 5)
ggplot(country_summary, aes(x = reorder(country, `Mean NMR`), y = `Mean NMR`)) +
  geom_col(fill = "#005CB9") +
  geom_text(aes(label = `Mean NMR`), hjust = -0.2, size = 4) +
  coord_flip() +
  labs(title = "Average NMR by Country",
       x = NULL, y = "NMR (per 1,000 live births)") +
  theme_minimal(base_size = 14)


## ── Inline R Code ─────────────────────────────────────────────

# Computed values for inline use
avg_nmr       <- round(mean(facility_data$nmr), 1)
n_facilities  <- nrow(facility_data)
n_countries   <- n_distinct(facility_data$country)

avg_nmr
n_facilities
n_countries

# In a .qmd file, inline R uses backtick-r syntax in markdown text:
#
# "The average NMR across all facilities is `r avg_nmr`
#  per 1,000 live births, based on data from `r n_facilities` facilities
#  across `r n_countries` countries."
#
# When rendered, this becomes:
# "The average NMR across all facilities is 33.5 per 1,000 live births,
#  based on data from 30 facilities across 5 countries."
#
# Inline R eliminates copy-paste errors — numbers update automatically.


## ── Output Formats ───────────────────────────────────────────

# Change the format in the YAML header:
#
# format: html     → Interactive web page (default, no extra software)
# format: pdf      → Print-ready document (requires TinyTeX)
# format: docx     → Microsoft Word (recipients can edit text)
#
# Multiple formats at once:
# format:
#   html: default
#   docx: default
#   pdf: default
#
# Render from the command line (Terminal tab in RStudio):
# quarto render mnh_brief.qmd
# quarto render mnh_brief.qmd --to docx
# quarto render mnh_brief.qmd --to pdf
#
# Or press Ctrl+Shift+K in RStudio to render the current .qmd file.


## ── Parameterized Reports ────────────────────────────────────

# Step 1: Add params to the YAML header of your .qmd file:
# ---
# title: "MNH Country Brief"
# params:
#   country: "Ethiopia"
# format: html
# ---
#
# Step 2: Use params$country anywhere in the document
country_data <- facility_data |>
  filter(country == params$country)  # params$country comes from the YAML

# Step 3: Compute values for this country
n_fac   <- nrow(country_data)
avg_nmr <- round(mean(country_data$nmr, na.rm = TRUE), 1)

n_fac
avg_nmr

# Step 4: Use inline R in narrative:
# "This brief covers `r n_fac` facilities in `r params$country`,
#  with an average NMR of `r avg_nmr` per 1,000 live births."

# Step 5: Render one report per country from R
countries <- c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya")

for (ctry in countries) {
  quarto::quarto_render(
    input        = "country_brief.qmd",
    output_file  = paste0("brief_", tolower(ctry), ".html"),
    execute_params = list(country = ctry)
  )
}
# Produces: brief_ethiopia.html, brief_tanzania.html, etc.
# Five country briefs from one template — re-run when data updates.
