<script>
  import { scaleLinear, scaleTime } from "d3-scale";
  import { max, extent } from "d3-array";
  import { line, area, curveMonotoneX } from "d3-shape";
  import { format } from "d3-format";
  import { fly, fade } from "svelte/transition";

  export let data = [];
  export let width = 400;
  export let height = 400;
  export let showArea = true;
  export let highlightYear = null;

  // Clean margins for better visual balance
  const margin = { top: 25, right: 90, bottom: 45, left: 60 };

  $: innerWidth = width - margin.left - margin.right;
  $: innerHeight = height - margin.top - margin.bottom;

  $: xScale = scaleLinear()
    .domain(extent(data, d => d.year))
    .range([0, innerWidth]);

  $: yScale = scaleLinear()
    .domain([0, max(data, d => d.cumulativeLivesSaved) * 1.1])
    .range([innerHeight, 0]);

  $: linePath = line()
    .x(d => xScale(d.year))
    .y(d => yScale(d.cumulativeLivesSaved))
    .curve(curveMonotoneX);

  $: areaPath = area()
    .x(d => xScale(d.year))
    .y0(innerHeight)
    .y1(d => yScale(d.cumulativeLivesSaved))
    .curve(curveMonotoneX);

  $: xTicks = data.filter(d => d.year % 10 === 0 || d.year === 2026 || d.year === 2070);
  $: yTicks = yScale.ticks(5);

  const formatNumber = format(",");

  let hoveredData = null;

  function handleMouseMove(event) {
    const rect = event.currentTarget.getBoundingClientRect();
    const x = event.clientX - rect.left - margin.left;
    const year = Math.round(xScale.invert(x));
    hoveredData = data.find(d => d.year === year) || null;
  }
</script>

<div class="chart-wrapper">
  <svg {width} {height}>
    <defs>
      <!-- Subtle gradient - not distracting (Tufte: let data speak) -->
      <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#1a7f4b;stop-opacity:0.2" />
        <stop offset="100%" style="stop-color:#1a7f4b;stop-opacity:0.03" />
      </linearGradient>
    </defs>

    <g transform="translate({margin.left}, {margin.top})">
      <!-- Y-axis grid lines - very subtle -->
      {#each yTicks as tick}
        <g class="tick" transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#f0f0f0" stroke-width="1" />
          <text x={-8} y={4} text-anchor="end" class="tick-label">
            {formatNumber(tick)}
          </text>
        </g>
      {/each}

      <!-- Y-axis label -->
      <text
        class="axis-label"
        transform="rotate(-90)"
        x={-innerHeight / 2}
        y={-45}
        text-anchor="middle"
      >
        Cumulative lives saved
      </text>

      <!-- Area fill -->
      {#if showArea}
        <path
          d={areaPath(data)}
          fill="url(#areaGradient)"
          class="area"
        />
      {/if}

      <!-- Line - clean stroke -->
      <path
        d={linePath(data)}
        fill="none"
        stroke="#1a7f4b"
        stroke-width="2.5"
        class="line"
      />

      <!-- Data points - minimal, only show on hover -->
      {#each data as d}
        <circle
          cx={xScale(d.year)}
          cy={yScale(d.cumulativeLivesSaved)}
          r={hoveredData === d || d.year === highlightYear ? 5 : 0}
          fill="white"
          stroke="#1a7f4b"
          stroke-width="2"
          class="data-point"
        />
      {/each}

      <!-- X-axis - minimal ticks -->
      <g transform="translate(0, {innerHeight})">
        {#each xTicks as d}
          <g transform="translate({xScale(d.year)}, 0)">
            <line y1={0} y2={4} stroke="#ccc" />
            <text y={18} text-anchor="middle" class="tick-label">
              {d.year}
            </text>
          </g>
        {/each}
      </g>

      <!-- Final value annotation - direct labeling (Tufte principle) -->
      {#if data.length > 0}
        {@const lastPoint = data[data.length - 1]}
        <g transform="translate({xScale(lastPoint.year)}, {yScale(lastPoint.cumulativeLivesSaved)})">
          <circle r="4" fill="#1a7f4b" />
          <text
            x={8}
            y={4}
            text-anchor="start"
            class="annotation"
          >
            {formatNumber(lastPoint.cumulativeLivesSaved)} lives saved
          </text>
        </g>
      {/if}

      <!-- Hover interaction layer -->
      <rect
        x={0}
        y={0}
        width={innerWidth}
        height={innerHeight}
        fill="transparent"
        role="presentation"
        on:mousemove={handleMouseMove}
        on:mouseleave={() => hoveredData = null}
      />

      <!-- Hover indicator - subtle -->
      {#if hoveredData}
        <g transform="translate({xScale(hoveredData.year)}, 0)">
          <line
            y1={0}
            y2={innerHeight}
            stroke="#1a7f4b"
            stroke-dasharray="3,3"
            opacity="0.35"
          />
        </g>
      {/if}
    </g>
  </svg>

  {#if hoveredData}
    <div class="tooltip" transition:fade={{ duration: 100 }}>
      <div class="tooltip-year">{hoveredData.year}</div>
      <div class="tooltip-stat">
        <span class="tooltip-value">{formatNumber(hoveredData.cumulativeLivesSaved)}</span>
        <span class="tooltip-label">lives saved</span>
      </div>
      <div class="tooltip-secondary">
        {formatNumber(hoveredData.girlsVaccinated)} girls vaccinated
      </div>
    </div>
  {/if}
</div>

<style>
  .chart-wrapper {
    position: relative;
  }

  .line {
    transition: opacity 200ms ease;
  }

  .area {
    transition: opacity 200ms ease;
  }

  .data-point {
    transition: r 150ms ease;
    cursor: pointer;
  }

  .tick-label {
    font-size: 10px;
    fill: #888;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .axis-label {
    font-size: 10px;
    fill: #777;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .annotation {
    font-size: 12px;
    fill: #1a7f4b;
    font-weight: 600;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  /* NYT-style tooltip */
  .tooltip {
    position: absolute;
    top: 8px;
    right: 8px;
    background: white;
    padding: 10px 14px;
    border-radius: 2px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.12);
    pointer-events: none;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    border: 1px solid #eee;
  }

  .tooltip-year {
    font-size: 11px;
    color: #888;
    margin-bottom: 4px;
  }

  .tooltip-stat {
    display: flex;
    align-items: baseline;
    gap: 4px;
  }

  .tooltip-value {
    font-size: 16px;
    font-weight: 600;
    color: #1a7f4b;
  }

  .tooltip-label {
    font-size: 12px;
    color: #666;
  }

  .tooltip-secondary {
    font-size: 11px;
    color: #888;
    margin-top: 4px;
  }
</style>
