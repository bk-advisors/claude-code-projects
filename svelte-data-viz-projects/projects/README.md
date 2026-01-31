# Svelte + D3.js Data Visualization Projects

Four interactive data visualization projects built with Svelte and D3.js, based on Connor Rothschild's "Better Data Visualizations with Svelte" course.

## Projects

### 1. Scatterplot
An interactive, responsive scatterplot showing the relationship between study hours and exam grades.

**Features:**
- Responsive design with `bind:clientWidth`
- D3 scales (linear)
- Custom axes components
- Hover tooltips
- Animated transitions

```bash
cd 01-scatterplot
npm install
npm run dev
```

### 2. Beeswarm Plot
A physics-based visualization of World Happiness data using D3 force simulation.

**Features:**
- D3 force simulation for physics-based layout
- Multiple scale types (linear, band, ordinal, sqrt)
- Interactive legend with continent filtering
- Click to toggle grouping by continent
- Data aggregation with d3-array

```bash
cd 02-beeswarm
npm install
npm run dev
```

### 3. Interactive Globe
A rotating 3D globe showing world population data.

**Features:**
- Geographic projections with d3-geo
- TopoJSON data loading
- Auto-rotation with d3-timer
- Drag interaction with d3-drag
- Spring physics for smooth movement
- Color scale for population data

```bash
cd 03-globe
npm install
npm run dev
```

### 4. Scrollytelling
An NYT-style scrolling narrative article with progressive data reveals.

**Features:**
- Intersection Observer for scroll detection
- Sticky chart positioning
- Step-based narrative structure
- Conditional highlighting
- Smooth CSS transitions

```bash
cd 04-scrollytelling
npm install
npm run dev
```

## Documentation

See the [docs/](./docs/) folder for detailed skill documentation:

- [Overview & Universal Patterns](./docs/00-overview.md)
- [Scatterplot Skills](./docs/01-scatterplot-skills.md)
- [Beeswarm Skills](./docs/02-beeswarm-skills.md)
- [Globe Skills](./docs/03-globe-skills.md)
- [Scrollytelling Skills](./docs/04-scrollytelling-skills.md)

## Tech Stack

- **Svelte 4** - Reactive framework for UI
- **Vite 5** - Fast build tool
- **D3.js modules** - Data visualization utilities
  - d3-scale - Mapping data to visual values
  - d3-array - Array utilities (extent, mean, rollups)
  - d3-force - Physics simulations
  - d3-geo - Geographic projections
  - d3-timer - Animation timers
  - d3-drag - Drag interactions

## Key Concepts

### The Svelte + D3 Approach
- **Svelte** handles DOM manipulation via reactive bindings
- **D3** handles data transformation (scales, forces, projections)
- This hybrid approach is simpler than pure D3 DOM manipulation

### Common Patterns
```svelte
<!-- Reactive scales -->
$: xScale = scaleLinear().domain([0, 100]).range([0, width]);

<!-- Responsive sizing -->
<div bind:clientWidth={width}>

<!-- Conditional rendering -->
{#if hoveredData}
  <Tooltip data={hoveredData} />
{/if}
```

## Creating New Visualizations

Use these projects as templates. The general workflow:

1. **Setup**: Create Vite + Svelte project, install D3 modules
2. **Data**: Load/format your data
3. **Scales**: Map data values to visual properties
4. **Layout**: Define margins, dimensions
5. **Render**: Use `{#each}` to create SVG elements
6. **Interact**: Add hover, click, drag handlers
7. **Polish**: Add transitions, tooltips, legends
