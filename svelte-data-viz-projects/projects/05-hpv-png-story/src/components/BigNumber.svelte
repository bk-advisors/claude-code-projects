<script>
  import { fly } from "svelte/transition";

  export let number = "";
  export let label = "";
  export let color = "#dc2626";
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
    <span class="number" style="color: {color}" in:fly={{ y: 20, duration: 500 }}>
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
    padding: 1rem;
  }

  .number {
    font-family: Georgia, 'Times New Roman', serif;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 0.5rem;
  }

  .large .number {
    font-size: 4rem;
  }

  .medium .number {
    font-size: 3rem;
  }

  .small .number {
    font-size: 2rem;
  }

  .label {
    font-family: system-ui, sans-serif;
    font-size: 1rem;
    color: #666;
    max-width: 250px;
    line-height: 1.4;
  }

  .large .label {
    font-size: 1.1rem;
  }

  .medium .label {
    font-size: 1rem;
  }

  .small .label {
    font-size: 0.9rem;
  }
</style>
