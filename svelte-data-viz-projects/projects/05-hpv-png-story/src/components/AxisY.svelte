<script>
  export let width;
  export let yScale;
  export let margin;
  export let label = "";
  export let formatTick = (d) => d;

  $: yTicks = yScale.ticks ? yScale.ticks(5) : yScale.domain();
</script>

<g class="axis y" transform="translate({margin.left}, {margin.top})">
  {#each yTicks as tick, index}
    <g class="tick" transform="translate(0, {yScale(tick)})">
      <line
        x1={0}
        x2={width - margin.left - margin.right}
        y1={0}
        y2={0}
        stroke={index === 0 ? '#999' : '#e5e7eb'}
      />
      <text y={-4} x={-5} text-anchor="end">
        {formatTick(tick)}
      </text>
    </g>
  {/each}
  {#if label}
    <text
      class="axis-title"
      transform="rotate(-90)"
      x={-margin.top}
      y={-margin.left + 15}
      text-anchor="end"
    >
      {label}
    </text>
  {/if}
</g>
