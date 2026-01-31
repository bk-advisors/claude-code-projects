# Svelte + D3.js Data Visualization Skills Reference

This documentation captures the core skills and patterns learned from Connor Rothschild's "Better Data Visualizations with Svelte" course.

## Course Overview

The course teaches a hybrid approach to data visualization:
- **Svelte** handles DOM manipulation via reactive bindings
- **D3.js modules** handle data transformation (scales, forces, geographic projections)

This approach simplifies D3's learning curve while leveraging its powerful data tools.

## Projects Completed

| Project | Key Skills |
|---------|-----------|
| [01-Scatterplot](./01-scatterplot-skills.md) | Scales, axes, responsive design, tooltips, transitions |
| [02-Beeswarm](./02-beeswarm-skills.md) | Force simulation, color scales, legends, physics |
| [03-Globe](./03-globe-skills.md) | Geographic projections, rotation, drag interaction, springs |
| [04-Scrollytelling](./04-scrollytelling-skills.md) | Intersection Observer, sticky positioning, narrative |

## Core Technologies

```json
{
  "svelte": "^4.2.0",
  "vite": "^5.0.0",
  "d3-scale": "^4.0.2",
  "d3-array": "^3.2.0",
  "d3-force": "^3.0.0",
  "d3-geo": "^3.1.0",
  "d3-timer": "^3.0.1",
  "d3-drag": "^3.0.0",
  "d3-selection": "^3.0.0",
  "topojson-client": "^3.1.0"
}
```

## Universal Patterns

### 1. Reactive Scales
```svelte
<script>
  import { scaleLinear } from "d3-scale";

  let width = 400;

  // Reactive: updates automatically when width changes
  $: xScale = scaleLinear()
    .domain([0, 100])
    .range([0, width]);
</script>
```

### 2. Responsive Charts with bind:clientWidth
```svelte
<div class="chart-container" bind:clientWidth={width}>
  <svg {width} {height}>
    <!-- Chart content -->
  </svg>
</div>
```

### 3. Component Composition
```svelte
<!-- App.svelte -->
<AxisX {xScale} {width} {height} {margin} />
<AxisY {yScale} {width} {margin} />
<Tooltip {data} {xScale} {yScale} />
```

### 4. Hover Interactivity
```svelte
<script>
  let hoveredData;
</script>

<svg on:mouseleave={() => (hoveredData = null)}>
  {#each data as d}
    <circle
      on:mouseover={() => (hoveredData = d)}
      opacity={hoveredData ? (hoveredData === d ? 1 : 0.3) : 0.85}
    />
  {/each}
</svg>

{#if hoveredData}
  <Tooltip data={hoveredData} />
{/if}
```

### 5. Transitions with Svelte
```svelte
<script>
  import { fly, fade } from "svelte/transition";
</script>

<circle in:fly={{ x: -10, duration: 500 }} />
<div transition:fade />
```

## Quick Start for New Projects

```bash
# Create new project
npm create vite@latest my-viz -- --template svelte

# Install D3 modules (only what you need)
npm install d3-scale d3-array

# For force layouts
npm install d3-force

# For geographic maps
npm install d3-geo topojson-client

# For interactive drag
npm install d3-drag d3-selection d3-timer
```

## Vite Configuration with Path Aliases

```javascript
// vite.config.js
import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

export default defineConfig({
  plugins: [svelte()],
  resolve: {
    alias: {
      $components: path.resolve("./src/components"),
      $data: path.resolve("./src/data")
    }
  }
});
```
