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

  const margin = { top: 30, right: 100, bottom: 50, left: 70 };

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
      <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#22c55e;stop-opacity:0.4" />
        <stop offset="100%" style="stop-color:#22c55e;stop-opacity:0.05" />
      </linearGradient>
    </defs>

    <g transform="translate({margin.left}, {margin.top})">
      <!-- Y-axis grid lines -->
      {#each yTicks as tick}
        <g class="tick" transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#e5e7eb" />
          <text x={-10} y={4} text-anchor="end" class="tick-label">
            {formatNumber(tick)}
          </text>
        </g>
      {/each}

      <!-- Y-axis label -->
      <text
        class="axis-label"
        transform="rotate(-90)"
        x={-innerHeight / 2}
        y={-55}
        text-anchor="middle"
      >
        Cumulative Lives Saved
      </text>

      <!-- Area fill -->
      {#if showArea}
        <path
          d={areaPath(data)}
          fill="url(#areaGradient)"
          class="area"
        />
      {/if}

      <!-- Line -->
      <path
        d={linePath(data)}
        fill="none"
        stroke="#16a34a"
        stroke-width="3"
        class="line"
      />

      <!-- Data points -->
      {#each data as d, i}
        <circle
          cx={xScale(d.year)}
          cy={yScale(d.cumulativeLivesSaved)}
          r={hoveredData === d || d.year === highlightYear ? 7 : 4}
          fill={d.year === highlightYear ? "#16a34a" : "white"}
          stroke="#16a34a"
          stroke-width="2"
          class="data-point"
        />
      {/each}

      <!-- X-axis -->
      <g transform="translate(0, {innerHeight})">
        {#each xTicks as d}
          <g transform="translate({xScale(d.year)}, 0)">
            <line y1={0} y2={6} stroke="#999" />
            <text y={20} text-anchor="middle" class="tick-label">
              {d.year}
            </text>
          </g>
        {/each}

        <!-- X-axis label -->
        <text
          class="axis-label"
          x={innerWidth / 2}
          y={45}
          text-anchor="middle"
        >
          Year
        </text>
      </g>

      <!-- Final value annotation -->
      {#if data.length > 0}
        {@const lastPoint = data[data.length - 1]}
        <g transform="translate({xScale(lastPoint.year)}, {yScale(lastPoint.cumulativeLivesSaved)})">
          <text
            x={-10}
            y={-15}
            text-anchor="end"
            class="annotation"
          >
            {formatNumber(lastPoint.cumulativeLivesSaved)} lives
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

      <!-- Hover indicator -->
      {#if hoveredData}
        <g transform="translate({xScale(hoveredData.year)}, 0)">
          <line
            y1={0}
            y2={innerHeight}
            stroke="#16a34a"
            stroke-dasharray="4,4"
            opacity="0.5"
          />
        </g>
      {/if}
    </g>
  </svg>

  {#if hoveredData}
    <div class="tooltip" transition:fade={{ duration: 150 }}>
      <strong>{hoveredData.year}</strong><br/>
      Lives saved: <span class="highlight">{formatNumber(hoveredData.cumulativeLivesSaved)}</span><br/>
      Girls vaccinated: {formatNumber(hoveredData.girlsVaccinated)}
    </div>
  {/if}
</div>

<style>
  .chart-wrapper {
    position: relative;
  }

  .line {
    transition: all 300ms ease;
  }

  .area {
    transition: all 300ms ease;
  }

  .data-point {
    transition: r 200ms ease;
    cursor: pointer;
  }

  .tick-label {
    font-size: 11px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .axis-label {
    font-size: 12px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .annotation {
    font-size: 13px;
    fill: #16a34a;
    font-weight: 600;
    font-family: system-ui, sans-serif;
  }

  .tooltip {
    position: absolute;
    top: 10px;
    right: 10px;
    background: white;
    padding: 12px 16px;
    border-radius: 6px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    font-size: 14px;
    pointer-events: none;
    font-family: system-ui, sans-serif;
    line-height: 1.5;
  }

  .tooltip .highlight {
    color: #16a34a;
    font-weight: 600;
  }
</style>
