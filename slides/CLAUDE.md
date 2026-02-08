# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo converts whiteboard sketches and frameworks from BK Advisors into polished Quarto reveal.js slide decks for students. Each subfolder is a self-contained presentation on a business/professional framework.

## Build Commands

```bash
# Render a single deck
quarto render <deck-folder>/index.qmd

# Live preview with hot reload
quarto preview <deck-folder>/index.qmd
```

Quarto 1.8+ is required. No package.json or npm dependencies exist — Quarto handles everything.

## Architecture

Each deck is a standalone folder containing:

- `index.qmd` — Quarto markdown source (revealjs format)
- `custom.scss` — Deck-specific theme extending the BK Advisors brand
- `bka-logo.png` — Copied from `slide-master/` for each deck
- `index.html` + `index_files/` — Rendered output (generated, do not edit)

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

## Creating a New Deck

1. Create a new folder at the repo root (e.g., `new-framework/`)
2. Place the whiteboard photo or reference material in the folder
3. Copy `slide-master/BKA_Enhanced_Logo_Apr2025.png` as `bka-logo.png`
4. Copy an existing `custom.scss` as the starting theme
5. Create `index.qmd` using the same YAML front matter pattern as existing decks
6. Render with `quarto render new-framework/index.qmd`
