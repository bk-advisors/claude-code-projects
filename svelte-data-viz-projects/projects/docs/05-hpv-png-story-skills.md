# HPV PNG Story Skills

## Project: Data-Driven Advocacy Scrollytelling

An interactive data story making the case for HPV vaccination in Papua New Guinea, combining scrollytelling techniques with multiple visualization types.

## Key Skills Learned

### 1. Multi-Chart Story Architecture

**Orchestrating different chart types in one narrative:**
```javascript
const steps = [
  { id: "intro", visualization: "global-stats" },      // BigNumber
  { id: "png-intro", visualization: "bar-chart" },     // BarChart
  { id: "vs-australia", visualization: "comparison" }, // ComparisonChart
  { id: "lives-saved", visualization: "line-chart" },  // LineChart
  { id: "economic", visualization: "roi" }             // ROIChart
];

$: currentConfig = steps[currentStep] || steps[0];
```

**Conditional rendering based on step:**
```svelte
{#if currentConfig.visualization === "bar-chart"}
  <BarChart {data} highlightCountry={currentConfig.highlightCountry} />
{:else if currentConfig.visualization === "line-chart"}
  <LineChart {data} />
{:else if currentConfig.visualization === "comparison"}
  <ComparisonChart {width} {height} />
{/if}
```

### 2. BigNumber Component for Impact

**Emphasizing key statistics (NYT-style):**
```svelte
<script>
  import { fly } from "svelte/transition";

  export let number = "";
  export let label = "";
  export let color = "#c41d3a";
  export let size = "large";
</script>

<div class="big-number" class:large={size === "large"}>
  <span class="number" style="color: {color}" in:fly={{ y: 15, duration: 400 }}>
    {number}
  </span>
  <span class="label">{label}</span>
</div>
```

### 3. Bar Chart with Conditional Highlighting

**Spotlight specific data points:**
```svelte
<script>
  export let highlightCountry = null;

  function isHighlighted(d) {
    if (highlightCountry) {
      return d.country === highlightCountry;
    }
    return d.highlight; // Default from data
  }
</script>

<rect
  fill={isHighlighted(d) ? "#c41d3a" : "#c4c9cf"}
  class:highlighted={isHighlighted(d)}
/>
```

### 4. Area Chart with Cumulative Data

**Line + area for growth visualization:**
```javascript
import { line, area, curveMonotoneX } from "d3-shape";

$: linePath = line()
  .x(d => xScale(d.year))
  .y(d => yScale(d.cumulativeLivesSaved))
  .curve(curveMonotoneX); // Smooth curve

$: areaPath = area()
  .x(d => xScale(d.year))
  .y0(innerHeight)
  .y1(d => yScale(d.cumulativeLivesSaved))
  .curve(curveMonotoneX);
```

**Subtle gradient fill:**
```svelte
<defs>
  <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#1a7f4b;stop-opacity:0.2" />
    <stop offset="100%" style="stop-color:#1a7f4b;stop-opacity:0.03" />
  </linearGradient>
</defs>

<path d={areaPath(data)} fill="url(#areaGradient)" />
```

### 5. Mouse-Following Hover on Line Charts

**Interactive year detection:**
```javascript
function handleMouseMove(event) {
  const rect = event.currentTarget.getBoundingClientRect();
  const x = event.clientX - rect.left - margin.left;
  const year = Math.round(xScale.invert(x));
  hoveredData = data.find(d => d.year === year) || null;
}
```

### 6. Comparison Chart Pattern

**Grouped horizontal bars for country comparison:**
```svelte
{#each data as d}
  <g transform="translate(0, {yScale(d.country)})">
    <!-- Incidence bar (lighter) -->
    <rect
      width={xScale(d.incidence)}
      height={yScale.bandwidth() / 2 - 2}
      fill={d.country === "Papua New Guinea" ? "#e8a5a5" : "#a8c8e8"}
    />

    <!-- Mortality bar (stronger) -->
    <rect
      y={yScale.bandwidth() / 2 + 2}
      width={xScale(d.mortality)}
      height={yScale.bandwidth() / 2 - 2}
      fill={d.country === "Papua New Guinea" ? "#c41d3a" : "#4a7eb8"}
    />
  </g>
{/each}
```

### 7. Two-Column Scrolly Layout

**Left: scrolling text, Right: sticky visualization:**
```css
.section-container {
  display: flex;
  max-width: 1400px;
  margin: 0 auto;
}

.steps-column {
  flex: 0 0 360px;
  width: 360px;
  z-index: 10;
}

.sticky {
  flex: 1;
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### 8. Step Cards with Active State

**Progressive reveal with opacity:**
```svelte
<div class="step" class:active={currentStep === i}>
  <div class="step-content">
    <h2>{step.title}</h2>
    <p>{step.text}</p>
  </div>
</div>
```

```css
.step-content {
  opacity: 0.25;
  border-left: 3px solid transparent;
  transition: opacity 350ms ease, border-color 350ms ease;
}

.step.active .step-content {
  opacity: 1;
  border-left-color: var(--color-danger);
}
```

---

## Data Visualization Design Principles Applied

### Edward Tufte's Principles

#### 1. Maximize Data-Ink Ratio
Remove non-essential visual elements:
```css
/* Subtle grid lines - almost invisible */
line { stroke: #f0f0f0; stroke-width: 1; }

/* Minimal chart containers - no shadows */
.chart-container {
  box-shadow: none;
  border: 1px solid var(--color-border);
}

/* Minimal scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.15); }
```

#### 2. Direct Labeling (Avoid Legends When Possible)
Label data points directly instead of requiring legend lookup:
```svelte
<!-- Value label on each bar -->
<text
  x={xScale.bandwidth() / 2}
  y={yScale(d.rate) - 6}
  class="value-label"
>
  {d.rate}
</text>

<!-- Endpoint annotation on line chart -->
{@const lastPoint = data[data.length - 1]}
<text x={8} y={4} class="annotation">
  {formatNumber(lastPoint.cumulativeLivesSaved)} lives saved
</text>
```

#### 3. Small Multiples Concept
Using the same chart type with different highlighting states creates implicit comparison:
```javascript
// Step 2: Highlight PNG
{ highlightCountry: "Papua New Guinea" }

// Step 3: Show all for context
{ highlightCountry: null }
```

#### 4. Integrate Text and Graphics
Callouts and annotations are embedded within charts:
```svelte
<div class="callout">
  PNG's incidence rate is <strong>5.5x higher</strong> than Australia's.
</div>
```

### Alberto Cairo's Principles

#### 1. Truthful
Data sourced from credible institutions:
```javascript
// Source: Global Cancer Observatory (GCO, 2022)
export const globalDeaths = { total: 348709, ... };

// Source: Ueda (2024), Journal of Obstetrics and Gynaecology Research
export const mortalityRates = [...];
```

#### 2. Functional
Charts chosen to match the data story:
- **Bar charts** for ranking/comparison (mortality rates)
- **Line/area charts** for time series (projected lives saved)
- **Grouped bars** for paired comparisons (PNG vs Australia)
- **Big numbers** for impact statistics

#### 3. Beautiful (But Not Decorative)
Refined color palette serves meaning:
```css
:root {
  --color-danger: #c41d3a;      /* Deaths, urgency */
  --color-success: #1a7f4b;     /* Lives saved, hope */
  --color-text-light: #777;     /* De-emphasized text */
}
```

#### 4. Insightful
Contextual annotations reveal the story:
```svelte
<div class="stakes-context">
  <p>That's equivalent to the entire population of a provincial town.</p>
</div>
```

#### 5. Enlightening
Progressive disclosure through scrollytelling:
1. Global context → Regional burden → PNG specifically
2. Problem → Comparison → Solution → ROI

### New York Times Style Patterns

#### 1. Editorial Typography
```css
:root {
  --font-serif: "Georgia", "Times New Roman", serif;  /* Body text */
  --font-sans: -apple-system, BlinkMacSystemFont, sans-serif;  /* Labels */

  font-family: var(--font-serif);
  font-size: 17px;
  line-height: 1.65;
}
```

#### 2. Kicker + Headline Pattern
```svelte
<header class="hero">
  <p class="kicker">Health Equity in the Pacific</p>
  <h1>The Case for HPV Vaccination in Papua New Guinea</h1>
  <p class="subtitle">...</p>
  <p class="byline">An interactive data story by Matthew Kuch</p>
</header>
```

#### 3. Source Citations
```svelte
<p class="chart-source">
  Source: Ueda (2024), Journal of Obstetrics and Gynaecology Research
</p>
```

---

## Component Architecture

```
src/
├── App.svelte          # Main story with scrolly logic
├── app.css             # Global styles with design tokens
├── components/
│   ├── BarChart.svelte       # Mortality rates
│   ├── LineChart.svelte      # Projected lives saved
│   ├── ComparisonChart.svelte # PNG vs Australia
│   ├── ROIChart.svelte       # Economic returns
│   ├── BigNumber.svelte      # Impact statistics
│   ├── AxisX.svelte          # Reusable X axis
│   └── AxisY.svelte          # Reusable Y axis
├── helpers/
│   └── Scrolly.svelte        # Intersection Observer wrapper
└── data/
    └── data.js               # All datasets with sources
```

---

## Color Semantics

| Color | Hex | Meaning |
|-------|-----|---------|
| Danger Red | `#c41d3a` | Deaths, urgency, PNG highlight |
| Success Green | `#1a7f4b` | Lives saved, solutions, ROI |
| Muted Gray | `#c4c9cf` | Non-highlighted bars |
| Primary Dark | `#121f2b` | Hero background, headings |
| Accent Blue | `#6eb5d9` | Secondary highlights |

---

## Accessibility Considerations

```svelte
<!-- ARIA labels on interactive elements -->
<rect
  role="img"
  aria-label="{d.country}: {d.rate} deaths per 100,000"
/>

<!-- Focus styles -->
button:focus, a:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

<!-- Visually hidden utility -->
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  clip: rect(0, 0, 0, 0);
}
```

---

## Animation Philosophy

**Purposeful, not decorative:**
```svelte
<!-- Entrance animation for bars - staggered -->
<rect in:fly={{ y: innerHeight - yScale(d.rate), duration: 500, delay: i * 40 }} />

<!-- Subtle transitions for state changes -->
rect { transition: opacity 200ms ease; }

<!-- Tooltip fade -->
<div class="tooltip" transition:fade={{ duration: 100 }}>
```

---

## Responsive Behavior

```css
/* Tablet: Stack columns */
@media (max-width: 1024px) {
  .section-container { flex-direction: column; }
  .steps-column { width: 100%; }
}

/* Mobile: Reduce sizes */
@media (max-width: 768px) {
  .hero h1 { font-size: 2rem; }
  .stat-breakdown { flex-direction: column; }
  .inequity-icons { grid-template-columns: 1fr; }
}
```

---

## Key Takeaways

1. **Story-first design**: Chart selection serves the narrative, not the reverse
2. **Progressive disclosure**: Build understanding step by step
3. **Tufte minimalism**: Remove chart junk, maximize data-ink ratio
4. **Cairo functionality**: Choose chart types that reveal insights
5. **Direct labeling**: Reduce cognitive load, avoid legend lookups
6. **Semantic color**: Meaning encoded in the palette
7. **Source attribution**: Credibility through citation
8. **Responsive advocacy**: Works across devices
