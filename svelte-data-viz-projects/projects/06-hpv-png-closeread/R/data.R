# HPV Vaccination Data for Papua New Guinea Story
# Sources: Global Cancer Observatory (GCO), Globocan, UNFPA, Gavi, WHO

library(tibble)

# Cervical Cancer Mortality Rates in Asia-Pacific (2022)
# Age-standardized mortality rate per 100,000 women
# Source: Ueda (2024), Journal of Obstetrics and Gynaecology Research
mortality_rates <- tibble(
  country = c("Fiji", "Papua New Guinea", "Solomon Islands", "Vanuatu",
              "Myanmar", "Indonesia", "Maldives", "Guam", "India",
              "Mongolia", "Australia"),
  rate = c(22.5, 19.9, 17.9, 13.6, 13.4, 13.2, 12.9, 11.2, 11.2, 9.6, 1.7),
  region = c("Pacific", "Pacific", "Pacific", "Pacific", "Asia", "Asia",
             "Asia", "Pacific", "Asia", "Asia", "Pacific"),
  highlight = c(FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE,
                FALSE, FALSE, FALSE)
)

# Global cervical cancer deaths by region (2022)
# Source: Global Cancer Observatory (GCO, 2022)
global_deaths <- list(
  total = 348709,
  asia_pacific = 197217,
  asia_pacific_percent = 56.6,
  other_regions = 151492,
  other_regions_percent = 43.4
)

# PNG-specific statistics
# Source: Globocan PNG Factsheet, 2022
png_stats <- list(
  new_cases_per_year = 1053,
  mortality_rate = 19.9,
  global_rank = 12,
  regional_rank = 2,
  cancer_rank_in_women = 2
)

# Projected lives saved from HPV vaccination (2026-2070)
# Based on Gavi estimate of 17.4 deaths averted per 1,000 vaccinated
projected_lives_saved <- tibble(
  year = c(2026, 2027, 2028, 2029, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070),
  cumulative_lives_saved = c(3480, 4872, 6293, 7743, 9223, 17385, 27123, 38592,
                              52003, 67618, 75893, 85234, 96905),
  girls_vaccinated = c(200000, 280000, 361440, 444347, 528747, 998975, 1558641,
                       2218168, 2989041, 3885257, 4362582, 4898509, 5569161)
)

# Deaths without intervention projection
# Source: UNFPA and IARC analyses
deaths_without_action <- list(
  by_2070 = 60232,
  by_2120 = 148000
)

# Vaccination impact statistics
# Source: Gavi HPV Impact Report, 2022
vaccination_impact <- list(
  deaths_averted_per_1000 = 17.4,
  target_age_group = "9-14 year old girls",
  total_lives_saved_by_2070 = 96905,
  total_girls_vaccinated_by_2070 = 5569161
)

# Economic analysis
# Source: UNFPA PNG-specific modelling
economic_data <- list(
  investment_first_10_years = 21000000,  # USD 20-21 million
  return_per_1_dollar_30_years = 19,
  return_per_1_dollar_50_years = 61.32,
  lives_saved_by_2120_with_strategy = 148000,
  lives_saved_by_2120_vaccine_only = 100000
)

# Comparison data - PNG vs Australia
comparison_data <- tibble(
  country = c("Papua New Guinea", "Australia"),
  incidence = c(34.9, 6.4),
  mortality = c(19.9, 1.7),
  screening_program = c(FALSE, TRUE),
  hpv_vaccine_national = c(FALSE, TRUE)
)

# ROI data for visualization
roi_data <- tibble(
  period = c("Investment", "30-year return", "50-year return"),
  value = c(1, 19, 61.32),
  label = c("$1", "$19", "$61"),
  is_investment = c(TRUE, FALSE, FALSE)
)
