# Interactive Globe Skills

## Project: Rotating Globe with Population Data

An interactive 3D globe visualization using d3-geo projections with auto-rotation and drag interaction.

## Key Skills Learned

### 1. Geographic Projections with d3-geo

**Orthographic projection (3D globe view):**
```javascript
import { geoOrthographic, geoPath } from "d3-geo";

$: projection = geoOrthographic()
  .scale(width / 2.2)           // Size of the globe
  .rotate([xRotation, yRotation]) // Rotation angles
  .translate([width / 2, height / 2]); // Center position
```

**Other projections available:**
- `geoMercator()` - Flat map (common web maps)
- `geoEquirectangular()` - Simple flat projection
- `geoAlbers()` - Good for USA/regional maps
- Many more in `d3-geo-projection` package

### 2. GeoPath Generator

**Converts geographic coordinates to SVG path strings:**
```javascript
$: path = geoPath(projection);

// Usage in template
<path d={path(country)} />
<path d={path(borders)} />
```

### 3. Loading TopoJSON Data

**Fetch and parse world topology:**
```javascript
import * as topojson from "topojson-client";

onMount(async () => {
  const response = await fetch(
    "https://unpkg.com/world-atlas@2.0.2/countries-110m.json"
  );
  const world = await response.json();

  // Extract features
  countries = topojson.feature(world, world.objects.countries).features;
  borders = topojson.mesh(world, world.objects.countries, (a, b) => a !== b);
});
```

**Why TopoJSON?**
- Smaller file size than GeoJSON
- Shared boundaries stored once
- `topojson.feature()` converts to GeoJSON features
- `topojson.mesh()` extracts shared boundaries

### 4. Auto-Rotation with d3-timer

```javascript
import { timer } from "d3-timer";

let rotation = 0;
const degreesPerFrame = 0.3;

onMount(() => {
  const t = timer(() => {
    if (!dragging) {
      rotation += degreesPerFrame;
    }
  });

  return () => t.stop(); // Cleanup on destroy
});
```

### 5. Drag Interaction with d3-drag

```javascript
import { select } from "d3-selection";
import { drag } from "d3-drag";

let globe; // Reference to SVG element
let dragging = false;
const DRAG_SENSITIVITY = 3;

onMount(() => {
  const element = select(globe);
  element.call(
    drag()
      .on("drag", event => {
        dragging = true;
        xRotation += event.dx * DRAG_SENSITIVITY;
        yRotation -= event.dy * DRAG_SENSITIVITY; // Invert Y
      })
      .on("end", () => {
        dragging = false;
      })
  );
});
```

**Template binding:**
```svelte
<svg bind:this={globe} class:dragging>
```

### 6. Spring Physics for Smooth Rotation

**Svelte's spring store for inertia:**
```javascript
import { spring } from "svelte/motion";

let xRotation = spring(0, {
  stiffness: 0.08, // How snappy (lower = smoother)
  damping: 0.4     // How quickly it settles
});

let yRotation = spring(-20, {
  stiffness: 0.17,
  damping: 0.7
});
```

**Access spring values with $ prefix:**
```javascript
$: projection = geoOrthographic()
  .rotate([$xRotation, $yRotation]);

// Update spring target
$xRotation += event.dx * DRAG_SENSITIVITY;
```

### 7. Joining External Data to Geographic Features

```javascript
// Population data with ISO codes
const populationData = [
  { id: "840", country: "United States", population: 331002647 },
  // ...
];

// Attach to country features
countries.forEach(country => {
  const metadata = populationData.find(d => d.id === country.id);
  if (metadata) {
    country.population = metadata.population;
    country.name = metadata.country;
  }
});
```

### 8. Color Scale for Population

```javascript
$: colorScale = scaleLinear()
  .domain([0, max(populationData, d => d.population)])
  .range(["#1a472a", "#2ecc71"]); // Dark green to bright green

// Usage
<path fill={colorScale(country.population || 0)} />
```

### 9. Globe Layering Order

```svelte
<svg>
  <!-- 1. Ocean background -->
  <circle r={width / 2.2} cx={width / 2} cy={height / 2} fill="#0a2463" />

  <!-- 2. Countries -->
  {#each countries as country}
    <path d={path(country)} fill={colorScale(country.population)} />
  {/each}

  <!-- 3. Borders on top -->
  <path d={path(borders)} fill="none" stroke="rgba(255,255,255,0.3)" />
</svg>
```

## Complete Globe Architecture

```
Data Loading (onMount)
    ↓
TopoJSON → GeoJSON Features
    ↓
Projection (geoOrthographic) ← Rotation State
    ↓
Path Generator (geoPath)
    ↓
SVG Paths (rendered countries)
    ↑
Rotation Control:
  - Timer (auto-rotation)
  - Drag (user interaction)
  - Spring (smooth physics)
```

## Common Gotchas

1. **Y-axis inversion:** Drag Y should be subtracted (up = negative in screen coords)
2. **Cleanup timers:** Return `t.stop()` from onMount to prevent memory leaks
3. **Spring access:** Use `$springName` to read/write spring values
4. **Path updates:** Projection must be reactive (`$:`) for paths to update
5. **Borders vs fill:** Render countries with `stroke="none"`, then overlay separate border path
6. **Missing data:** Use `|| 0` fallback for countries without population data
