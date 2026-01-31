<script>
  export let colorScale;

  const steps = [0, 250000000, 500000000, 750000000, 1000000000, 1400000000];

  function formatNumber(n) {
    if (n >= 1000000000) return (n / 1000000000).toFixed(1) + 'B';
    if (n >= 1000000) return (n / 1000000).toFixed(0) + 'M';
    return n.toString();
  }
</script>

<div class="legend">
  <p class="title">Population</p>
  <div class="scale">
    {#each steps as step, i}
      {#if i < steps.length - 1}
        <div class="step">
          <div
            class="color"
            style="background: {colorScale(step)}"
          />
          <span>{formatNumber(step)}</span>
        </div>
      {/if}
    {/each}
  </div>
</div>

<style>
  .legend {
    position: absolute;
    bottom: 20px;
    left: 20px;
    background: rgba(0, 0, 0, 0.7);
    padding: 10px 15px;
    border-radius: 8px;
    color: white;
  }

  .title {
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 8px;
  }

  .scale {
    display: flex;
    gap: 2px;
  }

  .step {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 0.65rem;
  }

  .color {
    width: 25px;
    height: 10px;
  }

  span {
    margin-top: 3px;
    opacity: 0.8;
  }
</style>
