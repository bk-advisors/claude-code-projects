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

## Completed Decks

| Deck | Topic | Context | Sequel |
|---|---|---|---|
| `anatomy-of-a-good-point/` | 4-part argumentation framework (Point, Reasoning, Evidence, Impact) | Malawi MNH | — |
| `causal-arguments/` | Causal reasoning: correlation vs. causation, three alternatives to rule out, causal stories, removal test | Ethiopia MNH (CHEWs, woredas, HSTP) | Sequel to anatomy-of-a-good-point; signposts to inference-and-intervention |
| `inference-and-intervention/` | 10-chapter course on causal models for business analysis, applied to MNH | Ethiopia MNH | Sequel to causal-arguments |

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

## Creating a New Deck

1. Create a new folder at the repo root (e.g., `new-framework/`)
2. Place the whiteboard photo or reference material in the folder
3. Copy `slide-master/BKA_Enhanced_Logo_Apr2025.png` as `bka-logo.png`
4. Copy an existing `custom.scss` as the starting theme
5. Create `index.qmd` using the same YAML front matter pattern as existing decks
6. Create lecture materials: `speaker-notes.md`, `intro-video-speaker-notes.md`, `generate_essay.py`, `generate_whiteboard_diagram.py`
7. Render with `quarto render new-framework/index.qmd`
8. Generate materials with `python generate_essay.py` and `python generate_whiteboard_diagram.py`
