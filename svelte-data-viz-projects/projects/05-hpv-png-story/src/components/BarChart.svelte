<script>
  import { scaleBand, scaleLinear } from "d3-scale";
  import { max } from "d3-array";
  import { fly } from "svelte/transition";

  export let data = [];
  export let width = 400;
  export let height = 400;
  export let highlightCountry = null;
  export let showAll = true;
  export let animateIn = false;

  // Tufte-inspired margins: generous but purposeful
  const margin = { top: 25, right: 20, bottom: 100, left: 45 };

  $: innerWidth = width - margin.left - margin.right;
  $: innerHeight = height - margin.top - margin.bottom;

  $: displayData = showAll ? data : data.filter(d => d.highlight || d.country === highlightCountry);

  $: xScale = scaleBand()
    .domain(displayData.map(d => d.country))
    .range([0, innerWidth])
    .padding(0.2);

  $: yScale = scaleLinear()
    .domain([0, max(data, d => d.rate) * 1.1])
    .range([innerHeight, 0]);

  $: yTicks = yScale.ticks(5);

  function isHighlighted(d) {
    if (highlightCountry) {
      return d.country === highlightCountry;
    }
    return d.highlight;
  }

  let hoveredData = null;
</script>

<div class="chart-wrapper">
  <svg {width} {height}>
    <g transform="translate({margin.left}, {margin.top})">
      <!-- Y-axis grid lines - subtle (Tufte: minimize non-data ink) -->
      {#each yTicks as tick}
        <g class="tick" transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#f0f0f0" stroke-width="1" />
          <text x={-6} y={4} text-anchor="end" class="tick-label">
            {tick}
          </text>
        </g>
      {/each}

      <!-- Y-axis label - positioned cleanly -->
      <text
        class="axis-label"
        transform="rotate(-90)"
        x={-innerHeight / 2}
        y={-32}
        text-anchor="middle"
      >
        Deaths per 100,000
      </text>

      <!-- Bars - clean, direct labeling (Cairo: clarity first) -->
      {#each displayData as d, i}
        <g
          class="bar-group"
          transform="translate({xScale(d.country)}, 0)"
          role="img"
          aria-label="{d.country}: {d.rate} deaths per 100,000"
          on:mouseenter={() => hoveredData = d}
          on:mouseleave={() => hoveredData = null}
        >
          {#if animateIn}
            <rect
              in:fly={{ y: innerHeight - yScale(d.rate), duration: 500, delay: i * 40 }}
              y={yScale(d.rate)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.rate)}
              fill={isHighlighted(d) ? "#c41d3a" : "#c4c9cf"}
              rx="1"
              class:highlighted={isHighlighted(d)}
            />
          {:else}
            <rect
              y={yScale(d.rate)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.rate)}
              fill={isHighlighted(d) ? "#c41d3a" : "#c4c9cf"}
              rx="1"
              class:highlighted={isHighlighted(d)}
            />
          {/if}

          <!-- Value label - direct labeling (Tufte principle) -->
          <text
            x={xScale.bandwidth() / 2}
            y={yScale(d.rate) - 6}
            text-anchor="middle"
            class="value-label"
            class:highlighted={isHighlighted(d)}
          >
            {d.rate}
          </text>
        </g>
      {/each}

      <!-- X-axis labels -->
      <g transform="translate(0, {innerHeight})">
        {#each displayData as d}
          <g transform="translate({xScale(d.country) + xScale.bandwidth() / 2}, 0)">
            <text
              y={15}
              text-anchor="end"
              transform="rotate(-45)"
              class="country-label"
              class:highlighted={isHighlighted(d)}
            >
              {d.country}
            </text>
          </g>
        {/each}
      </g>
    </g>
  </svg>

  {#if hoveredData}
    <div class="tooltip" style="opacity: 1;">
      <strong>{hoveredData.country}</strong><br/>
      Mortality rate: {hoveredData.rate} per 100,000
    </div>
  {/if}
</div>

<style>
  .chart-wrapper {
    position: relative;
  }

  rect {
    transition: opacity 200ms ease;
    cursor: pointer;
  }

  rect:hover {
    opacity: 0.75;
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

  .country-label {
    font-size: 10px;
    fill: #666;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .country-label.highlighted {
    fill: #c41d3a;
    font-weight: 600;
  }

  .value-label {
    font-size: 10px;
    fill: #777;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  .value-label.highlighted {
    fill: #c41d3a;
    font-weight: 600;
  }

  /* Minimal tooltip - NYT style */
  .tooltip {
    position: absolute;
    top: 8px;
    right: 8px;
    background: white;
    padding: 8px 12px;
    border-radius: 2px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.12);
    font-size: 13px;
    pointer-events: none;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    border: 1px solid #eee;
  }
</style>
