<script>
  import { scaleBand, scaleLinear } from "d3-scale";
  import { max } from "d3-array";

  export let width = 400;
  export let height = 250;

  const data = [
    { country: "Papua New Guinea", incidence: 34.9, mortality: 19.9 },
    { country: "Australia", incidence: 6.4, mortality: 1.7 }
  ];

  const margin = { top: 40, right: 30, bottom: 50, left: 140 };

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
  <div class="chart-subtitle">Per 100,000 women</div>

  <svg {width} {height}>
    <g transform="translate({margin.left}, {margin.top})">
      <!-- X-axis grid lines -->
      {#each xTicks as tick}
        <g transform="translate({xScale(tick)}, 0)">
          <line y1={0} y2={innerHeight} stroke="#e5e7eb" />
          <text y={innerHeight + 15} text-anchor="middle" class="tick-label">
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

          <!-- Incidence bar -->
          <rect
            x={0}
            y={0}
            width={xScale(d.incidence)}
            height={yScale.bandwidth() / 2 - 2}
            fill={d.country === "Papua New Guinea" ? "#fca5a5" : "#93c5fd"}
            rx="2"
            role="img"
            aria-label="{d.country} incidence: {d.incidence} per 100,000"
            on:mouseenter={() => { hoveredData = d; hoveredType = 'incidence'; }}
            on:mouseleave={() => { hoveredData = null; hoveredType = null; }}
          />

          <!-- Mortality bar -->
          <rect
            x={0}
            y={yScale.bandwidth() / 2 + 2}
            width={xScale(d.mortality)}
            height={yScale.bandwidth() / 2 - 2}
            fill={d.country === "Papua New Guinea" ? "#dc2626" : "#3b82f6"}
            rx="2"
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
    font-size: 1.1rem;
    font-weight: 600;
    text-align: center;
    color: #333;
    margin-bottom: 4px;
  }

  .chart-subtitle {
    font-family: system-ui, sans-serif;
    font-size: 0.85rem;
    color: #666;
    text-align: center;
    margin-bottom: 10px;
  }

  .tick-label {
    font-size: 11px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .country-label {
    font-size: 13px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .country-label.png {
    fill: #dc2626;
    font-weight: 600;
  }

  .value-label {
    font-size: 11px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  rect {
    transition: opacity 200ms ease;
    cursor: pointer;
  }

  rect:hover {
    opacity: 0.8;
  }

  .legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 10px;
    font-family: system-ui, sans-serif;
    font-size: 12px;
    color: #666;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .legend-color {
    width: 14px;
    height: 14px;
    border-radius: 2px;
  }

  .legend-color.incidence {
    background: linear-gradient(to right, #fca5a5, #93c5fd);
  }

  .legend-color.mortality {
    background: linear-gradient(to right, #dc2626, #3b82f6);
  }

  .callout {
    margin-top: 15px;
    padding: 12px 16px;
    background: #fef2f2;
    border-left: 4px solid #dc2626;
    border-radius: 4px;
    font-family: system-ui, sans-serif;
    font-size: 14px;
    color: #333;
    line-height: 1.5;
  }

  .callout strong {
    color: #dc2626;
  }
</style>
