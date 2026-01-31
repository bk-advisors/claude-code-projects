<script>
  export let height;
  export let width;
  export let xScale;
  export let margin;
  export let label = "";
  export let formatTick = (d) => d;

  $: xTicks = xScale.ticks ? xScale.ticks(5) : xScale.domain();
</script>

<g class="axis x" transform="translate(0, {height - margin.bottom})">
  {#each xTicks as tick, index}
    <g class="tick" transform="translate({xScale(tick)}, 0)">
      <line x1={0} x2={0} y1={0} y2={6} stroke="#999" />
      <text
        y={6}
        dy={14}
        text-anchor={index === 0 ? "start" : "middle"}
      >
        {formatTick(tick)}
      </text>
    </g>
  {/each}
  {#if label}
    <text
      class="axis-title"
      y={-9}
      x={width}
      text-anchor="end"
    >
      {label}
    </text>
  {/if}
</g>
