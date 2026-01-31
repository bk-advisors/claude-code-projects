<script>
  export let width;
  export let yScale;
  export let margin;
  export let label = "Hours Studied";

  $: yTicks = yScale.ticks ? yScale.ticks(4) : yScale.domain();
</script>

<g class="axis y" transform="translate(0, {margin.top})">
  {#each yTicks as tick, index}
    <g class="tick" transform="translate(0, {yScale(tick)})">
      <line
        x1={0}
        x2={width}
        y1={0}
        y2={0}
        stroke={index === 0 ? '#999' : '#e5e7eb'}
      />
      <text y={-3}>
        {index === yTicks.length - 1 ? `${tick} ${label}` : tick}
      </text>
    </g>
  {/each}
</g>
