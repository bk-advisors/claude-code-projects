# BK Advisors — Quarto Design Principles

A reference guide for styling Quarto reveal.js slides and HTML reports. These principles are applied across all BKA course decks and companion pages.

---

## 1. Typography

**Font stack:** Inter (Google Fonts) with Calibri fallback for offline/brand consistency.

```scss
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
$font-family-sans-serif: "Inter", "Calibri", "Segoe UI", system-ui, sans-serif;
$headings-font-family: "Inter", "Calibri Light", "Calibri", system-ui, sans-serif;
```

**Why Inter:** Renders consistently across all platforms, highly legible at small sizes (data-dense slides), free, well-maintained. Falls back to Calibri (PPTX brand font) when offline.

**Heading weight:** Use `font-weight: 600` (semi-bold) instead of 700 (bold). Lighter feel, more modern.

**Letter-spacing:** Tighten headings to `-0.02em`. Tighter tracking on large text reads as professional/editorial.

**Line-height:** `1.4` for slides, `1.7` for HTML reports/blog posts. Reports need more breathing room for sustained reading.

**Type scale (slides):**
```scss
$presentation-font-size-root: 36px;
$presentation-h1-font-size: 1.8em;
$presentation-h2-font-size: 1.3em;   // not 1.4 — tighter hierarchy
$presentation-h3-font-size: 1.05em;  // not 1.1 — closer to body
```

---

## 2. Color

**Background:** `#FAFBFC` off-white instead of pure `#FFFFFF`. Reduces eye strain, looks more designed.

**Body text:** `#2D3748` warm dark gray instead of `#333333`. Softer, less harsh.

**Headings:** `#242852` (BKA navy) instead of `$bka-blue` (`#005CB9`). Creates clear hierarchy — headings are distinct from links and interactive elements.

**The Knaflic principle:** "Grey everything, color only what matters." Default chart elements and secondary text to gray tones. Reserve BKA brand colors for focal points.

**Design tokens:**
```scss
$bka-navy: #242852;     // titles, emphasis text
$bka-body: #2D3748;     // body text, paragraphs
$bka-blue: #005CB9;     // links, interactive, primary accent
$bka-light-blue: #00A1DF;  // secondary accent
// ... rest of BKA palette unchanged
```

---

## 3. Spacing

The single biggest differentiator between "template" and "designed."

**Slides:**
```scss
.reveal .slides section {
  padding: 40px 60px;       // generous horizontal padding
}

h2 { margin-bottom: 0.8em; }  // more air after headings (was 0.6em)
ul li { margin-bottom: 0.5em; }  // breathing room between bullets
```

**Reports:**
```scss
body { line-height: 1.7; }    // comfortable reading rhythm
h2 { margin-top: 2em; }       // clear section breaks
```

**Content width (reports):**
```scss
.content { max-width: 760px; margin: 0 auto; }  // optimal reading width
```

---

## 4. Shadows

**Layered box-shadows** (Josh W. Comeau technique). Two-layer shadows create realistic depth — a tight shadow for definition + a soft spread for atmosphere:

```scss
box-shadow:
  0 1px 3px rgba(0, 0, 0, 0.08),   // tight: defines the edge
  0 4px 12px rgba(0, 0, 0, 0.04);  // soft: creates depth
```

Apply to: callout boxes, key-concept cards, example blocks, code blocks, tables, slide-embed containers, chapter cards.

**Colored shadows** for branded elements (step badges, key-takeaway):
```scss
.step-number {
  box-shadow: 0 2px 8px rgba($bka-blue, 0.25);
}

.key-takeaway {
  box-shadow:
    0 2px 4px rgba($bka-blue, 0.2),
    0 8px 24px rgba($bka-blue, 0.1);
}
```

---

## 5. Gradient Accents

**Heading underlines** — gradient fade replacing flat `border-bottom`:
```scss
h2::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  margin-top: 10px;
  background: linear-gradient(90deg, $bka-blue, $bka-light-blue);
  border-radius: 2px;
}
```

**Key-takeaway boxes** — gradient background:
```scss
.key-takeaway {
  background: linear-gradient(135deg, $bka-blue, darken($bka-blue, 8%));
}
```

**Compass center / hero elements:**
```scss
.compass-center {
  background: linear-gradient(135deg, $bka-blue, darken($bka-blue, 10%));
}
```

---

## 6. Border-Radius System

Pick 3 sizes and use them everywhere — consistency creates visual coherence:

```scss
$radius-sm: 6px;    // callout boxes, inline badges, blockquotes
$radius-md: 10px;   // cards, code blocks, tables, key-takeaway
$radius-lg: 16px;   // hero sections (rarely used)
```

---

## 7. Micro-Interactions

**Fragment animations (slides):**
```scss
.reveal .fragment {
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
.reveal .fragment:not(.visible) {
  opacity: 0;
  transform: translateY(8px);  // subtle upward fade-in
}
```

**Hover lift (cards/quadrant boxes):**
```scss
.quadrant-box {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.1), 0 8px 20px rgba(0,0,0,0.06);
  }
}
```

**Table row hover:**
```scss
tbody tr:hover { background: rgba($bka-blue, 0.03); }
```

---

## Code Block Styling

```scss
// Slides
.reveal pre {
  border-radius: $radius-md;
  border-left: 3px solid $bka-blue;
  background: #F1F3F5;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 2px 8px rgba(0,0,0,0.03);
  font-size: 0.7em;
}

// Reports — inline code
p code, li code {
  background: rgba($bka-blue, 0.06);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.88em;
}
```

---

## Table Styling (Reports)

```scss
table {
  border-collapse: separate;
  border-spacing: 0;
  border-radius: $radius-md;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 2px 8px rgba(0,0,0,0.03);
}

thead th {
  background: $bka-navy;
  color: white;
  font-weight: 600;
  padding: 10px 14px;
}

tbody td {
  padding: 8px 14px;
  border-bottom: 1px solid #E8E8E8;
}

tbody tr:hover { background: rgba($bka-blue, 0.03); }
```

---

## ggplot2 Consistency

Match plot fonts to slide/report fonts:
```r
library(showtext)
font_add_google("Inter", "Inter")
showtext_auto()

# Transparent background inherits slide/page bg
ggsave("chart.png", bg = "transparent", dpi = 300)
```

Use BKA navy (`#242852`) for titles/annotations and BKA gray (`#606060`) for subtitles/axis labels in plots — matching the SCSS heading/body hierarchy.

---

## Sources

- **Cole Nussbaumer Knaflic** — "grey everything, color only what matters"
- **Edward Tufte** — maximize data-ink ratio, subtle gridlines
- **Josh W. Comeau** — layered box-shadow technique
- **Stephen Few** — readable typography, consistent sizing
- **Alberto Cairo** — meaningful annotations, pre-attentive attributes
