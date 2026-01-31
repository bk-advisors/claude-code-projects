<script>
  import { scaleBand, scaleLinear } from "d3-scale";
  import { max } from "d3-array";

  export let width = 400;
  export let height = 250;

  const data = [
    { country: "Papua New Guinea", incidence: 34.9, mortality: 19.9 },
    { country: "Australia", incidence: 6.4, mortality: 1.7 }
  ];

  // Clean margins
  const margin = { top: 35, right: 30, bottom: 40, left: 130 };

  $: innerWidth = width - margin.left - margin.right;
  $: innerHeight = height - margin.top - margin.bottom;

  $: yScale = scaleBand()
    .domain(data.map(d => d.country))
    .range([0, innerHeight])
    .padding(0.3);

  $: xScale = scaleLinear()
    .domain([0, max(data, d => Math.max(d.incidence, d.mortality)) * 1.2])
    .range([0, innerWidth]);

  $: xTicks = xScale.ticks(5);

  let hoveredData = null;
  let hoveredType = null;
</script>

<div class="chart-wrapper">
  <div class="chart-title">PNG vs Australia: Cervical Cancer Rates</div>
  <div class="chart-subtitle">Per 100,000 women, 2022</div>

  <svg {width} {height}>
    <g transform="translate({margin.left}, {margin.top})">
      <!-- X-axis grid lines - subtle -->
      {#each xTicks as tick}
        <g transform="translate({xScale(tick)}, 0)">
          <line y1={0} y2={innerHeight} stroke="#f0f0f0" />
          <text y={innerHeight + 14} text-anchor="middle" class="tick-label">
            {tick}
          </text>
        </g>
      {/each}

      <!-- Bars -->
      {#each data as d}
        <g transform="translate(0, {yScale(d.country)})">
          <!-- Country label -->
          <text
            x={-10}
            y={yScale.bandwidth() / 2}
            dy="0.35em"
            text-anchor="end"
            class="country-label"
            class:png={d.country === "Papua New Guinea"}
          >
            {d.country}
          </text>

          <!-- Incidence bar - muted colors -->
          <rect
            x={0}
            y={0}
            width={xScale(d.incidence)}
            height={yScale.bandwidth() / 2 - 2}
            fill={d.country === "Papua New Guinea" ? "#e8a5a5" : "#a8c8e8"}
            rx="1"
            role="img"
            aria-label="{d.country} incidence: {d.incidence} per 100,000"
            on:mouseenter={() => { hoveredData = d; hoveredType = 'incidence'; }}
            on:mouseleave={() => { hoveredData = null; hoveredType = null; }}
          />

          <!-- Mortality bar - stronger colors for emphasis -->
          <rect
            x={0}
            y={yScale.bandwidth() / 2 + 2}
            width={xScale(d.mortality)}
            height={yScale.bandwidth() / 2 - 2}
            fill={d.country === "Papua New Guinea" ? "#c41d3a" : "#4a7eb8"}
            rx="1"
            role="img"
            aria-label="{d.country} mortality: {d.mortality} per 100,000"
            on:mouseenter={() => { hoveredData = d; hoveredType = 'mortality'; }}
            on:mouseleave={() => { hoveredData = null; hoveredType = null; }}
          />

          <!-- Value labels -->
          <text
            x={xScale(d.incidence) + 5}
            y={yScale.bandwidth() / 4}
            dy="0.35em"
            class="value-label"
          >
            {d.incidence}
          </text>
          <text
            x={xScale(d.mortality) + 5}
            y={yScale.bandwidth() * 3 / 4}
            dy="0.35em"
            class="value-label"
          >
            {d.mortality}
          </text>
        </g>
      {/each}
    </g>
  </svg>

  <!-- Legend -->
  <div class="legend">
    <div class="legend-item">
      <span class="legend-color incidence"></span>
      <span>Incidence (new cases)</span>
    </div>
    <div class="legend-item">
      <span class="legend-color mortality"></span>
      <span>Mortality (deaths)</span>
    </div>
  </div>

  <!-- Comparison callout -->
  <div class="callout">
    PNG's incidence rate is <strong>5.5x higher</strong> than Australia's.<br/>
    Its mortality rate is <strong>11.7x higher</strong>.
  </div>
</div>

<style>
  .chart-wrapper {
    position: relative;
  }

  .chart-title {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1rem;
    font-weight: 600;
    text-align: left;
    color: #1a1a1a;
    margin-bottom: 2px;
    letter-spacing: -0.01em;
  }

  .chart-subtitle {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 0.8rem;
    color: #777;
    text-align: left;
    margin-bottom: 12px;
  }

  .tick-label {
    font-size: 10px;
    fill: #888;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .country-label {
    font-size: 12px;
    fill: #666;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .country-label.png {
    fill: #c41d3a;
    font-weight: 600;
  }

  .value-label {
    font-size: 10px;
    fill: #666;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  rect {
    transition: opacity 200ms ease;
    cursor: pointer;
  }

  rect:hover {
    opacity: 0.75;
  }

  /* Cleaner legend */
  .legend {
    display: flex;
    justify-content: flex-start;
    gap: 18px;
    margin-top: 8px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 11px;
    color: #777;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .legend-color {
    width: 12px;
    height: 12px;
    border-radius: 1px;
  }

  .legend-color.incidence {
    background: linear-gradient(to right, #e8a5a5, #a8c8e8);
  }

  .legend-color.mortality {
    background: linear-gradient(to right, #c41d3a, #4a7eb8);
  }

  /* Refined callout */
  .callout {
    margin-top: 16px;
    padding: 10px 14px;
    background: #fdf6f6;
    border-left: 3px solid #c41d3a;
    border-radius: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    color: #555;
    line-height: 1.5;
  }

  .callout strong {
    color: #c41d3a;
    font-weight: 600;
  }
</style>
