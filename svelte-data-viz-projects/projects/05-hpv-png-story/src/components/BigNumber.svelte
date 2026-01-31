<script>
  import { fly } from "svelte/transition";

  export let number = "";
  export let label = "";
  export let color = "#c41d3a";
  export let size = "large";
  export let animate = true;
</script>

<div
  class="big-number"
  class:large={size === "large"}
  class:medium={size === "medium"}
  class:small={size === "small"}
>
  {#if animate}
    <span class="number" style="color: {color}" in:fly={{ y: 15, duration: 400 }}>
      {number}
    </span>
  {:else}
    <span class="number" style="color: {color}">
      {number}
    </span>
  {/if}
  <span class="label">{label}</span>
</div>

<style>
  .big-number {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 1.25rem 1rem;
  }

  .number {
    font-family: Georgia, 'Times New Roman', serif;
    font-weight: 600;
    line-height: 1;
    margin-bottom: 0.6rem;
    letter-spacing: -0.02em;
  }

  .large .number {
    font-size: 3.5rem;
  }

  .medium .number {
    font-size: 2.75rem;
  }

  .small .number {
    font-size: 2rem;
  }

  .label {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 0.95rem;
    color: #666;
    max-width: 280px;
    line-height: 1.45;
  }

  .large .label {
    font-size: 1rem;
  }

  .medium .label {
    font-size: 0.95rem;
  }

  .small .label {
    font-size: 0.85rem;
  }
</style>
