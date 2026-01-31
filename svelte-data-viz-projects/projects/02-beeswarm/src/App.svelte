<script>
  import AxisX from "$components/AxisX.svelte";
  import AxisY from "$components/AxisY.svelte";
  import Legend from "$components/Legend.svelte";
  import Tooltip from "$components/Tooltip.svelte";

  import data from "$data/data.js";
  import { forceSimulation, forceX, forceY, forceCollide } from "d3-force";
  import { scaleLinear, scaleBand, scaleOrdinal, scaleSqrt } from "d3-scale";
  import { mean, rollups } from "d3-array";
  import { fade } from "svelte/transition";

  let width = 400;
  let height = 400;
  const margin = { top: 0, right: 0, left: 0, bottom: 20 };

  // Generate the average happiness for each continent for sorting
  const continents = rollups(
    data,
    v => mean(v, d => d.happiness),
    d => d.continent
  )
    .sort((a, b) => a[1] - b[1])
    .map(d => d[0]);

  const colorRange = [
    "#dda0dd",
    "#fe7f2d",
    "#fcca46",
    "#a1c181",
    "#619b8a",
    "#eae2b7"
  ];

  const colorScale = scaleOrdinal()
    .domain(continents)
    .range(colorRange);

  $: radiusScale = scaleSqrt()
    .domain([1, 9])
    .range(width < 568 ? [2, 6] : [3, 8]);

  $: xScale = scaleLinear()
    .domain([1, 9])
    .range([0, width - margin.left - margin.right]);

  const yScale = scaleBand()
    .domain(continents)
    .range([height - margin.bottom - margin.top, 0])
    .paddingOuter(0.5);

  // D3 Force Simulation
  const simulation = forceSimulation(data);
  let nodes = [];

  simulation.on("tick", () => {
    nodes = simulation.nodes();
  });

  // Reactive simulation updates
  $: {
    simulation
      .force(
        "x",
        forceX()
          .x(d => xScale(d.happiness))
          .strength(0.8)
      )
      .force(
        "y",
        forceY()
          .y(d =>
            groupByContinent
              ? yScale(d.continent)
              : (height - margin.bottom - margin.top) / 2
          )
          .strength(0.2)
      )
      .force("collide", forceCollide().radius(d => radiusScale(d.happiness)))
      .alpha(0.3)
      .alphaDecay(0.0005)
      .restart();
  }

  // Interactivity state
  let hovered;
  let hoveredContinent;
  let groupByContinent = false;
</script>

<h1>The Happiest Countries in the World</h1>
<p class="subtitle">Click to group by continent</p>

<Legend {colorScale} bind:hoveredContinent />

<div
  class="chart-container"
  bind:clientWidth={width}
  on:click={() => {
    groupByContinent = !groupByContinent;
    hovered = null;
  }}
  role="button"
  tabindex="0"
  on:keydown={(e) => e.key === 'Enter' && (groupByContinent = !groupByContinent)}
>
  <svg {width} {height}>
    <AxisX {xScale} {height} {width} {margin} />
    <AxisY {yScale} {margin} {groupByContinent} />

    {#if hovered}
      <line
        transition:fade
        x1={hovered.x}
        x2={hovered.x}
        y1={height - margin.bottom}
        y2={hovered.y + margin.top + radiusScale(hovered.happiness)}
        stroke={colorScale(hovered.continent)}
        stroke-width="2"
      />
    {/if}

    <g
      class="inner-chart"
      transform="translate({margin.left}, {margin.top})"
      on:mouseleave={() => (hovered = null)}
    >
      {#each nodes as node, i}
        <circle
          in:fade={{ delay: 200 + 10 * i, duration: 400 }}
          cx={node.x}
          cy={node.y}
          r={radiusScale(node.happiness)}
          fill={colorScale(node.continent)}
          title={node.country}
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
          on:mouseover={() => (hovered = node)}
          on:focus={() => (hovered = node)}
          tabindex="0"
          on:click|stopPropagation
          role="button"
          aria-label="{node.country}: Happiness {node.happiness}"
        />
      {/each}
    </g>
  </svg>

  {#if hovered}
    <Tooltip data={hovered} {colorScale} {width} />
  {/if}
</div>

<style>
  :global(.tick text, .axis-title) {
    font-size: 12px;
    font-weight: 400;
    fill: hsla(212, 10%, 53%, 1);
    user-select: none;
  }

  h1 {
    margin: 0 0 0.25rem 0;
    font-size: 1.35rem;
    font-weight: 600;
    text-align: center;
  }

  .subtitle {
    text-align: center;
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 0.5rem;
  }

  .chart-container {
    position: relative;
    cursor: pointer;
  }

  circle {
    transition: stroke 300ms ease, opacity 300ms ease;
    cursor: pointer;
  }
</style>
