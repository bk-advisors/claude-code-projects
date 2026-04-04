# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo converts whiteboard sketches and frameworks from BK Advisors into polished Quarto reveal.js slide decks for students. Each subfolder is a self-contained presentation on a business/professional framework. The audience is early-to-mid career professionals in global health consulting, working in maternal and newborn health.

**Voice/framing convention:** Do not assume students have worked in Ethiopia or any specific country. The lecturer (Matthew Kuch) shares his own experiences from Ethiopia and other countries. Use third-person or lecturer-as-narrator framing ("In Ethiopia, consultants face...", "Consider this scenario from Ethiopia...") rather than "in your work in Ethiopia." General second-person for the skill being taught is fine ("When you claim X causes Y...").

## Build Commands

```bash
# Render a single deck
quarto render <deck-folder>/index.qmd

# Live preview with hot reload
quarto preview <deck-folder>/index.qmd

# Generate lecture materials (per deck)
python <deck-folder>/generate_essay.py
python <deck-folder>/generate_whiteboard_diagram.py
python <deck-folder>/generate_youtube_metadata.py
python <deck-folder>/generate_youtube_thumbnails.py
```

Quarto 1.8+ is required. No package.json or npm dependencies exist — Quarto handles everything. Python scripts require `python-docx` and `matplotlib`.

## Architecture

Each deck is a standalone folder containing:

- `index.qmd` — Quarto markdown source (revealjs format)
- `custom.scss` — Deck-specific theme extending the BK Advisors brand
- `bka-logo.png` — Copied from `slide-master/` for each deck
- `index.html` + `index_files/` — Rendered output (generated, do not edit)

### Lecture Materials

Each standalone deck also includes supplementary lecture materials:

- `speaker-notes.md` — Slide-by-slide presenter script (conversational, second-person, with `*(pause)*` markers)
- `intro-video-speaker-notes.md` — YouTube intro video script (~5 minutes, hook story + framework walkthrough)
- `generate_essay.py` — Python script that generates `pre-class-essay.docx` using `python-docx` (Morgan Housel style: story-driven, counterintuitive)
- `generate_whiteboard_diagram.py` — Python script that generates `whiteboard-diagram.png` using matplotlib with `plt.xkcd()` for hand-drawn style
- `pre-class-essay.docx` — Generated output (regenerate with `python generate_essay.py`)
- `whiteboard-diagram.png` — Generated output (regenerate with `python generate_whiteboard_diagram.py`)
- `generate_youtube_metadata.py` — Python script that generates per-video YouTube upload metadata `.docx` files (title, description, tags, category, chapters, thumbnail suggestions)
- `youtube-metadata-*.docx` — Generated output (regenerate with `python generate_youtube_metadata.py`)
- `generate_youtube_thumbnails.py` — Python script that generates `youtube-thumb-*.png` YouTube thumbnail images using matplotlib (polished style, 1280x720, BKA branded)
- `youtube-thumb-*.png` — Generated output (regenerate with `python generate_youtube_thumbnails.py`)

## Completed Decks

| Deck | Topic | Context | Sequel |
|---|---|---|---|
| `anatomy-of-a-good-point/` | 4-part argumentation framework (Point, Reasoning, Evidence, Impact) | Malawi MNH | — |
| `causal-arguments/` | Causal reasoning: correlation vs. causation, three alternatives to rule out, causal stories, removal test | Ethiopia MNH (CHEWs, woredas, HSTP) | Sequel to anatomy-of-a-good-point; signposts to inference-and-intervention |
| `inference-and-intervention/` | 10-chapter course on causal models for business analysis, applied to MNH | Ethiopia MNH | Sequel to causal-arguments |
| `r-for-management-consultants/` | 9-chapter R programming course (tidyverse, ggplot2, Quarto reports) for consultants with no prior coding experience | MNH facility datasets (5 countries, 200 facilities) | Prerequisite for inference-and-intervention |
| `storytelling-with-data/` | Four-mode data storytelling framework (Diagnostic, Descriptive, Prescriptive, Predictive) with blog post, slides, and R tutorial | Africa measles heatmap, HPV-PNG scrollytelling | — |

### `storytelling-with-data/` Structure

This deck has three Quarto outputs (slides, blog post, R tutorial) and uses an organized subfolder layout:

- `generators/` — Python generator scripts (`generate_essay.py`, etc.). Run with `python storytelling-with-data/generators/generate_essay.py`
- `generated/` — All generator output (`.docx`, `.png`). Gitignored; regenerate by running the scripts
- `reference/` — Research notes (`Storytelling with data 2026.docx`) and editing guide (`ai-writing-tells.md`)
- Root contains: `index.qmd` (slides), `blog.qmd` (blog post), `tutorial.qmd` (R tutorial), `tutorial-analysis.R`, `speaker-notes.md`, SCSS themes, logo

## Shared Assets (`slide-master/`)

- `BKA_Enhanced_Logo_Apr2025.png` — Canonical BK Advisors logo
- `BKA Slides Template_vFinal.pptx` — PowerPoint style guide; the source of truth for brand colors, fonts, and visual style

## BK Advisors Brand (from PPTX template)

Colors extracted from the template's theme XML:

| Role | Hex |
|---|---|
| Primary Blue | `#005CB9` |
| Light Blue | `#00A1DF` |
| Green | `#83BD00` |
| Teal | `#3E9B6E` |
| Red | `#E24A3F` |
| Orange | `#FA7650` |
| Amber | `#F8A623` |
| Yellow | `#FED141` |

Fonts: **Calibri Light** (headings), **Calibri** (body).

These are defined as SCSS variables (`$bka-blue`, `$bka-light-blue`, etc.) in each deck's `custom.scss`.

## Quarto/Reveal.js Conventions

- Section divider slides use `{background-color="#005CB9"}` (the brand blue)
- Title slides use `data-background-color: "#005CB9"` in YAML front matter
- CSS grid layouts break inside reveal.js — use inline HTML `<table>` for diagram layouts instead
- The `filter: brightness(0) invert(1)` CSS trick for logo color inversion produces artifacts — avoid it; use white-background closing slides with the logo as-is
- Reusable CSS component classes are defined in `custom.scss`: `.callout-box`, `.example-block`, `.step-number`, `.key-takeaway`, `.columns-equal`, `.good-example`, `.bad-example`
- **Overflow fix:** All `custom.scss` files include `overflow-y: auto` on `.reveal .slides section` to prevent callout boxes and key-takeaway boxes from being clipped at the bottom of content-heavy slides. Component sizing (padding, margins, font-size) was tightened to minimize the need for scrolling.

## Multi-Chapter Website Courses

`inference-and-intervention/` and `r-for-management-consultants/` are Quarto **website** projects (not standalone decks). Each has:

- `_quarto.yml` — website project config with sidebar navigation
- `chapters/ch01.qmd` … `chapters/ch0N.qmd` — companion pages with learning objectives, key concepts, slide embed (iframe), R code workshop, and takeaways
- `ch01-xxx/index.qmd` … `ch0N-xxx/index.qmd` — reveal.js slide decks, one per chapter
- `styles.scss` — website SCSS (component classes: `.learning-objectives`, `.key-concept`, `.slide-embed`, `.key-takeaway`)
- Python generators in the project root: `generate_essays.py`, `generate_whiteboard_diagrams.py`, `generate_youtube_metadata.py`, `generate_youtube_thumbnails.py`

**Build commands for multi-chapter websites:**

```bash
# Render the full website (companion pages + all slide decks)
quarto render r-for-management-consultants/

# Live preview
quarto preview r-for-management-consultants/

# Generate supplementary materials
python r-for-management-consultants/generate_essays.py
python r-for-management-consultants/generate_whiteboard_diagrams.py
python r-for-management-consultants/generate_youtube_metadata.py
python r-for-management-consultants/generate_youtube_thumbnails.py
```

**Live demo scripts:** `r-for-management-consultants/demo-scripts/` contains one self-contained `.R` file per chapter (`ch01-why-r.R` through `ch09-quarto-reports.R`). Each script mirrors the slide section order and is designed for RStudio line-by-line execution during class delivery (Ctrl+Enter). Scripts build datasets inline — no external data files required. When adding new chapters or revising slide code examples, update the corresponding demo script to keep them in sync.

**Critical `_quarto.yml` render list rule:** Slide deck files (`ch*/index.qmd`) MUST be included in the `render:` list in `_quarto.yml`. Without this, Quarto copies the slide deck folders to `_site/` but omits `index_files/` (revealjs CSS and JS assets), causing slides to appear as plain HTML. When slide decks are in the render list, Quarto renders them as revealjs and consolidates assets into `_site/site_libs/revealjs/`.

**Inline R in companion pages:** Companion pages use `eval: false` (set at project level). Do NOT use backtick-r inline expressions (e.g., `` `r mean(x)` ``) in companion page narrative — they always evaluate regardless of `eval: false`. Show them as plain code spans or describe them in prose instead.

## Creating a New Deck

1. Create a new folder at the repo root (e.g., `new-framework/`)
2. Place the whiteboard photo or reference material in the folder
3. Copy `slide-master/BKA_Enhanced_Logo_Apr2025.png` as `bka-logo.png`
4. Copy an existing `custom.scss` as the starting theme
5. Create `index.qmd` using the same YAML front matter pattern as existing decks
6. Create lecture materials: `speaker-notes.md`, `intro-video-speaker-notes.md`, `generate_essay.py`, `generate_whiteboard_diagram.py`
7. Render with `quarto render new-framework/index.qmd`
8. Generate materials with `python generate_essay.py`, `python generate_whiteboard_diagram.py`, `python generate_youtube_metadata.py`, and `python generate_youtube_thumbnails.py`
