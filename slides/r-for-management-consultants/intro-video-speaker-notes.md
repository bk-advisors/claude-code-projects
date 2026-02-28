# Speaker Notes — Intro Video: R for Management Consultants

## Opening Hook (30 seconds)

The Spreadsheet That Fell Apart
Why learning R might be the most valuable week of your career

Let me tell you about a consultant I know who nearly lost a major funding decision because of a spreadsheet.

She was preparing a quarterly report for a multi-country MNH initiative in sub-Saharan Africa. Five countries, sixty facilities, twelve months of delivery data. She'd built the entire analysis in Excel — pivot tables, VLOOKUP formulas, conditional formatting. It was a masterpiece of spreadsheet engineering. Then the data team sent a correction: two facilities had been double-counted.

Fixing it meant retracing every formula, every linked cell, every pivot table across fourteen tabs. She spent three days rebuilding what should have taken thirty minutes. And when a colleague asked to reproduce her analysis, she couldn't explain half the formulas she'd written three months earlier.

That's the moment she learned R. Not because she wanted to become a programmer — she didn't. Because she wanted to stop doing the same work twice.

*(pause)*

## A Little About Me (30 seconds)

My name is Matthew Kuch. I've spent the last decade in global health — at CHAI, at Gavi, at Deloitte managing grants for USAID and DFID. I've watched brilliant analysts waste days on tasks that should take minutes. I've seen reports delayed because "the Excel broke." And I've seen teams transform their work by switching to R — not because R is trendy, but because it solves a real problem: making your analysis reproducible, auditable, and fast.

This course is the introduction I wish someone had given me.

*(pause)*

## What This Course Is About (1 minute)

Welcome to R for Management Consultants.

This is a practical, hands-on course that teaches you R programming from scratch. No prior programming experience is needed. If you can use Excel, you can learn R.

We're not going to turn you into a data scientist. We're going to give you a toolkit that does three things Excel cannot: handle large datasets without breaking, reproduce your entire analysis with one click, and produce publication-quality charts that are ready for donor presentations.

Every example in this course uses real-world maternal and newborn health data. You'll work with facility-level delivery data, neonatal mortality rates, equipment inventories, and training records — the same kinds of data you encounter in your day-to-day work.

*(pause)*

## The Journey in Four Parts (2.5 minutes)

*(Reference the whiteboard diagram here — the R workflow from import to communicate)*

The course is organized into four parts, nine chapters total. Let me walk you through what you'll learn.

**Part I: Getting Started** covers the basics. Chapter 1 explains why R matters for consultants — when to use it, when Excel is still fine, and how to set up your workspace. Chapter 2 teaches the building blocks: vectors, data types, functions. Think of it as learning the grammar before writing sentences.

**Part II: Working with Data** is where things get practical. Chapter 3 teaches you to import CSV and Excel files — the kind of DHIS2 exports and donor spreadsheets you deal with daily. Chapter 4 is the core: data transformation with dplyr. Filtering, grouping, summarizing — everything you do with pivot tables, but reproducible and readable. Chapter 5 covers reshaping and joining, which is how you combine data from multiple sources into one analysis-ready dataset.

**Part III: Visualization and Analysis** is where your work becomes visible. Chapters 6 and 7 teach ggplot2 — the visualization library that produces charts worthy of a donor presentation. You'll go from basic bar charts to polished, branded dashboards in two chapters. Chapter 8 covers the descriptive statistics every consultant needs: means, confidence intervals, correlation, and simple regression.

**Part IV: Communication** closes the loop. Chapter 9 teaches Quarto — the tool that combines your R code, charts, and narrative text into a single document. Change the data, click render, and your entire report updates. You can even generate country-specific briefs from a single template.

*(pause)*

## Who This Is For (30 seconds)

This course is for management consultants, program analysts, and technical advisors in global health who work with data regularly but have never written a line of code.

If you spend hours in Excel every week copying data between files, reformatting charts for different audiences, or trying to remember how you calculated a number three months ago — this course will change how you work.

You don't need a math background. You don't need to be "technical." You need to be willing to type instead of click.

## What You'll Walk Away With (30 seconds)

By the end of this course, you'll be able to:

- Import and clean facility-level data from any CSV or Excel source
- Transform raw data into summary tables and indicator dashboards
- Create publication-quality charts with consistent branding
- Calculate and interpret basic statistics with confidence intervals
- Produce reproducible reports that update automatically when data changes
- And most importantly: you'll be ready for the Inference and Intervention course, where these R skills become the foundation for causal analysis

## Closing (15 seconds)

The best analysts in global health aren't the ones with the most data. They're the ones whose work can be trusted, reproduced, and updated. R gives you that.

Let's get started.
