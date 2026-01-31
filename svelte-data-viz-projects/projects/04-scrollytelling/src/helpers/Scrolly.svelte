<script>
  // Russell Samora's Scrolly component for Svelte
  // https://twitter.com/russellviz/status/1432774653139984387
  import { onMount } from "svelte";

  export let value = undefined;
  export let root = null;
  export let top = 0;
  export let bottom = 0;
  export let threshold = 0.5;

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
    const options = {
      root,
      rootMargin: `${top}px 0px ${bottom}px 0px`,
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
