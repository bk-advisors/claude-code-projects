# Skills: Inference and Intervention

This file documents the patterns, conventions, and decisions made while building and revising the 10-chapter Quarto reveal.js lecture series and the companion course website, based on *Inference and Intervention: Causal Models for Business Analysis* (Ryall & Bramson, 2014), adapted for a Maternal & Newborn Health (MNH) audience.

---

## 1. Project Overview

- **Source material:** The textbook uses business examples (advertising, market share, ridesharing companies). Every chapter's examples have been adapted to MNH/public health contexts.
- **Audience:** Future program managers in MNH and Public Health programs in developing countries.
- **Privacy requirement:** All identifying details from the real organization behind the examples have been removed. See Section 7 (Anonymization) below.
- **10 chapters**, each a standalone deck in its own folder under `inference-and-intervention/`.
- **Course website** — a Quarto multi-page website tying all 10 chapters together with navigation, companion pages, and supplementary resources.

---

## 2. Folder Structure

```
inference-and-intervention/
  _quarto.yml               # Website project configuration
  index.qmd                 # Website home/landing page
  schedule.qmd              # Course schedule/syllabus
  r-setup.qmd               # R environment setup guide
  references.qmd            # Bibliography and references
  styles.scss               # Website-specific SCSS theme
  chapters/                 # Chapter companion pages (website)
    ch01.qmd                #   Ch 1 companion page
    ch02.qmd                #   Ch 2 companion page
    ...                     #   (ch03–ch09)
    ch10.qmd                #   Ch 10 companion page
  ch01-intro/               # Ch 1 slide deck (standalone)
  ch02-qualitative-models/  # Ch 2 slide deck (standalone)
  ch03-interview-case/      # Ch 3 slide deck (standalone)
  ch04-quantitative-models/ # Ch 4 slide deck (standalone)
  ch05-situational-analysis/# Ch 5 slide deck (standalone)
  ch06-business-financials/ # Ch 6 slide deck (standalone)
  ch07-single-agent/        # Ch 7 slide deck (standalone)
  ch08-resource-allocation/ # Ch 8 slide deck (standalone)
  ch09-multi-agent/         # Ch 9 slide deck (standalone)
  ch10-data-driven/         # Ch 10 slide deck (standalone)
  context/                  # Reference PDFs (do not modify)
  skills.md                 # This file
  _site/                    # Rendered website output (generated)
```

Each **chapter slide folder** (e.g., `ch01-intro/`) contains:
- `index.qmd` — Slide source (revealjs format)
- `custom.scss` — Identical SCSS theme (same file across all 10)
- `bka-logo.png` — Logo (copied from `slide-master/`)
- `index.html` + `index_files/` — Rendered slide output (generated)

Each **chapter companion page** (e.g., `chapters/ch01.qmd`) contains:
- Learning objectives, key concepts, embedded slide iframe, R code workshop, key takeaways, looking ahead

---

## 3. YAML Front Matter Template

All 10 decks use this exact YAML header:

```yaml
---
title: "Chapter N: Title Here"
subtitle: "Inference and Intervention | BK Advisors"
author: "BK Advisors"
date: today
format:
  revealjs:
    theme: [default, custom.scss]
    logo: bka-logo.png
    slide-number: true
    transition: fade
    background-transition: slide
    title-slide-attributes:
      data-background-color: "#005CB9"
    hash-type: number
    center: false
    width: 1280
    height: 720
execute:
  echo: true
  eval: false
  warning: false
---
```

Key settings:
- `eval: false` — R code is displayed but not executed (no R dependencies needed to render)
- `echo: true` — Code blocks are shown on slides
- `width: 1280`, `height: 720` — 16:9 aspect ratio
- Title slide gets the brand blue background automatically

---

## 4. Slide Structure Pattern

Every deck follows this section order:

| Section | Slides | Notes |
|---|---|---|
| Title (auto-generated) | 1 | Blue background from YAML |
| Learning Objectives | 1 | `::: {.incremental}` bullet list |
| Chapter Overview | 1-2 | Key concepts map, connection to prior chapters |
| **Theory Sections** | 12-20 | Core book content with definitions, diagrams, formulas |
| Section Divider: MNH Application | 1 | `{background-color="#005CB9"}` with subtitle span |
| **MNH Application** | 5-10 | Real-world examples using MNH context |
| Section Divider: R Workshop | 1 | `{background-color="#005CB9"}` |
| **R Code Workshop** | 4-8 | Working R code blocks using bnlearn, dagitty, etc. |
| Key Takeaways | 1 | `.key-takeaway` box |
| Looking Ahead | 1 | `.callout-box` previewing next chapter |
| Closing Slide | 1 | White background, centered logo, chapter title |

### Section Dividers

```markdown
# Section Title {background-color="#005CB9"}

<span style="color: rgba(255,255,255,0.7); font-size: 0.7em;">Subtitle text here</span>
```

### Closing Slide

```markdown
##  {background-color="white"}

<br><br><br>

::: {style="text-align: center;"}
![](bka-logo.png){width="250px"}

<br>

[Inference and Intervention | Chapter N: Title]{style="color: #005CB9; font-size: 0.6em;"}

[BK Advisors]{style="color: #666; font-size: 0.5em;"}
:::
```

### Progressive Reveal

Use `. . .` (three dots with spaces) for fragment reveals within a slide. Use `::: {.incremental}` for bullet-by-bullet reveal.

---

## 5. CSS Component Classes

All defined in `custom.scss`. Use these consistently:

| Class | Purpose | Color Variants |
|---|---|---|
| `.callout-box` | Highlighted info/insight box | `.green`, `.orange`, `.red` |
| `.definition-box` | Formal definitions (teal/green gradient) | — |
| `.example-block` | Worked example with label | — |
| `.key-takeaway` | Full-width blue summary box | — |
| `.columns-equal` > `.col` | Two-column layout | — |
| `.step-flow` > `.step-item` + `.step-arrow` | Horizontal process flow | — |
| `.dag-node` | DAG diagram nodes (inline HTML) | `.outcome`, `.treatment`, `.confounder`, `.decision`, `.rect`, `.hexagon` |
| `.dag-arrow` | Arrow between DAG nodes | `.positive`, `.negative` |
| `.math-block` | Centered math equation container | — |
| `.step-number` | Circular numbered badge | `.green`, `.teal`, `.orange`, `.red`, `.amber` |
| `.bad-example` / `.good-example` | Cross/check prefixed text | — |

### Example Usage

```markdown
::: {.callout-box .green}
**Key insight:** Text here.
:::

::: {.definition-box}
**Term:** Formal definition here.
:::

::: {.example-block}
[MNH Example]{.example-label}
Content here.
:::
```

---

## 6. DAG Diagrams

CSS grid layouts break in reveal.js. Always use **inline HTML `<table>`** for DAG and diagram layouts:

```html
<table style="width: 95%; margin: 0.4em auto; font-size: 0.45em;">
<tr>
<td style="text-align: center; padding: 0.5em;">
<div class="dag-node decision rect" style="padding: 0.4em 0.6em;">Node<br>Label</div>
</td>
<td style="text-align: center;">
<span class="dag-arrow">→</span>
</td>
<td style="text-align: center; padding: 0.5em;">
<div class="dag-node" style="padding: 0.4em 0.6em;">Another<br>Node</div>
</td>
</tr>
</table>
```

Node type conventions:
- **Decision nodes:** `.dag-node.decision.rect` (rectangle, orange border)
- **Chance/probabilistic nodes:** `.dag-node` (circle, blue border)
- **Outcome/objective nodes:** `.dag-node.hexagon` (hexagon shape, teal/green)
- **Confounders:** `.dag-node.confounder` (amber border)
- **Treatment/intervention:** `.dag-node.treatment` (green border)

---

## 7. Anonymization Rules (CRITICAL)

The MNH examples are based on a real organization. All identifying details have been removed. **Never reintroduce any of the following:**

### Banned Terms (must never appear in any `.qmd` file)

| Category | Banned Terms | Generic Replacement |
|---|---|---|
| Organization names | Beginnings Fund, Meridian Health Alliance, the Alliance | "the program", "the MNH program", "the donor program", "MNH programs" |
| Budget amounts | $525M, $525 million | "pooled funding", "the program's total budget", "a substantial investment" |
| Life-saving targets | 322,000, 322,847 | "hundreds of thousands of lives", "over the program period" |
| Donor names | CIFF, Delta Philanthropies, ELMA, Gates Foundation, Mohamed bin Zayed | Remove entirely or say "multiple global health foundations" |
| Governance | Investment Committee | "program leadership", "the leadership team" |
| Country names | Ethiopia, Tanzania, Kenya, Uganda, Ghana, Malawi, Zimbabwe, Rwanda, Lesotho, Nigeria | Country A through Country J |
| Phase names | Phase 1, Phase 2 (with specific dates) | "Cohort 1", "Cohort 2", "subsequent cycles", "subsequent funding cycle" |
| Timeline | 76 months | "the program timeline" |
| Partner orgs | HaHCo, Fund Two | "The Rideshare Case" (for the textbook case), remove Fund Two |
| Specific dollar amounts tied to the program | $50M, $15M, $8M, $3M, $20M (program budgets) | Use percentages, "a budget tranche", relative terms |

### Country Anonymization Mapping

Used in ch06 and ch08 (the only chapters with country-level data):

| Original | Anonymous |
|---|---|
| Ethiopia | Country A |
| Tanzania | Country B |
| Kenya | Country C |
| Uganda | Country D |
| Ghana | Country E |
| Malawi | Country F |
| Zimbabwe | Country G |
| Rwanda | Country H |
| Lesotho | Country I |
| Nigeria | Country J |

### What IS Allowed

- MNH-specific clinical terms: NMR, MMR, CPAP, PPH, preterm birth, birth asphyxia, nurse-midwife, DHIS2
- Theory of Change structure: People / Products / Systems pathway to impact
- Generic program descriptions: "large-scale MNH initiative", "multi-country philanthropic program"
- Pedagogical dollar amounts in teaching examples: cost-per-life-saved figures ($1,050, $14,706), generic pilot costs ($2M)
- The book's original business examples: Slimtree Publishing, Hubris Health, The Rideshare Case — these are from the textbook and not identifying

### Verification Command

Run this grep to verify no identifying terms remain:

```bash
rg -i "Meridian|Alliance|Beginnings|Investment Committee|CIFF|Delta Philanthrop|ELMA|Gates Foundation|Mohamed|HaHCo|Fund Two|76 months|\$525|322,000|322,847|Ethiopia|Tanzania|Kenya|Uganda|Ghana|Malawi|Zimbabwe|Rwanda|Lesotho|Nigeria|Phase [12]" inference-and-intervention/**/*.qmd
```

This should return zero matches.

---

## 8. R Code Conventions

### Packages Used Across Chapters

| Package | Purpose | Chapters |
|---|---|---|
| `dagitty` | Define and analyze DAGs, d-separation, adjustment sets | Ch1-5, Ch10 |
| `ggdag` | Visualize DAGs using ggplot2 | Ch1-3, Ch10 |
| `bnlearn` | Bayesian network structure and parameter learning | Ch4-5, Ch7, Ch10 |
| `ggplot2` | All data visualizations | Ch4-10 |
| `ivreg` | Instrumental variable regression (2SLS) | Ch10 |
| `tidyr` | Data reshaping (pivot_longer) | Ch8 |

### Code Block Labels

Every R code block has a descriptive `#| label:` tag:

```r
```{r}
#| label: descriptive-name
#| echo: true
#| fig-width: 10
#| fig-height: 6
```
```

### Consistent MNH Variables

These variable names are used across chapters for consistency:

| Variable | Values | R Variable Name |
|---|---|---|
| Staffing | Adequate / Low | `Staffing` |
| Equipment (CPAP) | Available / Unavailable | `Equipment` or `CPAP` |
| Training | Completed / Not Completed | `Training` |
| Quality of Care | Good / Poor | `Quality` |
| NMR | High (>25/1000) / Low (≤25/1000) | `NMR` |
| MMR | High (>300/100K) / Low (≤300/100K) | `MMR` |
| Coverage | >80% / ≤80% | `Coverage` |

---

## 9. Business-to-Public-Health Terminology

The textbook uses business language. We systematically replaced:

| Business Term (Book) | Public Health Replacement |
|---|---|
| Advertising | Mass media campaign / demand generation |
| Firm / Company | Program / MNH initiative |
| Client | Beneficiary / target population |
| ROI | Cost-effectiveness / lives saved per dollar |
| Revenue | Lives saved / mortality reduction |
| Profit | Impact / net health benefit |
| Market share | Coverage rate |
| Consultant | Technical advisor |
| CEO / Board | Program Director / Leadership |
| Shareholders | Stakeholders / beneficiaries |
| Product launch | Intervention rollout |
| Sales | Service delivery / uptake |

The book's *original* examples (Slimtree Publishing, Hubris Health, The Rideshare Case) are kept as-is in "Book Context" sections, then explicitly mapped to MNH equivalents.

---

## 10. Cross-Chapter References

Chapters reference each other frequently. The linking pattern:

- Forward reference: "We will formalize this in **Chapter 7** when we discuss decision analysis."
- Back reference: "Using the d-separation criteria from **Chapter 2**..."
- "Looking Ahead" slide at the end of each chapter previews the next chapter with 3-4 bullet points.

Chapter dependency chain:
```
Ch1 (intro) → Ch2 (qualitative DAGs) → Ch3 (case study applying Ch2)
                                      → Ch4 (quantitative / CPTs / Bayes)
                                        → Ch5 (inference / belief updating)
                                          → Ch6 (Simpson's Paradox case)
                                            → Ch7 (decisions / do-calculus)
                                              → Ch8 (resource allocation case)
                                                → Ch9 (game theory)
                                                  → Ch10 (structure learning)
```

---

## 11. Revision Workflow

When revising content across all 10 decks (e.g., anonymization, terminology changes):

### Strategy

1. **Grep first** to find all occurrences across all files
2. **Triage by volume**: Files with many hits (ch06: 30, ch08: 94) get dedicated subagents; files with few hits get direct edits
3. **Edit in parallel** when edits are independent across files
4. **Use `replace_all`** for simple global substitutions within a file
5. **Watch for article doubling**: replacing "Meridian Health Alliance" with "the donor program" can create "The the donor program" when preceded by "The". Always check and fix.
6. **Final verification grep** after all edits — search for ALL banned terms in one pass

### Common Pitfalls

- **Sibling tool call cascade**: If one edit in a parallel batch fails, all subsequent edits in that batch fail. Retry the failed edits in a follow-up call.
- **Context sensitivity**: "the program" vs. "the MNH program" vs. "the donor program" — choose based on whether the sentence is about the implementing organization, the health initiative broadly, or the funding entity specifically.
- **R code consistency**: When renaming concepts in prose, also update R variable names, plot titles, data frame column values, and code comments to match.
- **Tables with country data**: After anonymizing country names, verify the numbers don't exactly match any public source. Shift values slightly if needed.

---

## 12. Course Website

### Architecture

The course website is a Quarto `type: website` project rooted at `inference-and-intervention/`. The `_quarto.yml` file configures the project with:

- **`render:` list** — explicitly includes only website `.qmd` files; the `ch*/index.qmd` slide decks are excluded from the website build and remain standalone
- **Top navbar** — Home, Schedule, R Setup, References
- **Sidebar** — chapters grouped into 4 parts: Foundations (Ch1–3), Quantitative Analysis (Ch4–6), Decision & Strategy (Ch7–9), Data-Driven Methods (Ch10)
- **Theme** — `cosmo` base + `styles.scss` overlay with BK Advisors brand colors
- **`eval: false`** globally — R code displayed but not executed (matches slide decks)

### Website Pages

| Page | File | Content |
|---|---|---|
| Home | `index.qmd` | Course overview, chapter table, MNH analyst workflow, prerequisites |
| Schedule | `schedule.qmd` | 10-session syllabus, part groupings, dependency chain |
| R Setup | `r-setup.qmd` | Software requirements, package installation, verification script, troubleshooting |
| References | `references.qmd` | Textbook, causal inference literature, R package citations, MNH references |
| Chapter 1–10 | `chapters/ch01.qmd`–`ch10.qmd` | Learning objectives, key concepts, embedded slides, R code workshop, takeaways |

### Chapter Companion Page Template

Every chapter companion page follows this structure:

```markdown
---
title: "Chapter N: Title"
subtitle: "One-line description"
---

## Learning Objectives
::: {.learning-objectives}
- Bullet points (no ::: {.incremental} — that's slides-only)
:::

## Key Concepts
::: {.key-concept}
#### Concept Name
Prose explanation.
:::
(3–5 concept blocks with color variants: .green, .teal, .orange, .red)

## Lecture Slides
::: {.slide-embed}
<iframe src="../chXX-folder/index.html"></iframe>
<div class="slide-embed-footer">
<a href="../chXX-folder/index.html" target="_blank">Open slides full-screen &rarr;</a>
</div>
:::

## R Code Workshop
(R code blocks from slides with explanatory prose between them)

## Key Takeaways
::: {.key-takeaway}
Summary content.
:::

## Looking Ahead
Preview of next chapter (or "Course Summary" for Ch 10).
```

### Website CSS Component Classes

Defined in `styles.scss` (website-specific, separate from slide `custom.scss`):

| Class | Purpose | Variants |
|---|---|---|
| `.learning-objectives` | Teal-bordered box for learning objectives | — |
| `.key-concept` | White card with colored left border | `.green`, `.teal`, `.orange`, `.red` |
| `.slide-embed` | Iframe container with border, shadow, footer link | — |
| `.key-takeaway` | Blue background summary box (white text) | — |
| `.callout-box` | Info/insight box (same as slides, adapted for web) | `.green`, `.orange`, `.red` |
| `.definition-box` | Teal-bordered definition box | — |
| `.chapter-grid` / `.chapter-card` | Card grid layout for home page | — |
| `.r-code-section` | Light background container for R code areas | — |
| `.step-number` | Circular numbered badge | `.green`, `.teal`, `.orange`, `.red` |

### Relationship Between Slides and Website

- **Slide decks are standalone.** Each `ch*/index.qmd` renders independently as a reveal.js deck with its own `custom.scss`. The website build does NOT touch them.
- **Website companion pages embed slides.** Each `chapters/chXX.qmd` uses an `<iframe>` pointing to `../chXX-folder/index.html` to display the pre-rendered slides.
- **Content is extracted, not duplicated.** Companion pages extract learning objectives, key concepts, R code, and takeaways from the slide sources, adapted from slide-format fragments to full web prose (removing `. . .`, `::: {.incremental}`, `{background-color=...}`, and inline HTML table diagrams).
- **Render independently.** `quarto render ch01-intro/index.qmd` renders a slide deck; `quarto render` (from the project root) renders the website. Neither affects the other.

---

## 13. Rendering and Testing

### Slide Decks (standalone)

```bash
# Render a single chapter's slide deck
quarto render inference-and-intervention/ch01-intro/index.qmd

# Live preview a slide deck
quarto preview inference-and-intervention/ch01-intro/index.qmd
```

### Course Website

```bash
# Render the full website (from the project root)
quarto render inference-and-intervention/

# Live preview the website
quarto preview inference-and-intervention/

# Output goes to inference-and-intervention/_site/
```

### Checks

**Slide decks:**
- Slide transitions and fragment reveals (`. . .`)
- SCSS styling applied correctly (callout boxes, DAG nodes, tables)
- Section divider backgrounds (should be brand blue)
- Code blocks render with syntax highlighting
- Closing slide has centered logo on white background

**Course website:**
- All 14 pages render without errors (4 top-level + 10 chapters)
- Navbar and sidebar navigation work correctly
- Chapter groupings in sidebar match the 4-part structure
- Iframe slide embeds display correctly on each chapter page
- "Open slides full-screen" link opens in a new tab
- R code blocks have syntax highlighting and copy button
- No anonymization violations in any new content
- Existing `ch*/index.html` files are unmodified after website render

Since `eval: false`, rendering requires only Quarto 1.8+ (no R installation).

### Anonymization Verification (covers both slides and website)

```bash
rg -i "Meridian|Alliance|Beginnings|Investment Committee|CIFF|Delta Philanthrop|ELMA|Gates Foundation|Mohamed|HaHCo|Fund Two|76 months|\$525|322,000|322,847|Ethiopia|Tanzania|Kenya|Uganda|Ghana|Malawi|Zimbabwe|Rwanda|Lesotho|Nigeria|Phase [12]" inference-and-intervention/**/*.qmd
```

This should return zero matches.
