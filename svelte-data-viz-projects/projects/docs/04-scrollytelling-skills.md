# Scrollytelling Skills

## Project: NYT-Style Scrollytelling Article

A narrative visualization that reveals insights progressively as the user scrolls.

## Key Skills Learned

### 1. Scrolly Component (Intersection Observer)

**Russell Samora's Scrolly pattern:**
```svelte
<!-- Scrolly.svelte -->
<script>
  import { onMount } from "svelte";

  export let value = undefined;
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
    const observer = new IntersectionObserver(handleIntersect, {
      threshold
    });

    steps = Array.from(container.querySelectorAll(":scope > *"));
    steps.forEach((step) => observer.observe(step));

    return () => observer.disconnect();
  });
</script>

<div bind:this={container}>
  <slot />
</div>
```

**Usage:**
```svelte
<script>
  let currentStep;
</script>

<Scrolly bind:value={currentStep}>
  {#each steps as step, i}
    <div class="step" class:active={currentStep === i}>
      {step.text}
    </div>
  {/each}
</Scrolly>
```

### 2. Sticky Chart Pattern

**Layout structure:**
```svelte
<section>
  <div class="sticky">
    <!-- Chart stays fixed while scrolling -->
    <div class="chart-container">
      <svg>...</svg>
    </div>
  </div>

  <div class="steps">
    <!-- Steps scroll over the chart -->
    <Scrolly bind:value={currentStep}>
      ...
    </Scrolly>
  </div>
</section>
```

**CSS for sticky behavior:**
```css
section {
  position: relative;
}

.sticky {
  position: sticky;
  top: 10vh;
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.steps {
  position: relative;
  z-index: 2; /* Steps appear above chart */
  pointer-events: none; /* Allow clicking through to chart */
}

.step {
  height: 90vh; /* Each step is nearly full screen */
  opacity: 0.3;
  transition: opacity 300ms ease;
}

.step.active {
  opacity: 1;
}

.step-content {
  pointer-events: auto; /* Re-enable clicks on step text */
}
```

### 3. Step Configuration

**Data-driven story structure:**
```javascript
const steps = [
  {
    text: "Introduction text...",
    highlight: null, // No highlighting
    xAccessor: d => d.grade,
    yAccessor: d => d.hours
  },
  {
    text: "Focusing on low performers...",
    highlight: d => d.hours < 20, // Predicate function
    xAccessor: d => d.grade,
    yAccessor: d => d.hours
  },
  {
    text: "Looking at top performers...",
    highlight: d => d.hours >= 40,
    xAccessor: d => d.grade,
    yAccessor: d => d.hours
  },
  // More steps...
];

$: currentConfig = steps[currentStep] || steps[0];
```

### 4. Conditional Highlighting

**Apply styles based on step configuration:**
```svelte
<script>
  function isHighlighted(d) {
    if (!currentConfig.highlight) return true;
    return currentConfig.highlight(d);
  }
</script>

<circle
  r={isHighlighted(d) ? radius * 1.5 : radius}
  opacity={isHighlighted(d) ? 0.9 : 0.2}
  stroke={isHighlighted(d) ? "black" : "transparent"}
/>
```

### 5. Animated Transitions Between States

**CSS transitions for smooth updates:**
```css
circle {
  transition: all 400ms ease;
}
```

This handles:
- Position changes (when accessors change)
- Size changes (highlighted vs not)
- Opacity changes
- Stroke changes

### 6. Article Layout

**Typical scrollytelling structure:**
```svelte
<article>
  <header>
    <h1>Title</h1>
    <p class="byline">Subtitle</p>
  </header>

  <section>
    <!-- Sticky chart + scrolling steps -->
  </section>

  <footer>
    <p>Conclusion text</p>
  </footer>
</article>
```

### 7. Typography for Data Stories

```css
:root {
  font-family: Georgia, 'Times New Roman', serif; /* Readable for long text */
  font-size: 18px;
  line-height: 1.7;
}

header h1 {
  font-size: 2.5rem;
  line-height: 1.2;
}

.step-content {
  font-size: 1.1rem;
  line-height: 1.6;
  max-width: 350px; /* Comfortable reading width */
}
```

## Complete Scrollytelling Flow

```
1. User scrolls down
       ↓
2. Intersection Observer detects which step is visible
       ↓
3. Scrolly component updates `value` (currentStep)
       ↓
4. App receives new step index via bind:value
       ↓
5. currentConfig reactive statement updates
       ↓
6. Chart elements re-render with new highlighting
       ↓
7. CSS transitions animate the changes
```

## Step Design Patterns

### Reveal Pattern
Start with overview, then highlight specific subsets:
```javascript
steps = [
  { highlight: null },           // Show all
  { highlight: d => d.value < 20 }, // Highlight low
  { highlight: d => d.value > 80 }, // Highlight high
  { highlight: null }            // Return to overview
];
```

### Transform Pattern
Change what the axes represent:
```javascript
steps = [
  { xAccessor: d => d.grade, yAccessor: d => d.hours },
  { xAccessor: d => d.age, yAccessor: d => d.income },
];
```

### Annotation Pattern
Highlight specific data points:
```javascript
steps = [
  { highlight: d => d.name === "Sai" }, // Spotlight one
  { highlight: d => ["Sai", "Roy"].includes(d.name) }, // Compare two
];
```

## Common Gotchas

1. **Z-index stacking:** Steps must have higher z-index than sticky chart
2. **Pointer events:** Disable on steps container, re-enable on step content
3. **Step height:** Must be tall enough (90vh) to trigger intersection
4. **Observer cleanup:** Return `observer.disconnect()` from onMount
5. **Mobile consideration:** Reduce step height on small screens
6. **Performance:** Throttle expensive calculations in step transitions
