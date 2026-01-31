<script>
  import Scrolly from "$helpers/Scrolly.svelte";
  import AxisX from "$components/AxisX.svelte";
  import AxisY from "$components/AxisY.svelte";
  import Tooltip from "$components/Tooltip.svelte";
  import data from "$data/data.js";

  import { scaleLinear, scaleBand } from "d3-scale";
  import { max } from "d3-array";
  import { fly } from "svelte/transition";

  let width = 400;
  let height = 400;

  const margin = { top: 25, right: 15, bottom: 40, left: 0 };
  const radius = 8;

  // Scrolly state
  let currentStep = 0;

  // Story steps with different data views
  const steps = [
    {
      text: "We surveyed 18 students about their study habits and final exam performance.",
      highlight: null,
      xAccessor: d => d.grade,
      yAccessor: d => d.hours,
      xLabel: "Final Grade (%)",
      yLabel: "hours studied"
    },
    {
      text: "Some students studied very little and scored poorly on their exams.",
      highlight: d => d.hours < 20,
      xAccessor: d => d.grade,
      yAccessor: d => d.hours,
      xLabel: "Final Grade (%)",
      yLabel: "hours studied"
    },
    {
      text: "Students who studied more tended to perform better.",
      highlight: d => d.hours >= 40,
      xAccessor: d => d.grade,
      yAccessor: d => d.hours,
      xLabel: "Final Grade (%)",
      yLabel: "hours studied"
    },
    {
      text: "Sai studied the most (60 hours) and achieved the highest grade (99%).",
      highlight: d => d.name === "Sai",
      xAccessor: d => d.grade,
      yAccessor: d => d.hours,
      xLabel: "Final Grade (%)",
      yLabel: "hours studied"
    },
    {
      text: "The data suggests a positive correlation between study time and exam performance.",
      highlight: null,
      xAccessor: d => d.grade,
      yAccessor: d => d.hours,
      xLabel: "Final Grade (%)",
      yLabel: "hours studied"
    }
  ];

  $: currentConfig = steps[currentStep] || steps[0];

  // Scales
  $: xScale = scaleLinear()
    .domain([0, 100])
    .range([0, width - margin.left - margin.right]);

  $: yScale = scaleLinear()
    .domain([0, max(data, currentConfig.yAccessor)])
    .range([height - margin.bottom - margin.top, 0]);

  // Hover state
  let hoveredData = null;

  function isHighlighted(d) {
    if (!currentConfig.highlight) return true;
    return currentConfig.highlight(d);
  }
</script>

<article>
  <header>
    <h1>The Relationship Between Study Time and Exam Performance</h1>
    <p class="byline">A data-driven story using Svelte and D3</p>
  </header>

  <section>
    <div class="sticky">
      <div class="chart-container" bind:clientWidth={width}>
        <svg {width} {height} on:mouseleave={() => (hoveredData = null)}>
          <AxisX {xScale} {width} {height} {margin} label={currentConfig.xLabel} />
          <AxisY {yScale} {width} {margin} label={currentConfig.yLabel} />

          <g class="inner-chart" transform="translate({margin.left}, {margin.top})">
            {#each data as d, index}
              <circle
                cx={xScale(currentConfig.xAccessor(d))}
                cy={yScale(currentConfig.yAccessor(d))}
                fill="purple"
                stroke={isHighlighted(d) ? "black" : "transparent"}
                stroke-width="2"
                r={isHighlighted(d) ? radius * 1.5 : radius}
                opacity={isHighlighted(d) ? 0.9 : 0.2}
                on:mouseover={() => (hoveredData = d)}
                on:focus={() => (hoveredData = d)}
                tabindex="0"
                role="button"
                aria-label="{d.name}: {d.grade}% grade"
              />
            {/each}
          </g>
        </svg>

        {#if hoveredData}
          <Tooltip
            data={hoveredData}
            {xScale}
            {yScale}
            xAccessor={currentConfig.xAccessor}
            yAccessor={currentConfig.yAccessor}
            {width}
          />
        {/if}
      </div>
    </div>

    <div class="steps">
      <Scrolly bind:value={currentStep}>
        {#each steps as step, i}
          <div class="step" class:active={currentStep === i}>
            <div class="step-content">
              <p>{step.text}</p>
            </div>
          </div>
        {/each}
      </Scrolly>
    </div>
  </section>

  <footer>
    <p>Scroll up to explore the data again.</p>
  </footer>
</article>

<style>
  article {
    max-width: 1200px;
    margin: 0 auto;
  }

  header {
    text-align: center;
    padding: 4rem 1rem;
    max-width: 700px;
    margin: 0 auto;
  }

  header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    line-height: 1.2;
  }

  .byline {
    color: #666;
    font-style: italic;
  }

  section {
    position: relative;
  }

  .sticky {
    position: sticky;
    top: 10vh;
    width: 100%;
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fafafa;
  }

  .chart-container {
    position: relative;
    max-width: 600px;
    width: 100%;
    padding: 1rem;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .steps {
    position: relative;
    z-index: 2;
    pointer-events: none;
  }

  .step {
    height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0.3;
    transition: opacity 300ms ease;
  }

  .step.active {
    opacity: 1;
  }

  .step-content {
    pointer-events: auto;
    padding: 1.5rem 2rem;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.15);
    max-width: 350px;
    font-size: 1.1rem;
  }

  .step-content p {
    margin: 0;
    line-height: 1.6;
  }

  footer {
    text-align: center;
    padding: 4rem 1rem;
    color: #666;
  }

  :global(.tick text, .axis-title) {
    font-family: system-ui, sans-serif;
    font-weight: 400;
    font-size: 11px;
    fill: #666;
  }

  circle {
    transition: all 400ms ease;
    cursor: pointer;
  }
</style>
