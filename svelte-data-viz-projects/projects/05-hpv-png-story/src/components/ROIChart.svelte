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

  // Clean margins
  const margin = { top: 45, right: 25, bottom: 55, left: 45 };

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
      <!-- Y-axis grid lines - subtle -->
      {#each yTicks as tick}
        <g transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#f0f0f0" />
          <text x={-8} y={4} text-anchor="end" class="tick-label">
            ${tick}
          </text>
        </g>
      {/each}

      <!-- Bars - clean styling -->
      {#each data as d, i}
        <g transform="translate({xScale(d.period)}, 0)">
          {#if animate}
            <rect
              in:fly={{ y: innerHeight - yScale(d.value), duration: 500, delay: i * 150 }}
              y={yScale(d.value)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.value)}
              fill={d.isInvestment ? "#c4c9cf" : "#1a7f4b"}
              rx="2"
            />
          {:else}
            <rect
              y={yScale(d.value)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.value)}
              fill={d.isInvestment ? "#c4c9cf" : "#1a7f4b"}
              rx="2"
            />
          {/if}

          <!-- Value label - direct labeling -->
          <text
            x={xScale.bandwidth() / 2}
            y={yScale(d.value) - 8}
            text-anchor="middle"
            class="value-label"
            class:highlight={!d.isInvestment}
          >
            {d.label}
          </text>

          <!-- X-axis label -->
          <text
            x={xScale.bandwidth() / 2}
            y={innerHeight + 18}
            text-anchor="middle"
            class="x-label"
          >
            {d.period}
          </text>
        </g>
      {/each}

      <!-- Arrow annotation - subtle -->
      <g transform="translate({xScale('Investment') + xScale.bandwidth()}, {yScale(1) - 25})">
        <path
          d="M 8,0 L {xScale('30-year return') - xScale('Investment') - xScale.bandwidth() - 16},0"
          stroke="#1a7f4b"
          stroke-width="1.5"
          fill="none"
          marker-end="url(#arrowhead)"
          opacity="0.6"
        />
      </g>

      <!-- Arrow marker -->
      <defs>
        <marker
          id="arrowhead"
          markerWidth="8"
          markerHeight="6"
          refX="7"
          refY="3"
          orient="auto"
        >
          <polygon
            points="0 0, 8 3, 0 6"
            fill="#1a7f4b"
            opacity="0.6"
          />
        </marker>
      </defs>
    </g>
  </svg>

  <div class="callout">
    HPV vaccination delivers <strong>substantial returns</strong>: preventing expensive late-stage cancer care,
    reducing catastrophic health expenditures for families, and preserving women's economic contribution.
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

  .value-label {
    font-size: 14px;
    fill: #777;
    font-family: Georgia, 'Times New Roman', serif;
    font-weight: 600;
  }

  .value-label.highlight {
    fill: #1a7f4b;
    font-size: 16px;
  }

  .x-label {
    font-size: 10px;
    fill: #666;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  rect {
    transition: opacity 200ms ease;
  }

  rect:hover {
    opacity: 0.8;
  }

  /* Refined callout */
  .callout {
    margin-top: 16px;
    padding: 10px 14px;
    background: #f4faf7;
    border-left: 3px solid #1a7f4b;
    border-radius: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    color: #555;
    line-height: 1.5;
  }

  .callout strong {
    color: #1a7f4b;
    font-weight: 600;
  }
</style>
