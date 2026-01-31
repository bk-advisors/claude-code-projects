<script>
  import { fly } from "svelte/transition";

  export let data;
  export let xScale;
  export let yScale;
  export let xAccessor;
  export let yAccessor;
  export let width;

  $: x = xScale(xAccessor(data));
  $: y = yScale(yAccessor(data));

  let tooltipWidth;

  const xNudge = 15;
  const yNudge = 30;

  $: xPosition = x + tooltipWidth > width ? x - tooltipWidth - xNudge : x + xNudge;
  $: yPosition = y + yNudge;
</script>

<div
  class="tooltip"
  transition:fly={{ y: 10 }}
  style="position: absolute; top: {yPosition}px; left: {xPosition}px"
  bind:clientWidth={tooltipWidth}
>
  <h1>{data.name}</h1>
  <p><strong>Grade:</strong> {data.grade}%</p>
  <p><strong>Hours:</strong> {data.hours}</p>
</div>

<style>
  .tooltip {
    padding: 10px 12px;
    background: white;
    box-shadow: rgba(0, 0, 0, 0.15) 2px 3px 8px;
    border-radius: 4px;
    pointer-events: none;
    font-family: system-ui, sans-serif;
  }

  h1 {
    margin: 0 0 6px 0;
    font-size: 1rem;
    font-weight: 600;
  }

  p {
    margin: 0;
    font-size: 0.85rem;
    line-height: 1.4;
  }
</style>
