// Cervical Cancer Mortality Rates in Asia-Pacific (2022)
// Age-standardized mortality rate per 100,000 women
// Source: Ueda (2024), Journal of Obstetrics and Gynaecology Research
export const mortalityRates = [
  { country: "Fiji", rate: 22.5, region: "Pacific", highlight: false },
  { country: "Papua New Guinea", rate: 19.9, region: "Pacific", highlight: true },
  { country: "Solomon Islands", rate: 17.9, region: "Pacific", highlight: false },
  { country: "Vanuatu", rate: 13.6, region: "Pacific", highlight: false },
  { country: "Myanmar", rate: 13.4, region: "Asia", highlight: false },
  { country: "Indonesia", rate: 13.2, region: "Asia", highlight: false },
  { country: "Maldives", rate: 12.9, region: "Asia", highlight: false },
  { country: "Guam", rate: 11.2, region: "Pacific", highlight: false },
  { country: "India", rate: 11.2, region: "Asia", highlight: false },
  { country: "Mongolia", rate: 9.6, region: "Asia", highlight: false },
  { country: "Australia", rate: 1.7, region: "Pacific", highlight: false }
];

// Global cervical cancer deaths by region (2022)
// Source: Global Cancer Observatory (GCO, 2022)
export const globalDeaths = {
  total: 348709,
  asiaPacific: 197217,
  asiaPacificPercent: 56.6,
  otherRegions: 151492,
  otherRegionsPercent: 43.4
};

// PNG-specific statistics
// Source: Globocan PNG Factsheet, 2022
export const pngStats = {
  newCasesPerYear: 1053,
  mortalityRate: 19.9,
  globalRank: 12,
  regionalRank: 2,
  cancerRankInWomen: 2
};

// Projected lives saved from HPV vaccination (2026-2070)
// Based on Gavi estimate of 17.4 deaths averted per 1,000 vaccinated
// Assumptions:
// - 2026: 200,000 girls vaccinated (9-14 year olds), 80% coverage target
// - 2027-2070: 80,000 9-year-olds vaccinated annually (1.8% annual growth), 90% coverage target
export const projectedLivesSaved = [
  { year: 2026, cumulativeLivesSaved: 3480, girlsVaccinated: 200000 },
  { year: 2027, cumulativeLivesSaved: 4872, girlsVaccinated: 280000 },
  { year: 2028, cumulativeLivesSaved: 6293, girlsVaccinated: 361440 },
  { year: 2029, cumulativeLivesSaved: 7743, girlsVaccinated: 444347 },
  { year: 2030, cumulativeLivesSaved: 9223, girlsVaccinated: 528747 },
  { year: 2035, cumulativeLivesSaved: 17385, girlsVaccinated: 998975 },
  { year: 2040, cumulativeLivesSaved: 27123, girlsVaccinated: 1558641 },
  { year: 2045, cumulativeLivesSaved: 38592, girlsVaccinated: 2218168 },
  { year: 2050, cumulativeLivesSaved: 52003, girlsVaccinated: 2989041 },
  { year: 2055, cumulativeLivesSaved: 67618, girlsVaccinated: 3885257 },
  { year: 2060, cumulativeLivesSaved: 75893, girlsVaccinated: 4362582 },
  { year: 2065, cumulativeLivesSaved: 85234, girlsVaccinated: 4898509 },
  { year: 2070, cumulativeLivesSaved: 96905, girlsVaccinated: 5569161 }
];

// Deaths without intervention projection
// Source: UNFPA and IARC analyses
export const deathsWithoutAction = {
  by2070: 60232,
  by2120: 148000
};

// Vaccination impact statistics
// Source: Gavi HPV Impact Report, 2022
export const vaccinationImpact = {
  deathsAvertedPer1000: 17.4,
  targetAgeGroup: "9-14 year old girls",
  totalLivesSavedBy2070: 96905,
  totalGirlsVaccinatedBy2070: 5569161
};

// Economic analysis
// Source: UNFPA PNG-specific modelling
export const economicData = {
  investmentFirst10Years: 21000000, // USD 20-21 million
  returnPer1Dollar30Years: 19,
  returnPer1Dollar50Years: 61.32,
  livesSavedBy2120WithStrategy: 148000,
  livesSavedBy2120VaccineOnly: 100000
};

// Comparison with Australia (for context)
export const comparisonData = {
  png: {
    country: "Papua New Guinea",
    incidenceRate: 34.9, // per 100,000
    mortalityRate: 19.9,
    screeningProgram: false,
    hpvVaccineNational: false
  },
  australia: {
    country: "Australia",
    incidenceRate: 6.4, // per 100,000
    mortalityRate: 1.7,
    screeningProgram: true,
    hpvVaccineNational: true
  }
};

// Regional comparison - incidence vs mortality
export const regionalComparison = [
  { country: "Papua New Guinea", incidence: 34.9, mortality: 19.9, highlight: true },
  { country: "Fiji", incidence: 35.2, mortality: 22.5, highlight: false },
  { country: "Solomon Islands", incidence: 29.7, mortality: 17.9, highlight: false },
  { country: "Indonesia", incidence: 23.4, mortality: 13.2, highlight: false },
  { country: "India", incidence: 18.7, mortality: 11.2, highlight: false },
  { country: "Australia", incidence: 6.4, mortality: 1.7, highlight: false }
];

// Key messages for the story
export const keyMessages = [
  {
    id: "global-burden",
    stat: "348,709",
    description: "women died from cervical cancer globally in 2022"
  },
  {
    id: "asia-pacific",
    stat: "56.6%",
    description: "of these deaths occurred in the Asia-Pacific region"
  },
  {
    id: "png-rank",
    stat: "12th",
    description: "PNG ranks 12th globally for cervical cancer mortality"
  },
  {
    id: "lives-at-stake",
    stat: "60,232",
    description: "women in PNG could die from cervical cancer by 2070 without action"
  },
  {
    id: "lives-saved",
    stat: "96,905",
    description: "lives could be saved through HPV vaccination by 2070"
  },
  {
    id: "roi",
    stat: "$19",
    description: "return for every $1 invested over 30 years"
  }
];
