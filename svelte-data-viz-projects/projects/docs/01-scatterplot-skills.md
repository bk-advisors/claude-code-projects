# Scatterplot Skills

## Project: Interactive Responsive Scatterplot

A responsive scatterplot with hover interactions, tooltips, and animated transitions.

## Key Skills Learned

### 1. D3 Scales

**Linear Scale for continuous data:**
```javascript
import { scaleLinear } from "d3-scale";
import { max } from "d3-array";

// X-axis: grade (0-100%)
$: xScale = scaleLinear()
  .domain([0, 100])
  .range([0, width - margin.left - margin.right]);

// Y-axis: hours (0 to max hours in data)
$: yScale = scaleLinear()
  .domain([0, max(data, d => d.hours)])
  .range([height - margin.bottom - margin.top, 0]); // Inverted for SVG
```

**Key insight:** Y-axis range is inverted because SVG coordinates start from top-left.

### 2. Responsive Design

```svelte
<script>
  let width = 400; // Initial fallback
  let height = 400;
</script>

<div class="chart-container" bind:clientWidth={width}>
  <svg {width} {height}>
    <!-- Chart content -->
  </svg>
</div>
```

**Reactive scales update automatically** when `width` changes.

### 3. Margin Convention

```javascript
const margin = { top: 20, right: 15, bottom: 40, left: 0 };

// Apply margins via transform
<g class="inner-chart" transform="translate({margin.left}, {margin.top})">
```

### 4. Axis Components

**X-Axis with custom ticks:**
```svelte
<script>
  export let xScale;
  export let height;
  export let margin;

  let xTicks = [0, 25, 50, 75, 100];
</script>

<g class="axis x" transform="translate(0, {height - margin.bottom})">
  {#each xTicks as tick}
    <g class="tick" transform="translate({xScale(tick)}, 0)">
      <line x1={0} x2={0} y1={0} y2={6} stroke="black" />
      <text y={6} dy={12}>{tick}%</text>
    </g>
  {/each}
</g>
```

**Y-Axis with auto-generated ticks:**
```svelte
<script>
  $: yTicks = yScale.ticks(4); // D3 generates ~4 nice tick values
</script>
```

### 5. Hover Interactivity

**Pattern: Track hovered item, conditionally style:**
```svelte
<script>
  let hoveredData;
</script>

<circle
  r={hoveredData === d ? radius * 2 : radius}
  opacity={hoveredData ? (hoveredData === d ? 1 : 0.45) : 0.85}
  on:mouseover={() => (hoveredData = d)}
/>
```

### 6. Tooltips

**Key techniques:**
- Position absolutely relative to chart container
- Calculate position based on data point coordinates
- Handle edge cases (tooltip overflow)

```svelte
<script>
  $: x = xScale(data.grade);
  $: y = yScale(data.hours);

  let tooltipWidth;

  // Flip tooltip if it would overflow right edge
  $: xPosition = x + tooltipWidth > width
    ? x - tooltipWidth - 15
    : x + 15;
</script>

<div
  class="tooltip"
  style="position: absolute; top: {yPosition}px; left: {xPosition}px"
  bind:clientWidth={tooltipWidth}
>
```

### 7. Animated Transitions

**Entry animation with staggered delay:**
```svelte
<script>
  import { fly } from "svelte/transition";
</script>

{#each data.sort((a, b) => a.grade - b.grade) as d, index}
  <circle
    in:fly={{ x: -10, opacity: 0, duration: 500, delay: index * 30 }}
  />
{/each}
```

**CSS transitions for smooth state changes:**
```css
circle {
  transition: r 300ms ease, opacity 500ms ease;
  cursor: pointer;
}
```

## Complete Data Flow

```
Data (JS array)
    ↓
Scales (d3-scale) - map data values to pixel positions
    ↓
SVG Elements (Svelte #each) - render circles at scaled positions
    ↓
Interactivity (Svelte reactive) - update styles on hover
    ↓
Tooltip (Svelte conditional) - show on hover
```

## Common Gotchas

1. **SVG Y-axis inversion:** Remember to invert the range for y-scales
2. **Margin application:** Use `transform` on a group, not on individual elements
3. **Tooltip positioning:** Account for container offset when using absolute positioning
4. **Accessibility:** Add `role="button"` and `tabindex="0"` for keyboard navigation
