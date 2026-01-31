<script>
  import AxisX from "$components/AxisX.svelte";
  import AxisY from "$components/AxisY.svelte";
  import Tooltip from "$components/Tooltip.svelte";
  import data from "$data/data.js";

  import { scaleLinear } from "d3-scale";
  import { max } from "d3-array";
  import { fly } from "svelte/transition";

  let width = 400;
  let height = 400;

  const margin = { top: 20, right: 15, bottom: 40, left: 0 };
  const radius = 10;

  // Reactive scales that update when width changes
  $: xScale = scaleLinear()
    .domain([0, 100])
    .range([0, width - margin.left - margin.right]);

  $: yScale = scaleLinear()
    .domain([0, max(data, d => d.hours)])
    .range([height - margin.bottom - margin.top, 0]);

  let hoveredData;
</script>

<h1>Students who studied longer scored higher on their final exams</h1>

<div class="chart-container" bind:clientWidth={width}>
  <svg {width} {height} on:mouseleave={() => (hoveredData = null)}>
    <AxisX {xScale} {width} {height} {margin} />
    <AxisY {yScale} {width} {margin} />

    <g class="inner-chart" transform="translate({margin.left}, {margin.top})">
      {#each data.sort((a, b) => a.grade - b.grade) as d, index}
        <circle
          in:fly={{ x: -10, opacity: 0, duration: 500, delay: index * 30 }}
          cx={xScale(d.grade)}
          cy={yScale(d.hours)}
          fill="purple"
          stroke="black"
          r={hoveredData === d ? radius * 2 : radius}
          opacity={hoveredData ? (hoveredData === d ? 1 : 0.45) : 0.85}
          on:mouseover={() => (hoveredData = d)}
          on:focus={() => (hoveredData = d)}
          tabindex="0"
          role="button"
          aria-label="{d.name}: {d.grade}% grade, {d.hours} hours studied"
        />
      {/each}
    </g>
  </svg>

  {#if hoveredData}
    <Tooltip {xScale} {yScale} {width} data={hoveredData} />
  {/if}
</div>

<style>
  :global(.tick text, .axis-title) {
    font-weight: 400;
    font-size: 12px;
    fill: hsla(212, 10%, 53%, 1);
  }

  .chart-container {
    position: relative;
  }

  circle {
    transition: r 300ms ease, opacity 500ms ease;
    cursor: pointer;
  }

  h1 {
    margin: 0 0 0.5rem 0;
    font-size: 1.35rem;
    font-weight: 600;
  }
</style>
