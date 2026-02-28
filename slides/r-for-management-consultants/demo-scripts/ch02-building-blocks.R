# ============================================================
#  Chapter 2: R Building Blocks
#  R for Management Consultants | BK Advisors
#
#  Live demo script — run line-by-line with Ctrl+Enter in RStudio
# ============================================================


## ── Vectors ──────────────────────────────────────────────────

# A single value is actually a vector of length 1
neonatal_deaths <- 23
length(neonatal_deaths)  # 1

# A vector of neonatal mortality rates (per 1,000 live births)
nmr <- c(25.3, 31.7, 19.8, 42.1, 27.5)
nmr
length(nmr)  # 5

# Named vectors: NMR by country
nmr <- c(
  Ethiopia   = 25.3,
  Tanzania   = 31.7,
  Malawi     = 19.8,
  Mozambique = 42.1,
  Kenya      = 27.5
)
nmr

# Monthly deliveries at a facility
deliveries <- c(
  Jan = 112, Feb = 98,  Mar = 134,
  Apr = 121, May = 105, Jun = 143
)
deliveries

# Summary statistics on a vector
mean(nmr)
sum(nmr)
min(nmr)
max(nmr)
range(nmr)

# Vectorized math: operates on every element at once
live_births     <- c(1200, 950, 1100, 800, 1050)
neonatal_deaths <- c(30, 30, 22, 34, 29)
nmr_calculated  <- (neonatal_deaths / live_births) * 1000
nmr_calculated

# Indexing by position
nmr[1]
nmr[c(1, 3)]
nmr[2:4]
nmr[-4]          # exclude Mozambique

# Indexing by name
nmr["Ethiopia"]
nmr[c("Malawi", "Kenya")]

# Indexing by condition
nmr[nmr > 30]
nmr[nmr <= 12]   # SDG target
names(nmr[nmr > 30])
sum(nmr > 25)    # how many countries exceed 25?

# Modifying vectors
nmr["Tanzania"] <- 29.4  # updated data
nmr["Uganda"]   <- 22.1  # new country
sort(nmr)
sort(nmr, decreasing = TRUE)


## ── Data Types ───────────────────────────────────────────────

class(25.3)        # "numeric"
class("Ethiopia")  # "character"
class(TRUE)        # "logical"

# Numeric
nmr       <- c(25.3, 31.7, 19.8, 42.1, 27.5)
deliveries <- c(1200L, 950L, 1100L, 800L, 1050L)  # L = integer
class(nmr)
class(deliveries)
is.numeric(nmr)

# Character
countries   <- c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya")
facility_ids <- c("ETH-HC-042", "TZA-HOSP-007", "MWI-HP-118")
nchar(countries)
toupper(countries)
paste(countries, "NMR:", nmr)

# Logical
has_cpap      <- c(TRUE, FALSE, TRUE, FALSE, TRUE)
has_ultrasound <- c(TRUE, TRUE, FALSE, FALSE, TRUE)
nmr <- c(Ethiopia = 25.3, Tanzania = 31.7, Malawi = 19.8,
         Mozambique = 42.1, Kenya = 27.5)
high_nmr <- nmr > 30
high_nmr

# TRUE = 1, FALSE = 0
sum(has_cpap)       # count with CPAP
mean(has_cpap)      # proportion
mean(has_cpap) * 100  # percentage

# Factor
facility_type <- factor(
  c("Hospital", "Health Center", "Health Post", "Health Center", "Hospital")
)
facility_type
levels(facility_type)

# Ordered factor
facility_type <- factor(
  c("Hospital", "Health Center", "Health Post", "Health Center", "Hospital"),
  levels  = c("Health Post", "Health Center", "Hospital"),
  ordered = TRUE
)
facility_type

# Missing values
deliveries <- c(112, 98, NA, 121, NA, 143)
mean(deliveries)                     # NA — contagious!
mean(deliveries, na.rm = TRUE)       # 118.5
sum(is.na(deliveries))               # 2 missing


## ── Comparison & Logical Operators ───────────────────────────

nmr <- c(Ethiopia = 25.3, Tanzania = 31.7, Malawi = 19.8,
         Mozambique = 42.1, Kenya = 27.5)

nmr > 12
nmr > 30
nmr == min(nmr)

countries <- c("Ethiopia", "Tanzania", "Malawi", "Mozambique", "Kenya")
countries[nmr > 30]
countries[nmr <= 25]

# AND / OR
has_cpap <- c(TRUE, FALSE, TRUE, FALSE, TRUE)
high_risk <- (nmr > 30) & (!has_cpap)
names(nmr)[high_risk]

# %in% operator
east_africa <- c("Ethiopia", "Kenya", "Tanzania")
countries %in% east_africa
countries[countries %in% east_africa]


## ── Functions ────────────────────────────────────────────────

nmr_vec <- c(25.3, 31.7, 19.8, 42.1, 27.5)
mean(nmr_vec)
round(mean(nmr_vec), 1)
seq(0, 50, by = 10)
paste("NMR:", nmr_vec)

# Function anatomy
round(25.347, digits = 1)
round(25.347, digits = 0)
round(25.347)          # digits defaults to 0

# Custom function: NMR
calc_nmr <- function(neonatal_deaths, live_births) {
  nmr <- (neonatal_deaths / live_births) * 1000
  return(nmr)
}
calc_nmr(neonatal_deaths = 30, live_births = 1200)
calc_nmr(22, 1100)

# Custom function: MMR
calc_mmr <- function(maternal_deaths, live_births) {
  mmr <- (maternal_deaths / live_births) * 100000
  return(mmr)
}
calc_mmr(3, 1200)
calc_mmr(5, 950)

# Function with default argument
classify_nmr <- function(nmr, target = 12) {
  if (nmr <= target) {
    return("On Track")
  } else if (nmr <= target * 2) {
    return("Needs Improvement")
  } else {
    return("Critical")
  }
}
classify_nmr(10)
classify_nmr(20)
classify_nmr(42)
classify_nmr(20, target = 15)

# Vectorized custom function
neonatal_deaths <- c(30, 30, 22, 34, 29)
live_births     <- c(1200, 950, 1100, 800, 1050)
facility_nmr    <- calc_nmr(neonatal_deaths, live_births)
facility_nmr

facility_names <- c("Facility A", "Facility B", "Facility C",
                    "Facility D", "Facility E")
names(facility_nmr) <- facility_names
facility_nmr[facility_nmr > 30]

# Why functions beat copy-paste
calc_nmr <- function(deaths, births) (deaths / births) * 1000
nmr_a <- calc_nmr(30, 1200)
nmr_b <- calc_nmr(30, 950)
nmr_c <- calc_nmr(22, 1100)


## ── Getting Help ─────────────────────────────────────────────

?mean
?round
?factor
args(round)

deliveries <- c(112, 98, NA, 121, NA, 143)
mean(deliveries)                   # NA
mean(deliveries, na.rm = TRUE)     # 118.5
