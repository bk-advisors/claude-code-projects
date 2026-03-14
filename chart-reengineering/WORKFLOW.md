# Chart Reengineering — Workflow

Step-by-step process for adding a new chart to the series. Follow this sequence each time the user provides a URL to a chart they want to reverse-engineer.

---

## Phase 1: Research the Original Chart

1. **Fetch the source URL** — use `WebFetch` to extract the original R code, data source, and chart type
2. **Identify the key techniques** — which ggplot2 layers, scales, themes, and annotations does it use?
3. **Map to synthesized lessons** — for each technique, identify the relevant lesson (e.g., `geom_tile()` → Lesson 1.4 Geometries)
4. **Assess the data** — can we use MNH synthetic data, the original data, or do we need real-world data from APIs?

## Phase 2: Create the Lesson (.qmd)

### Structure (Minto Pyramid — every lesson follows this)

```
## About This Lesson     — Context, data source, techniques table
## The Answer             — Full polished chart (complete code, renders immediately)
## Key Insight            — 1-sentence blockquote takeaway
## Building Blocks        — Step-by-step construction (one concept per code chunk)
## Quick Reference        — Summary table of functions/arguments covered
## Your Turn              — Practice exercise (eval=FALSE, fill-in-the-blank)
```

### Naming Convention

```
lessons/NN-short-name.qmd
```

- `NN` = sequential number (01, 02, 03...)
- Use the same prefix when the chart type is a variant (e.g., 01/02/03 are all vaccination heatmaps)

### Required Elements in Every Lesson

- **YAML**: `title`, `subtitle`, `format: html`
- **Setup chunk**: `knitr::opts_chunk$set(warning = FALSE, message = FALSE, fig.width = ..., fig.height = ...)`
- **Theme source**: `source("../../synthesized-lessons/_common/theme_bka.R")`
- **Cross-reference comments**: `# See Lesson X.Y (Topic)` on every technique
- **BKA gradient** (when applicable): use `colorRampPalette()` with BKA palette anchors
- **Minto-style title**: insight-first, not descriptive (e.g., "X cut Y by Z%" not "Chart of X over time")

### BKA Palette Anchors

```r
# Sequential: light blue → dark blue → lime → amber → coral → red
c("#ACCBF9", "#005CB9", "#83BD00", "#F8A623", "#FA7650", "#E24A3F")

# Typography
bka_colors$title_dark    # "#242852" — titles, emphasis
bka_colors$subtitle_gray # "#606060" — subtitles, axis labels
bka_colors$header_green  # "#83BD00" — brand accent
```

## Phase 3: Variants (if applicable)

If the user requests variants of the same chart with different data:

1. **Original data version** — use the chart's original dataset for comparison
2. **Real-world data version** — research appropriate real-world data (WHO, World Bank, OWID)
   - Download via `curl` if R can't reach HTTPS APIs directly (known Windows issue)
   - Create a `data/prep_*.R` script to process raw JSON/CSV into clean data
   - Store raw downloads in `data/` (JSON/CSV), processed output as `data/*.csv`
   - Normalize per-capita when comparing across countries of different sizes
   - Use `oob = scales::squish` for extreme outliers in real data

## Phase 4: LinkedIn / Social Media Script

Create `linkedin/CHART-NAME-linkedin.R`:

1. Mirror the polished chart from "The Answer" section
2. Add `setwd()` logic so the script works from any directory
3. Save two PNGs via `ggsave()`:
   - **Portrait** (4:5 ratio): `width = 10, height = 12.5, dpi = 300` — best for image posts
   - **Landscape** (1.91:1 ratio): `width = 12, height = 6.28, dpi = 300` — best for link shares
4. Caption references BKA: `"Visualization: BK Advisors — bk-advisors.github.io"`

## Phase 5: Interactive Version (ggiraph)

Create `interactive/interactive-CHART-NAME.qmd`:

1. **Convert geoms**: `geom_*()` → `geom_*_interactive()` with `tooltip` and `data_id` aesthetics
2. **Tooltip content**: HTML-formatted, shows key data values on hover
3. **data_id**: use per-tile/per-point IDs (NOT per-group — per-group highlighting is distracting)
4. **Hover styling**: subtle border highlight via `opts_hover(css = "stroke:...")`, no fill override
5. **No `opts_hover_inv`**: don't fade other elements — it's distracting for dense charts
6. **Render with `girafe()`**: set `width_svg`, `height_svg`, tooltip CSS in BKA navy
7. **YAML**: `format: html` with `self-contained: true` and `page-layout: full`
8. **Self-contained data**: copy the CSV into `interactive/data/` so the folder is portable

### Tooltip CSS Template (BKA-branded)

```r
opts_tooltip(
  css = paste0(
    "background-color:#242852;color:white;",
    "padding:8px 12px;border-radius:4px;",
    "font-family:Lato,Arial,sans-serif;font-size:13px;",
    "line-height:1.4;box-shadow:2px 2px 6px rgba(0,0,0,0.3);"
  ),
  opacity = 0.95
)
```

## Phase 6: Folder Organization

After all files are created, the folder should look like this:

```
chart-reengineering/
├── chart-reengineering.Rproj
├── WORKFLOW.md                  # This file
├── data/                        # Shared data
│   ├── *.csv                    # Processed datasets
│   ├── prep_*.R                 # Data prep scripts
│   └── *.json                   # Raw API downloads (if any)
├── lessons/                     # Teaching .qmd files
│   ├── 01-*.qmd
│   ├── 02-*.qmd
│   └── ...
├── linkedin/                    # Social media outputs
│   ├── *-linkedin.R             # Scripts
│   ├── *.png                    # Generated PNGs
│   └── ...
└── interactive/                 # Interactive HTML versions
    ├── interactive-*.qmd
    ├── data/                    # Self-contained data copies
    └── *.html                   # Generated output
```

## Phase 7: Update CLAUDE.md

Add a row to the Chart Reengineering Series table in the root `CLAUDE.md` for each new file created.

---

## Known Gotchas

- **R can't reach HTTPS APIs on Windows** — download JSON via `curl` in bash, process with `Rscript`
- **Rscript inline code segfaults** — write code to a `.R` file and run `Rscript file.R` instead of `Rscript -e`
- **Pandoc not found from Rscript** — set `Sys.setenv(RSTUDIO_PANDOC = "C:/Users/Personal/AppData/Local/Programs/Quarto/bin/tools")`
- **Quarto render sets wd to file location** — relative paths in `.qmd` files are relative to the file, not the project root
- **Rscript does NOT set wd** — standalone `.R` scripts need explicit `setwd()` logic
- **Real-world data has extreme outliers** — always check the data range and use `oob = scales::squish` when needed
- **`coord_cartesian(clip = "off")`** — required when annotations sit above/outside the plot area
