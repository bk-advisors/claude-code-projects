# Speaker Notes — R for Management Consultants

## Overview
This course teaches R programming from scratch to management consultants working in global health. It is a companion to the Inference and Intervention course, providing the R skills needed for that course's code workshops. All examples use maternal and newborn health data from facility-level programs across sub-Saharan Africa.

---

# Chapter 1: Why R for Management Consultants

## Slide: Learning Objectives

We're starting at the very beginning. By the end of this chapter, you'll understand why R is worth learning, you'll be able to navigate RStudio, and you'll have written your first lines of R code. No prior programming experience needed.

## Slide: The Spreadsheet Trap

Here's a scenario most of you will recognize. A consultant working on an MNH program across five countries receives monthly DHIS2 data extracts. Each country sends a different Excel format. Each month, a new file. Sixty files a year. The consultant spends more time copying, pasting, and reformatting than actually analyzing.

*(pause)*

This is the spreadsheet trap. It's not that Excel is bad — it's that Excel doesn't scale. When your analysis involves multiple files, repeated calculations, and results that need to be reproduced next quarter, you need something more.

## Slide: Excel vs. R: A Practical Comparison

Look at this comparison. Combining 60 monthly data files in Excel? Copy-paste, hope you don't miss a row. In R? Three lines of code. Recalculating when data updates? In Excel, redo everything. In R, re-run the script. Audit trail? Excel doesn't track who changed cell B47 last Tuesday. R scripts are version-controlled — every change is documented.

The point isn't that R replaces Excel entirely. It's that R replaces the parts of Excel that waste your time and introduce errors.

## Slide: When to Keep Using Excel

To be fair, Excel is still the right tool sometimes. Quick look at a small dataset. One-off calculations you'll never repeat. Sharing something where the recipient needs to edit values interactively. Don't throw away Excel. Just stop using it for the wrong tasks.

## Slide: R in One Sentence

R is a free, open-source programming language designed for statistical computing and data visualization. Free means no license fees, ever — unlike Stata or SAS. Open-source means 20,000 packages built by researchers and analysts around the world. And the community of global health R users is growing fast.

## Slide: Who Uses R in Global Health?

WHO uses R for disease surveillance. The Global Burden of Disease study runs on R. The DHS Program produces country-level reports using R. And increasingly, donors require reproducible analysis pipelines — which is exactly what R provides.

## Slide: The Four Panes of RStudio

RStudio is where you'll do all your work. Think of it as four windows. Top-left is your notebook — the Source Editor where you write and save R scripts. Bottom-left is your calculator — the Console where you test commands. Top-right is your workspace — the Environment showing your data and variables. Bottom-right is everything else — files, plots, help documentation.

*(pause)*

The mental model: write in the notebook, test in the calculator. Save your work in the notebook so you can re-run it tomorrow.

## Slide: Your First R Commands

Let's write some R. The simplest thing R can do is arithmetic. Two plus three. Ten times five point five. A hundred divided by seven. Nothing fancy — but notice R handles decimals without any special formatting.

Now let's store some values. Maternal deaths equals 45. Total deliveries equals 1,200. We can compute the maternal mortality ratio: maternal deaths divided by total deliveries, times 100,000. That's our first MNH indicator calculated in R.

## Slide: Naming Things Well

This slide matters more than you'd think. Good variable names are descriptive, lowercase, with underscores: neonatal_deaths, facility_count, anc_coverage_pct. Bad names are cryptic abbreviations or single letters. You'll read your code far more often than you write it. Name things so your future self can understand them.

## Slide: Console vs. Scripts

The console is scratch paper. It runs one command at a time, and results disappear when you close RStudio. A script is your permanent record. It saves every command, and you can re-run the entire analysis anytime. The transition from console to script is the transition from ad-hoc analysis to reproducible analysis.

## Slide: What Are Packages?

A package is someone else's code that extends what R can do. Think of it like apps on your phone. You install once with install.packages, then load each session with library. The tidyverse is a collection of packages that work together — it includes almost everything we'll use in this course.

## Slide: Key Takeaways

Three things to remember. One: R replaces the repetitive, error-prone parts of Excel with reproducible scripts. Two: RStudio has four panes — learn them. Three: the tidyverse is your core toolkit.

---

# Chapter 2: R Building Blocks

## Slide: Learning Objectives

This chapter teaches the fundamental building blocks. Vectors, data types, operators, functions, and how to get help. Once you have these, you can build anything.

## Slide: What Is a Vector?

Everything in R is a vector. Even a single number is a vector of length one. A vector is just an ordered collection of values of the same type. Use c() to combine multiple values.

Here we're creating a vector of neonatal mortality rates across five countries, and naming each element. Named vectors are useful because you can access values by name later.

## Slide: Vector Operations

This is one of R's superpowers. You don't need loops. When you multiply a vector by 2, R multiplies every element. When you calculate the mean, R takes the mean of all elements. This is called vectorization, and it makes R code both fast and readable.

## Slide: Indexing

Indexing means picking out specific values. By position: countries bracket 1 gives you the first country. By name: nmr bracket Malawi gives you Malawi's NMR. By condition: nmr bracket nmr greater than 30 gives you all countries with NMR above 30. That last one — conditional indexing — is incredibly powerful.

## Slide: The Four Core Types

R has four types you need to know. Numeric for numbers — NMR, delivery counts, coverage percentages. Character for text — country names, facility IDs. Logical for TRUE/FALSE — does this facility have CPAP? And factor for categories — facility type with ordered levels.

## Slide: Missing Values: NA

NA is R's way of saying "I don't know." And it's contagious — any calculation involving NA returns NA. That's by design. R forces you to make an explicit decision about missing values with na.rm = TRUE. In health data, missing and zero are fundamentally different. Missing means "not reported." Zero means "no one died." Never confuse them.

## Slide: Writing Your Own Functions

Functions are reusable calculations. Instead of writing the NMR formula every time, wrap it in a function: calc_nmr takes neonatal_deaths and live_births, returns the rate per 1,000. Now you have a standardized calculation your whole team can use.

## Slide: Getting Help

Professional R users look things up constantly. Question mark followed by a function name opens the help page. Double question mark searches all documentation. Stack Overflow has answered almost every R question imaginable. The skill isn't memorizing — it's knowing how to find the answer quickly.

---

# Chapter 3: Importing & Exploring Data

## Slide: Learning Objectives

This is where R gets practical. You'll learn to bring real data into R from CSV and Excel files, explore what you've got, and handle the inevitable missing values.

## Slide: The readr Package

read_csv from the readr package is the standard way to read CSV files. It automatically detects column types and gives you a tibble — which is just a modern data frame that prints nicely. If the automatic type detection gets it wrong, you can override with col_types.

## Slide: Reading Excel Files

Because donors and government offices love Excel. read_excel from the readxl package handles this. The key arguments to know are sheet (which sheet to read), skip (how many header rows to skip), and range (to read a specific cell range). DHIS2 exports often have merged cells and metadata rows, so inspect the file in Excel first.

## Slide: Data Frames and Tibbles

A data frame is R's spreadsheet — rows are observations, columns are variables. A tibble is the tidyverse's improved version. Same structure, but it prints more neatly and never silently converts your strings to factors. Use the dollar sign to access columns: facilities dollar sign nmr.

## Slide: The Exploration Toolkit

Every new dataset gets the same treatment. nrow and ncol for dimensions. head for the first few rows. glimpse for a compact summary of every column. summary for min, max, mean, median, and missing value counts. Run these before doing anything else.

*(pause)*

Think of it as a physical exam for your data. You wouldn't prescribe treatment without an exam. Don't analyze data without exploring it first.

## Slide: Handling Missing Values

colSums of is.na tells you how many NAs per column. colMeans of is.na times 100 gives you the percentage. These two commands should be your first check after importing any health dataset.

The table on this slide is important: all values missing for one facility means they didn't report — investigate. One column mostly missing means that indicator wasn't collected — note it. Random NAs scattered suggest data entry errors. And zeros that should be NA need recoding.

---

# Chapter 4: Data Transformation with dplyr

## Slide: Learning Objectives

This is the most important chapter in the course. Five dplyr verbs — filter, select, mutate, summarise, group_by — handle 90% of data transformation. Add the pipe operator, and you can build entire analysis workflows that read like English.

## Slide: The Pipe Operator

The pipe — that vertical bar followed by a greater-than sign — takes the result of one function and passes it to the next. It reads left to right, like a sentence: "Take this, then do that, then do that."

Without pipes, you get nested functions that read inside-out. With pipes, you get step-by-step workflows that anyone can follow.

## Slide: filter()

filter keeps only the rows that match your conditions. Facilities in Ethiopia. Facilities with NMR above 30. Facilities where CPAP is not available. Use comma for AND, vertical bar for OR, exclamation mark for NOT.

## Slide: select()

select keeps only the columns you need. Most DHIS2 exports have dozens of columns. You usually need five or six for a given analysis. select gets you there.

## Slide: mutate()

mutate creates new columns from existing ones. Convert coverage from a proportion to a percentage. Flag high-risk facilities. Classify NMR into categories with case_when. This is where you add the business logic to your data.

## Slide: group_by() + summarise()

This is the pivot table replacement. group_by splits your data by one or more variables. summarise calculates summary statistics within each group. Together, they produce the kind of country-by-country or facility-type-by-facility-type tables that consultants build every day.

*(pause)*

If you learn one thing from this chapter, learn this pattern. group_by, then summarise. It's the most powerful two-line combination in R.

## Slide: Putting It All Together

This final slide shows a complete pipeline: start with facility data, filter to active facilities, create NMR categories, group by country, summarise indicators, sort by worst-performing. That's a country dashboard in eight lines of code.

---

# Chapter 5: Reshaping & Joining Datasets

## Slide: Learning Objectives

Data rarely arrives in the shape you need. This chapter teaches you to reshape it and combine it.

## Slide: Wide vs. Long Format

Most DHIS2 exports and Excel files arrive in wide format — one column per month or per indicator. Most R analysis tools expect long format — one row per observation. pivot_longer converts from wide to long. pivot_wider converts from long to wide. Understanding when to use each is an essential skill.

## Slide: Joining Datasets

In MNH program analysis, your data lives in separate files: facility characteristics in one, monthly deliveries in another, country indicators in a third. left_join is the workhorse: it takes your main dataset and adds columns from a reference table, matching by a key column.

The key insight: left_join keeps all rows from your main dataset. If there's no match in the reference table, you get NAs. If you want only complete matches, use inner_join.

## Slide: String Basics

Facility names from DHIS2 are often inconsistent: "Hospital" vs "hospital", leading spaces, abbreviations. str_trim removes whitespace, str_to_title standardizes capitalization, str_replace fixes abbreviations. Clean strings early — inconsistent names break joins and grouping.

---

# Chapter 6: Data Visualization with ggplot2

## Slide: Learning Objectives

You've been transforming data. Now you'll see it. ggplot2 is the most widely used visualization library in R, and it produces charts that are ready for donor presentations.

## Slide: The Three Layers

Every ggplot2 chart has three layers. Data — what you're plotting. Aesthetics — what goes on the x-axis, the y-axis, what determines color. Geometry — what shape to draw. Once you internalize this pattern, you can build any chart.

## Slide: Bar Charts

geom_col for values you've already calculated. geom_bar for counting rows. Use reorder to sort bars by value. Horizontal bars are better when category labels are long.

## Slide: Scatter Plots

geom_point for exploring relationships between two numeric variables. Map a third variable to color to add another dimension. Add geom_smooth with method lm for a trend line. But remember — a trend line shows correlation, not causation.

## Slide: Line Charts

geom_line for time series. The group aesthetic tells ggplot2 which points to connect. Multiple lines with different colors show trends for multiple countries side by side.

## Slide: Choosing the Right Chart

This table is a reference you'll come back to. Comparing categories? Bar chart. Relationship between two variables? Scatter plot. Trend over time? Line chart. Distribution? Histogram. Comparing distributions? Box plot.

---

# Chapter 7: Publication-Quality Charts

## Slide: Learning Objectives

Chapter 6 taught you the chart types. This chapter teaches you to make them beautiful. Themes, colors, faceting, multi-panel layouts, and exporting.

## Slide: A Reusable BKA Theme

Define your theme once as a function, use it everywhere. This theme_bka function sets bold blue titles, removes vertical grid lines, positions the legend at the bottom, and uses a clean minimal base. Every chart in your report gets the same professional look.

## Slide: BK Advisors Color Palette

Consistent branding matters. Define the BKA colors as named variables. Create a named vector mapping countries to colors. Use scale_color_manual and scale_fill_manual to apply them. Your charts will match your slides, your reports, and your organization's brand.

## Slide: Faceting

Faceting is one of the most powerful visualization techniques. Instead of cramming everything into one chart, facet_wrap creates one small chart per group. The pattern — or lack thereof — becomes immediately obvious. Use it whenever you're comparing the same metric across countries or facility types.

## Slide: Patchwork

The patchwork package combines individual ggplot2 charts into multi-panel layouts. p1 plus p2 puts them side by side. p1 slash p2 stacks them vertically. Parentheses control grouping. This replaces the manual chart-grid arrangement you'd do in PowerPoint.

## Slide: ggsave

ggsave exports your chart to a file. Always use dpi = 300 for presentations and print. PNG for slides and email. PDF for formal reports. SVG for web. Specify width and height in inches for consistent sizing.

---

# Chapter 8: Descriptive Statistics for Consultants

## Slide: Learning Objectives

This chapter covers the statistics every consultant needs. Not theoretical statistics — practical statistics. The kind that goes into a quarterly report or a donor presentation.

## Slide: Mean vs. Median

NMR data across facilities is typically right-skewed — a few facilities with very high values pull the mean up. Always report both mean and median, and note when they diverge significantly. The median tells you what the "typical" facility looks like.

## Slide: Confidence Intervals

A 95% confidence interval quantifies uncertainty. It says: "We're fairly confident the true value falls in this range." For consultants, the practical takeaway is this: when two confidence intervals don't overlap, the difference between groups is likely real. When they overlap substantially, you can't be confident there's a real difference.

*(pause)*

The visualization on this slide — a dot plot with error bars — is one of the most useful charts for comparing countries. It shows both the point estimate and the uncertainty around it.

## Slide: Correlation

Correlation measures how strongly two variables move together. The coefficient r ranges from minus 1 to plus 1. But — and I can't stress this enough — correlation does not imply causation. Two variables can be correlated because a third variable drives both. That's confounding, and it's covered in depth in the Inference and Intervention course.

## Slide: Simple Linear Regression

lm fits a linear model. The output tells you: the slope (how much Y changes per unit of X), the significance (p-value), and the explanatory power (R-squared). For consultants, the key is to understand what these numbers mean, not to memorize the formulas.

A statistically significant result with a tiny coefficient is not practically important. And a regression coefficient is not a causal effect — it's an association that might be confounded.

## Slide: Statistics → Causation: The Bridge

Everything in this chapter describes associations. To move from association to causation, you need the tools from the Inference and Intervention course: causal diagrams, confounding analysis, and the do-operator. This chapter gives you the foundation; that course builds the structure.

---

# Chapter 9: Reproducible Reports with Quarto

## Slide: Learning Objectives

The final chapter closes the loop. You can import, transform, visualize, and analyze data. Now you need to communicate the results — in a way that updates automatically when data changes.

## Slide: The Reproducibility Problem

The old way: analyze in R, copy results into Word, format manually, data updates, start over. The Quarto way: write analysis and narrative in one file, click render, professional report ready. Data updates, re-render — everything updates.

*(pause)*

This is the single biggest time-saver in data analysis. Not the analysis itself — the communication. Reports that used to take days to update now take minutes.

## Slide: Document Structure

A Quarto document has three sections. YAML header between triple dashes — sets the title, author, and output format. Markdown text — your narrative, headings, bullet points. Code chunks in fenced blocks — your R analysis, which produces results inline.

## Slide: Inline R Code

This is where it gets magical. Instead of typing "The average NMR is 28.3," you type "The average NMR is" followed by an inline R expression. When the data changes, that number updates automatically. No more copy-paste errors. No more "did I update all the numbers?"

## Slide: Parameterized Reports

The crown jewel. Define a parameter in your YAML — say, country. Use that parameter throughout your analysis to filter the data. Then run a loop that renders one report per country. Five country briefs from one template. When data updates, re-run the loop. All five reports regenerate in seconds.

## Slide: Course Wrap-Up

That's the complete workflow. Import data from CSV and Excel. Transform it with dplyr. Visualize it with ggplot2. Analyze it with descriptive statistics. Communicate findings in reproducible Quarto reports.

You now have everything you need for the Inference and Intervention course, where these R skills become the foundation for causal analysis, Bayesian networks, and data-driven resource allocation.
