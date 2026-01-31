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

  const margin = { top: 30, right: 20, bottom: 110, left: 50 };

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
      <!-- Y-axis grid lines -->
      {#each yTicks as tick}
        <g class="tick" transform="translate(0, {yScale(tick)})">
          <line x1={0} x2={innerWidth} stroke="#e5e7eb" />
          <text x={-8} y={4} text-anchor="end" class="tick-label">
            {tick}
          </text>
        </g>
      {/each}

      <!-- Y-axis label -->
      <text
        class="axis-label"
        transform="rotate(-90)"
        x={-innerHeight / 2}
        y={-40}
        text-anchor="middle"
      >
        Deaths per 100,000 women
      </text>

      <!-- Bars -->
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
              in:fly={{ y: innerHeight - yScale(d.rate), duration: 600, delay: i * 50 }}
              y={yScale(d.rate)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.rate)}
              fill={isHighlighted(d) ? "#dc2626" : "#94a3b8"}
              rx="2"
              class:highlighted={isHighlighted(d)}
            />
          {:else}
            <rect
              y={yScale(d.rate)}
              width={xScale.bandwidth()}
              height={innerHeight - yScale(d.rate)}
              fill={isHighlighted(d) ? "#dc2626" : "#94a3b8"}
              rx="2"
              class:highlighted={isHighlighted(d)}
            />
          {/if}

          <!-- Value label on top of bar -->
          <text
            x={xScale.bandwidth() / 2}
            y={yScale(d.rate) - 5}
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
    transition: fill 300ms ease, opacity 300ms ease;
    cursor: pointer;
  }

  rect:hover {
    opacity: 0.8;
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

  .country-label {
    font-size: 11px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .country-label.highlighted {
    fill: #dc2626;
    font-weight: 600;
  }

  .value-label {
    font-size: 11px;
    fill: #666;
    font-family: system-ui, sans-serif;
  }

  .value-label.highlighted {
    fill: #dc2626;
    font-weight: 600;
  }

  .tooltip {
    position: absolute;
    top: 10px;
    right: 10px;
    background: white;
    padding: 10px 14px;
    border-radius: 6px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    font-size: 14px;
    pointer-events: none;
    font-family: system-ui, sans-serif;
  }
</style>
