# Beeswarm Plot Skills

## Project: Physics-Based Beeswarm with Force Simulation

A beeswarm plot using D3's force simulation to prevent circle overlap, with interactive grouping by continent.

## Key Skills Learned

### 1. D3 Force Simulation

**Core concept:** Circles are "nodes" that repel each other with physics.

```javascript
import { forceSimulation, forceX, forceY, forceCollide } from "d3-force";

// Initialize simulation with data
const simulation = forceSimulation(data);

// Track node positions (simulation mutates the original data)
let nodes = [];
simulation.on("tick", () => {
  nodes = simulation.nodes();
});
```

**Force types:**
- `forceX` - attracts nodes horizontally to a target x position
- `forceY` - attracts nodes vertically to a target y position
- `forceCollide` - prevents nodes from overlapping

```javascript
$: {
  simulation
    .force("x", forceX()
      .x(d => xScale(d.happiness))
      .strength(0.8))
    .force("y", forceY()
      .y(d => groupByContinent
        ? yScale(d.continent)
        : height / 2)
      .strength(0.2))
    .force("collide", forceCollide()
      .radius(d => radiusScale(d.happiness)))
    .alpha(0.3)
    .alphaDecay(0.0005)
    .restart();
}
```

**Important parameters:**
- `strength` (0-1): How strongly the force pulls nodes
- `alpha` (0-1): "Temperature" of simulation - higher = more movement
- `alphaDecay`: How quickly simulation cools down

### 2. Multiple Scale Types

**Linear scale for continuous data:**
```javascript
$: xScale = scaleLinear()
  .domain([1, 9])
  .range([0, width]);
```

**Band scale for categorical data:**
```javascript
const yScale = scaleBand()
  .domain(continents) // ["Africa", "Asia", "Europe", ...]
  .range([height, 0])
  .paddingOuter(0.5);
```

**Ordinal scale for colors:**
```javascript
const colorScale = scaleOrdinal()
  .domain(continents)
  .range(["#dda0dd", "#fe7f2d", "#fcca46", ...]);
```

**Square root scale for radius (area perception):**
```javascript
$: radiusScale = scaleSqrt()
  .domain([1, 9])
  .range(width < 568 ? [2, 6] : [3, 8]);
```

**Why sqrt for radius?** Human perception of size is based on area, not radius. `scaleSqrt` ensures visual proportionality.

### 3. Data Aggregation with d3-array

**Calculate mean per group and sort:**
```javascript
import { mean, rollups } from "d3-array";

const continents = rollups(
  data,
  v => mean(v, d => d.happiness), // Aggregate function
  d => d.continent               // Group key
)
  .sort((a, b) => a[1] - b[1])   // Sort by happiness
  .map(d => d[0]);                // Extract continent names
```

### 4. Interactive Legend Component

**Two-way binding for hover state:**
```svelte
<!-- App.svelte -->
<Legend {colorScale} bind:hoveredContinent />

<!-- Legend.svelte -->
<script>
  export let colorScale;
  export let hoveredContinent;
</script>

<div on:mouseleave={() => (hoveredContinent = null)}>
  {#each colorScale.domain() as continent}
    <p
      class:unhovered={hoveredContinent && hoveredContinent !== continent}
      on:mouseover={() => (hoveredContinent = continent)}
    >
      <span style="background: {colorScale(continent)}" />
      {continent}
    </p>
  {/each}
</div>
```

### 5. Toggle Interaction

**Click to toggle grouping state:**
```svelte
<script>
  let groupByContinent = false;
</script>

<div on:click={() => { groupByContinent = !groupByContinent; }}>
  <!-- Chart -->
</div>
```

The reactive block re-runs the simulation when `groupByContinent` changes.

### 6. Conditional Styling with Multiple States

```svelte
<circle
  opacity={hovered || hoveredContinent
    ? hovered === node || hoveredContinent === node.continent
      ? 1
      : 0.3
    : 1}
  stroke={hovered || hoveredContinent
    ? hovered === node || hoveredContinent === node.continent
      ? "black"
      : "transparent"
    : "#00000090"}
/>
```

### 7. Reference Lines

**Draw a line from hovered point to axis:**
```svelte
{#if hovered}
  <line
    transition:fade
    x1={hovered.x}
    x2={hovered.x}
    y1={height - margin.bottom}
    y2={hovered.y + radiusScale(hovered.happiness)}
    stroke={colorScale(hovered.continent)}
    stroke-width="2"
  />
{/if}
```

## Force Simulation Lifecycle

```
1. Initialize: forceSimulation(data)
       ↓
2. Configure forces: .force("x", ...).force("y", ...).force("collide", ...)
       ↓
3. Set energy: .alpha(0.3).alphaDecay(0.0005)
       ↓
4. Start: .restart()
       ↓
5. On each tick: nodes = simulation.nodes()
       ↓
6. Render: {#each nodes as node} <circle cx={node.x} cy={node.y} />
```

## Common Gotchas

1. **Mutation warning:** `forceSimulation` mutates the original data array, adding `x`, `y`, `vx`, `vy` properties
2. **Restart required:** Call `.restart()` after changing forces
3. **Alpha decay:** Lower values = slower, smoother animations but more expensive
4. **Event propagation:** Use `on:click|stopPropagation` on circles to prevent triggering parent click
