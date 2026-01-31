<script>
  import { onMount } from "svelte";

  export let value = undefined;
  export let root = null;
  export let offset = 0.5;
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
