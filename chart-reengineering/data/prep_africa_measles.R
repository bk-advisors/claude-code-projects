# prep_africa_measles.R
# Downloads WHO measles data + World Bank population, computes cases per million,
# and saves a clean CSV for the Africa heatmap lesson.
#
# Run once: source("data/prep_africa_measles.R")
# Or: Rscript data/prep_africa_measles.R

library(jsonlite)
library(dplyr)

cat("Processing WHO measles data...\n")

# ---- Load from pre-downloaded JSON files ----
who_raw <- fromJSON("data/who_measles_raw.json")$value
wb_raw  <- fromJSON("data/wb_population_raw.json")[[2]]

# ---- Extract African measles cases ----
measles <- who_raw %>%
  filter(ParentLocation == "Africa") %>%
  transmute(
    country_code = SpatialDim,
    year = as.integer(TimeDim),
    cases = NumericValue
  ) %>%
  filter(year >= 1980, year <= 2023)

cat("  African measles records:", nrow(measles), "\n")

# ---- Extract population ----
pop <- wb_raw %>%
  transmute(
    country_code = countryiso3code,
    year = as.integer(date),
    population = value
  ) %>%
  filter(!is.na(population), !is.na(country_code), country_code != "")

cat("  Population records:", nrow(pop), "\n")

# ---- Get country names from WHO data ----
# Download country dimension lookup
country_url <- "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"
tryCatch({
  country_lookup <- fromJSON(country_url)$value %>%
    transmute(country_code = Code, country = Title)
}, error = function(e) {
  # Fallback: use country codes from the data
  cat("  Warning: Could not fetch country names from WHO API, using codes\n")
  country_lookup <<- measles %>%
    distinct(country_code) %>%
    mutate(country = country_code)
})

# ---- Join and compute cases per million ----
africa_measles <- measles %>%
  left_join(pop, by = c("country_code", "year")) %>%
  left_join(country_lookup, by = "country_code") %>%
  filter(!is.na(population), population > 0) %>%
  mutate(cases_per_million = round(cases / population * 1e6, 1))

# ---- Filter to countries with 15+ years of data ----
good_countries <- africa_measles %>%
  group_by(country) %>%
  summarise(n_years = n(), .groups = "drop") %>%
  filter(n_years >= 15) %>%
  pull(country)

africa_measles <- africa_measles %>%
  filter(country %in% good_countries) %>%
  select(country, country_code, year, cases, population, cases_per_million) %>%
  arrange(country, year)

cat("  Countries with 15+ years:", length(good_countries), "\n")
cat("  Final dataset:", nrow(africa_measles), "rows\n")

# ---- Save ----
write.csv(africa_measles, "data/africa_measles.csv", row.names = FALSE)
cat("Saved: data/africa_measles.csv\n")
