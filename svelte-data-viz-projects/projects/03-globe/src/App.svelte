<script>
  import { onMount } from "svelte";
  import { spring } from "svelte/motion";
  import { geoOrthographic, geoPath } from "d3-geo";
  import { scaleLinear } from "d3-scale";
  import { max } from "d3-array";
  import { timer } from "d3-timer";
  import { select } from "d3-selection";
  import { drag } from "d3-drag";
  import * as topojson from "topojson-client";

  import Legend from "$components/Legend.svelte";
  import Tooltip from "$components/Tooltip.svelte";
  import populationData from "$data/population.js";

  let width = 500;
  $: height = width;

  let world = null;
  let countries = [];
  let borders = null;

  // Rotation with spring physics for smooth dragging
  let xRotation = spring(0, { stiffness: 0.08, damping: 0.4 });
  let yRotation = spring(-20, { stiffness: 0.17, damping: 0.7 });

  // Dragging state
  let globe;
  let dragging = false;
  const DRAG_SENSITIVITY = 3;
  const degreesPerFrame = 0.3;

  // Hover state
  let hoveredCountry = null;
  let mouseX = 0;
  let mouseY = 0;

  // Color scale for population
  $: colorScale = scaleLinear()
    .domain([0, max(populationData, d => d.population) || 1400000000])
    .range(["#1a472a", "#2ecc71"]);

  // Geographic projection
  $: projection = geoOrthographic()
    .scale(width / 2.2)
    .rotate([$xRotation, $yRotation])
    .translate([width / 2, height / 2]);

  // Path generator
  $: path = geoPath(projection);

  // Load world topology data
  onMount(async () => {
    try {
      const response = await fetch(
        "https://unpkg.com/world-atlas@2.0.2/countries-110m.json"
      );
      world = await response.json();

      countries = topojson.feature(world, world.objects.countries).features;
      borders = topojson.mesh(world, world.objects.countries, (a, b) => a !== b);

      // Attach population data to countries
      countries.forEach(country => {
        const metadata = populationData.find(d => d.id === country.id);
        if (metadata) {
          country.population = metadata.population;
          country.name = metadata.country;
        }
      });
    } catch (error) {
      console.error("Failed to load world data:", error);
    }

    // Auto-rotation timer
    const t = timer(() => {
      if (!dragging) {
        $xRotation += degreesPerFrame;
      }
    });

    // Setup drag interaction
    const element = select(globe);
    element.call(
      drag()
        .on("drag", event => {
          dragging = true;
          $xRotation += event.dx * DRAG_SENSITIVITY;
          $yRotation -= event.dy * DRAG_SENSITIVITY;
        })
        .on("end", () => {
          dragging = false;
        })
    );

    return () => t.stop();
  });

  function handleMouseMove(event) {
    mouseX = event.clientX;
    mouseY = event.clientY;
  }

  function handleCountryHover(country) {
    hoveredCountry = country;
  }

  function handleCountryLeave() {
    hoveredCountry = null;
  }
</script>

<div class="container" bind:clientWidth={width}>
  <h1>World Population</h1>
  <p class="subtitle">Drag to rotate the globe</p>

  <div class="globe-container" on:mousemove={handleMouseMove}>
    <svg
      {width}
      {height}
      bind:this={globe}
      class:dragging
    >
      <!-- Ocean background -->
      <circle
        r={width / 2.2}
        cx={width / 2}
        cy={height / 2}
        fill="#0a2463"
      />

      {#if countries.length > 0}
        <!-- Countries -->
        {#each countries as country}
          <path
            d={path(country)}
            fill={colorScale(country.population || 0)}
            stroke="none"
            on:mouseenter={() => handleCountryHover(country)}
            on:mouseleave={handleCountryLeave}
            role="button"
            tabindex="-1"
            class="country"
          />
        {/each}

        <!-- Borders -->
        {#if borders}
          <path
            d={path(borders)}
            fill="none"
            stroke="rgba(255, 255, 255, 0.3)"
            stroke-width="0.5"
          />
        {/if}
      {:else}
        <!-- Loading indicator -->
        <text
          x={width / 2}
          y={height / 2}
          text-anchor="middle"
          fill="white"
        >
          Loading...
        </text>
      {/if}
    </svg>

    <Legend {colorScale} />

    {#if hoveredCountry}
      <Tooltip country={hoveredCountry} x={mouseX} y={mouseY} />
    {/if}
  </div>
</div>

<style>
  .container {
    max-width: 600px;
    margin: 0 auto;
  }

  h1 {
    color: white;
    text-align: center;
    margin: 0 0 0.25rem 0;
    font-size: 1.5rem;
    font-weight: 600;
  }

  .subtitle {
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    font-size: 0.9rem;
    margin-bottom: 1rem;
  }

  .globe-container {
    position: relative;
  }

  svg {
    display: block;
    cursor: grab;
    user-select: none;
  }

  svg.dragging {
    cursor: grabbing;
  }

  .country {
    transition: opacity 150ms ease;
  }

  .country:hover {
    opacity: 0.8;
  }
</style>
