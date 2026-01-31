<script>
  import { fly, fade } from "svelte/transition";

  export let country;
  export let x;
  export let y;

  function formatPopulation(n) {
    if (!n) return 'N/A';
    return n.toLocaleString();
  }
</script>

<div
  class="tooltip"
  in:fly={{ y: 10, duration: 200 }}
  out:fade
  style="left: {x + 15}px; top: {y - 10}px;"
>
  <h1>{country.name || 'Unknown'}</h1>
  <p>Population: {formatPopulation(country.population)}</p>
</div>

<style>
  .tooltip {
    position: absolute;
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: rgba(0, 0, 0, 0.25) 2px 3px 10px;
    border-radius: 5px;
    pointer-events: none;
    z-index: 100;
  }

  h1 {
    margin: 0 0 4px 0;
    font-size: 0.95rem;
    font-weight: 600;
  }

  p {
    margin: 0;
    font-size: 0.8rem;
    color: #555;
  }
</style>
