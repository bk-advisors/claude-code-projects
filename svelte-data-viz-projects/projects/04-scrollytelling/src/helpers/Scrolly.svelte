<script>
  // Russell Samora's Scrolly component for Svelte
  // https://twitter.com/russellviz/status/1432774653139984387
  import { onMount } from "svelte";

  export let value = undefined;
  export let root = null;
  export let offset = 0.5; // 0 = top of viewport, 1 = bottom, 0.5 = middle
  export let threshold = 0;

  let steps = [];
  let container;

  const handleIntersect = (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const index = steps.indexOf(entry.target);
        if (index !== -1) {
          value = index;
        }
      }
    });
  };

  onMount(() => {
    // Calculate rootMargin to create a trigger line at the offset position
    // Negative margins shrink the intersection area
    const topMargin = -offset * 100;
    const bottomMargin = -(1 - offset) * 100;

    const options = {
      root,
      rootMargin: `${topMargin}% 0px ${bottomMargin}% 0px`,
      threshold,
    };

    const observer = new IntersectionObserver(handleIntersect, options);

    steps = Array.from(container.querySelectorAll(":scope > *"));
    steps.forEach((step) => observer.observe(step));

    return () => observer.disconnect();
  });
</script>

<div bind:this={container}>
  <slot />
</div>
