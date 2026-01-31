<script>
  import { scaleBand, scaleLinear } from "d3-scale";
  import { fly } from "svelte/transition";

  export let width = 400;
  export let height = 300;
  export let animate = false;

  const data = [
    { period: "Investment", value: 1, label: "$1", isInvestment: true },
    { period: "30-year return", value: 19, label: "$19", isInvestment: false },
    { period: "50-year return", value: 61.32, label: "$61", isInvestment: false }
  ];

  const margin = { top: 50, right: 30, bottom: 60, left: 50 };

  $: innerWidth = width - margin.left - margin.right;
  $: innerHeight = height - margin.top - margin.bottom;

  $: xScale = scaleBand()
    .domain(data.map(d => d.period))
    .range([0, innerWidth])
    .padding(0.3);

  $: yScale = scaleLinear()
    .domain([0, 70])
    .range([innerHeight, 0]);

  $: yTicks = [0, 20, 40, 60];
</script>

<div class="chart-wrapper">
  <div class="chart-title">Return on Investment</div>
  <div class="chart-subtitle">For every $1 invested in HPV vaccination</div>

  <svg {width} {height}>
    <g transform="translate({margin.left}, {margin.top})">
      <!-- Y-axis grid lines -->
      {#each yTicks as tick}
        <g transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#e5e7eb" />
          <text x={-10} y={4} text-anchor="end" class="tick-label">
            ${tick}
          </text>
        </g>
      {/each}

      <!-- Bars -->
      {#each data as d, i}
        <g transform="translate({xScale(d.period)}, 0)">
          {#if animate}
            <rect
              in:fly={{ y: innerHeight - yScale(d.value), duration: 600, delay: i * 200 }}
              y={yScale(d.value)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.value)}
              fill={d.isInvestment ? "#94a3b8" : "#16a34a"}
              rx="4"
            />
          {:else}
            <rect
              y={yScale(d.value)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.value)}
              fill={d.isInvestment ? "#94a3b8" : "#16a34a"}
              rx="4"
            />
          {/if}

          <!-- Value label -->
          <text
            x={xScale.bandwidth() / 2}
            y={yScale(d.value) - 10}
            text-anchor="middle"
            class="value-label"
            class:highlight={!d.isInvestment}
          >
            {d.label}
          </text>

          <!-- X-axis label -->
          <text
            x={xScale.bandwidth() / 2}
            y={innerHeight + 20}
            text-anchor="middle"
            class="x-label"
          >
            {d.period}
          </text>
        </g>
      {/each}

      <!-- Arrow annotation -->
      <g transform="translate({xScale('Investment') + xScale.bandwidth()}, {yScale(1) - 30})">
        <path
          d="M 10,0 L {xScale('30-year return') - xScale('Investment') - xScale.bandwidth() - 20},0"
          stroke="#16a34a"
          stroke-width="2"
          fill="none"
          marker-end="url(#arrowhead)"
        />
      </g>

      <!-- Arrow marker -->
      <defs>
        <marker
          id="arrowhead"
          markerWidth="10"
          markerHeight="7"
          refX="9"
          refY="3.5"
          orient="auto"
        >
          <polygon
            points="0 0, 10 3.5, 0 7"
            fill="#16a34a"
          />
        </marker>
      </defs>
    </g>
  </svg>

  <div class="callout">
    HPV vaccination delivers <strong>exceptional returns</strong>: preventing expensive late-stage cancer care,
    reducing catastrophic health expenditures for families, and preserving women's economic contribution.
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

  .value-label {
    font-size: 16px;
    fill: #666;
    font-family: Georgia, 'Times New Roman', serif;
    font-weight: 600;
  }

  .value-label.highlight {
    fill: #16a34a;
    font-size: 18px;
  }

  .x-label {
    font-size: 12px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  rect {
    transition: opacity 200ms ease;
  }

  rect:hover {
    opacity: 0.85;
  }

  .callout {
    margin-top: 15px;
    padding: 12px 16px;
    background: #f0fdf4;
    border-left: 4px solid #16a34a;
    border-radius: 4px;
    font-family: system-ui, sans-serif;
    font-size: 14px;
    color: #333;
    line-height: 1.5;
  }

  .callout strong {
    color: #16a34a;
  }
</style>
