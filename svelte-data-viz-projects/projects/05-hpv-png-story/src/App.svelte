<script>
  import Scrolly from "$helpers/Scrolly.svelte";
  import BarChart from "$components/BarChart.svelte";
  import LineChart from "$components/LineChart.svelte";
  import BigNumber from "$components/BigNumber.svelte";
  import ComparisonChart from "$components/ComparisonChart.svelte";
  import ROIChart from "$components/ROIChart.svelte";

  import {
    mortalityRates,
    globalDeaths,
    pngStats,
    projectedLivesSaved,
    vaccinationImpact,
    economicData
  } from "$data/data.js";

  import { format } from "d3-format";
  import { fly, fade } from "svelte/transition";

  const formatNumber = format(",");

  // Chart dimensions
  let width = 600;
  let height = 400;

  // Scrolly state
  let currentStep = 0;

  // Story steps configuration
  const steps = [
    {
      id: "intro",
      title: "A Silent Crisis",
      text: "In 2022, cervical cancer claimed the lives of 348,709 women worldwide. More than half of these deaths occurred in the Asia-Pacific region.",
      visualization: "global-stats"
    },
    {
      id: "asia-pacific",
      title: "The Asia-Pacific Burden",
      text: "The Asia-Pacific region bears a disproportionate burden, accounting for 197,217 deaths - 56.6% of the global total.",
      visualization: "global-stats"
    },
    {
      id: "png-intro",
      title: "Papua New Guinea's Challenge",
      text: "Papua New Guinea has the second-highest cervical cancer mortality rate in the Western Pacific region, at 19.9 deaths per 100,000 women.",
      visualization: "bar-chart",
      highlightCountry: "Papua New Guinea"
    },
    {
      id: "regional-comparison",
      title: "Regional Context",
      text: "Among Asia-Pacific nations, PNG's mortality rate is exceeded only by Fiji. Both Pacific Island nations face unique healthcare access challenges.",
      visualization: "bar-chart",
      highlightCountry: null
    },
    {
      id: "vs-australia",
      title: "A Tale of Two Neighbors",
      text: "The disparity becomes stark when comparing PNG to Australia. PNG's incidence rate is 5.5 times higher, and its mortality rate is nearly 12 times higher.",
      visualization: "comparison"
    },
    {
      id: "inequity",
      title: "A Matter of Equity",
      text: "This burden falls heaviest on rural women, poorer women, and those outside major centers. Most cases are diagnosed at late stages when treatment is less effective or unavailable.",
      visualization: "inequity"
    },
    {
      id: "solution",
      title: "A Proven Solution",
      text: "The HPV vaccine is among the most effective cancer prevention tools available. Gavi estimates that vaccination prevents 17.4 deaths for every 1,000 girls vaccinated.",
      visualization: "solution-stats"
    },
    {
      id: "lives-saved",
      title: "Lives That Could Be Saved",
      text: "If PNG introduces comprehensive HPV vaccination, projections show that nearly 97,000 lives could be saved by 2070.",
      visualization: "line-chart"
    },
    {
      id: "projection-detail",
      title: "Growing Impact Over Time",
      text: "Starting with 750,000 girls in 2026 and expanding coverage annually, the cumulative impact grows substantially over the decades.",
      visualization: "line-chart"
    },
    {
      id: "economic",
      title: "A Sound Investment",
      text: "HPV vaccination isn't just good health policy - it's smart economics. UNFPA modeling shows $19 return for every $1 invested over 30 years.",
      visualization: "roi"
    },
    {
      id: "long-term-roi",
      title: "Compounding Returns",
      text: "Over a 50-year horizon, the return grows to $61.32 per dollar invested. This accounts for avoided treatment costs and preserved economic productivity.",
      visualization: "roi"
    },
    {
      id: "ready",
      title: "PNG Is Ready",
      text: "PNG has already piloted HPV vaccination in the National Capital District and Western Highlands, demonstrating its capacity to deliver adolescent vaccination programs.",
      visualization: "ready"
    },
    {
      id: "call-to-action",
      title: "The Time Is Now",
      text: "In March 2024, PNG's Senior Executive Management officially recommended HPV vaccine introduction. PNG has signed the WHO's Western Pacific 2023-2030 framework for cervical cancer elimination.",
      visualization: "call-to-action"
    }
  ];

  $: currentConfig = steps[currentStep] || steps[0];
</script>

<article>
  <!-- Hero Section -->
  <header class="hero">
    <div class="hero-content">
      <p class="kicker">Health Equity in the Pacific</p>
      <h1>The Case for HPV Vaccination in Papua New Guinea</h1>
      <p class="subtitle">
        Cervical cancer is devastating women across Papua New Guinea. A proven vaccine could save nearly 100,000 lives by 2070.
      </p>
      <p class="byline">An interactive data story by Matthew Kuch</p>
    </div>
    <div class="scroll-indicator">
      <span>Scroll to explore</span>
      <svg width="24" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 5v14M19 12l-7 7-7-7"/>
      </svg>
    </div>
  </header>

  <!-- Main Scrollytelling Section -->
  <section class="scrolly-section">
    <div class="section-container">
      <!-- Left side: scrolling text -->
      <div class="steps-column">
        <Scrolly bind:value={currentStep}>
          {#each steps as step, i}
            <div class="step" class:active={currentStep === i}>
              <div class="step-content">
                <h2 class="step-title">{step.title}</h2>
                <p class="step-text">{step.text}</p>
              </div>
            </div>
          {/each}
        </Scrolly>
      </div>

      <!-- Right side: sticky visualization -->
      <div class="sticky">
        <div class="visualization-container" bind:clientWidth={width}>
        {#if currentConfig.visualization === "global-stats"}
          <div class="stats-grid" in:fade={{ duration: 300 }}>
            <BigNumber
              number={formatNumber(globalDeaths.total)}
              label="women died from cervical cancer globally in 2022"
              color="#dc2626"
              size="large"
            />
            {#if currentStep >= 1}
              <div class="stat-breakdown" in:fly={{ y: 20, duration: 400 }}>
                <div class="stat-item asia-pacific">
                  <span class="stat-number">{formatNumber(globalDeaths.asiaPacific)}</span>
                  <span class="stat-label">deaths in Asia-Pacific ({globalDeaths.asiaPacificPercent}%)</span>
                </div>
                <div class="stat-item other">
                  <span class="stat-number">{formatNumber(globalDeaths.otherRegions)}</span>
                  <span class="stat-label">deaths in other regions ({globalDeaths.otherRegionsPercent}%)</span>
                </div>
              </div>
            {/if}
          </div>

        {:else if currentConfig.visualization === "bar-chart"}
          <div class="chart-container" in:fade={{ duration: 300 }}>
            <h3 class="chart-title">Cervical Cancer Mortality in Asia-Pacific (2022)</h3>
            <p class="chart-subtitle">Age-standardized mortality rate per 100,000 women</p>
            <BarChart
              data={mortalityRates}
              {width}
              height={500}
              highlightCountry={currentConfig.highlightCountry}
              showAll={true}
              animateIn={currentStep === 2}
            />
            <p class="chart-source">Source: Ueda (2024), Journal of Obstetrics and Gynaecology Research</p>
          </div>

        {:else if currentConfig.visualization === "comparison"}
          <div class="chart-container" in:fade={{ duration: 300 }}>
            <ComparisonChart {width} height={300} />
            <p class="chart-source">Source: Globocan 2022</p>
          </div>

        {:else if currentConfig.visualization === "inequity"}
          <div class="inequity-visual" in:fade={{ duration: 300 }}>
            <div class="inequity-icons">
              <div class="icon-group">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                </svg>
                <span>Rural women lack access to screening</span>
              </div>
              <div class="icon-group">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                </svg>
                <span>Limited oncology services outside Port Moresby</span>
              </div>
              <div class="icon-group">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span>Most diagnosed at late stages</span>
              </div>
              <div class="icon-group">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                  <path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                </svg>
                <span>Women in prime years - mothers, caregivers, breadwinners</span>
              </div>
            </div>
            <p class="inequity-quote">
              "Failing to act means rural women, poorer women, and women outside major centers continue to bear a disproportionate share of an entirely preventable disease."
            </p>
          </div>

        {:else if currentConfig.visualization === "solution-stats"}
          <div class="solution-visual" in:fade={{ duration: 300 }}>
            <div class="solution-stat">
              <span class="big-stat">17.4</span>
              <span class="stat-desc">deaths averted for every 1,000 girls vaccinated</span>
            </div>
            <div class="vaccine-info">
              <h4>The HPV Vaccine</h4>
              <ul>
                <li>Prevents infection from high-risk HPV types that cause most cervical cancers</li>
                <li>Most effective when given to girls aged 9-14, before HPV exposure</li>
                <li>Single-dose schedule now recommended by WHO</li>
                <li>Over 500 million doses administered globally</li>
              </ul>
            </div>
          </div>

        {:else if currentConfig.visualization === "line-chart"}
          <div class="chart-container" in:fade={{ duration: 300 }}>
            <h3 class="chart-title">Projected Lives Saved Through HPV Vaccination</h3>
            <p class="chart-subtitle">Papua New Guinea, 2026-2070</p>
            <LineChart
              data={projectedLivesSaved}
              {width}
              height={450}
              showArea={true}
            />
            <p class="chart-source">
              Based on Gavi estimate of 17.4 deaths averted per 1,000 vaccinated.
              Assumes 80% initial coverage expanding to 90%.
            </p>
          </div>

        {:else if currentConfig.visualization === "roi"}
          <div class="chart-container" in:fade={{ duration: 300 }}>
            <ROIChart {width} height={350} animate={currentStep === 10} />
            <p class="chart-source">Source: UNFPA PNG cervical cancer elimination modeling</p>
          </div>

        {:else if currentConfig.visualization === "ready"}
          <div class="ready-visual" in:fade={{ duration: 300 }}>
            <div class="ready-content">
              <h3>Building on Experience</h3>
              <div class="pilot-info">
                <div class="pilot-location">
                  <span class="location-icon">📍</span>
                  <span class="location-name">National Capital District</span>
                </div>
                <div class="pilot-location">
                  <span class="location-icon">📍</span>
                  <span class="location-name">Western Highlands Province</span>
                </div>
              </div>
              <p class="ready-text">
                These pilot programs demonstrate PNG's capacity to deliver immunization campaigns targeting the adolescent age cohort (9-14 year olds).
              </p>
              <div class="ready-stats">
                <div class="ready-stat">
                  <span class="stat-value">5.5M+</span>
                  <span class="stat-label">girls could be vaccinated by 2070</span>
                </div>
                <div class="ready-stat">
                  <span class="stat-value">~97,000</span>
                  <span class="stat-label">lives saved</span>
                </div>
              </div>
            </div>
          </div>

        {:else if currentConfig.visualization === "call-to-action"}
          <div class="cta-visual" in:fade={{ duration: 300 }}>
            <div class="cta-content">
              <div class="checkmarks">
                <div class="check-item">
                  <span class="check">✓</span>
                  <span>SEM recommendation (March 2024)</span>
                </div>
                <div class="check-item">
                  <span class="check">✓</span>
                  <span>WHO Western Pacific Framework signatory</span>
                </div>
                <div class="check-item">
                  <span class="check">✓</span>
                  <span>Gavi support eligible</span>
                </div>
                <div class="check-item">
                  <span class="check">✓</span>
                  <span>Pilot program experience</span>
                </div>
              </div>
              <div class="final-message">
                <p class="message-text">
                  Introducing HPV vaccination is not just a technical immunization decision.
                </p>
                <p class="message-highlight">
                  It is a gender, equity, and social justice decision.
                </p>
              </div>
            </div>
          </div>
        {/if}
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-content">
      <h2>Take Action</h2>
      <p>
        Support the introduction of HPV vaccination in Papua New Guinea.
        Together, we can eliminate cervical cancer as a public health threat.
      </p>
      <div class="sources">
        <h3>Sources</h3>
        <ul>
          <li>Global Cancer Observatory (GCO, 2022)</li>
          <li>Ueda (2024), Journal of Obstetrics and Gynaecology Research</li>
          <li>Globocan PNG Factsheet, 2022</li>
          <li>UNFPA PNG Cervical Cancer Elimination Brief</li>
          <li>Gavi HPV Impact Report, 2022</li>
          <li>WHO Western Pacific Region Framework 2023-2030</li>
        </ul>
      </div>
      <p class="credit">
        Built with Svelte and D3.js
      </p>
    </div>
  </footer>
</article>

<style>
  /* Global article styles */
  article {
    background: var(--color-bg);
  }

  /* Hero Section - refined, editorial style */
  .hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--color-primary);
    color: white;
    text-align: center;
    padding: 2.5rem;
    position: relative;
  }

  .hero-content {
    max-width: 720px;
  }

  .kicker {
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: var(--color-accent-blue);
    margin-bottom: 1.25rem;
    font-family: var(--font-sans);
    font-weight: 500;
  }

  .hero h1 {
    font-size: clamp(2.25rem, 5vw, 3.25rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 1.75rem;
    letter-spacing: -0.02em;
  }

  .subtitle {
    font-size: clamp(1.05rem, 2.5vw, 1.2rem);
    line-height: 1.55;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 2.5rem;
    max-width: 560px;
    margin-left: auto;
    margin-right: auto;
    font-family: var(--font-sans);
    font-weight: 400;
  }

  .byline {
    font-size: 0.85rem;
    color: var(--color-accent-blue);
    font-family: var(--font-sans);
    font-weight: 400;
    letter-spacing: 0.02em;
  }

  .scroll-indicator {
    position: absolute;
    bottom: 2.5rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.8rem;
    font-family: var(--font-sans);
    animation: gentleBounce 2.5s ease-in-out infinite;
  }

  @keyframes gentleBounce {
    0%, 100% { transform: translateX(-50%) translateY(0); opacity: 0.5; }
    50% { transform: translateX(-50%) translateY(-6px); opacity: 0.8; }
  }

  /* Scrollytelling Section - Two Column Layout */
  .scrolly-section {
    position: relative;
  }

  .section-container {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
  }

  /* Left column - scrolling text */
  .steps-column {
    flex: 0 0 360px;
    width: 360px;
    position: relative;
    z-index: 10;
  }

  .step {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 2rem 1.5rem 2rem 2.5rem;
  }

  /* Step cards - cleaner, less shadow (Tufte: reduce non-data ink) */
  .step-content {
    pointer-events: auto;
    padding: 1.5rem 1.75rem;
    background: white;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    border-left: 3px solid transparent;
    max-width: 320px;
    opacity: 0.25;
    transition: opacity 350ms ease, border-color 350ms ease;
  }

  .step.active .step-content {
    opacity: 1;
    border-left-color: var(--color-danger);
  }

  .step-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
    color: var(--color-primary);
    letter-spacing: -0.01em;
  }

  .step-text {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--color-text-secondary);
    margin: 0;
    font-family: var(--font-sans);
  }

  /* Right column - sticky visualization */
  .sticky {
    flex: 1;
    position: sticky;
    top: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--color-bg);
    z-index: 1;
    padding: 1.5rem;
  }

  .visualization-container {
    width: 100%;
    max-width: 800px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* Chart containers - minimal, clean (NYT style) */
  .chart-container {
    width: 100%;
    background: white;
    padding: 2rem 1.75rem;
    border-radius: 2px;
    box-shadow: none;
    border: 1px solid var(--color-border);
  }

  .chart-title {
    font-size: 1.05rem;
    font-weight: 600;
    text-align: left;
    margin-bottom: 0.15rem;
    color: var(--color-text);
    letter-spacing: -0.01em;
  }

  .chart-subtitle {
    font-size: 0.8rem;
    color: var(--color-text-light);
    text-align: left;
    margin-bottom: 1.25rem;
    font-family: var(--font-sans);
  }

  .chart-source {
    font-size: 0.7rem;
    color: var(--color-text-light);
    text-align: left;
    margin-top: 1.25rem;
    font-family: var(--font-sans);
    border-top: 1px solid var(--color-grid);
    padding-top: 0.75rem;
  }

  /* Stats grid - cleaner presentation */
  .stats-grid {
    text-align: center;
  }

  .stat-breakdown {
    display: flex;
    gap: 2.5rem;
    justify-content: center;
    margin-top: 2.5rem;
    flex-wrap: wrap;
  }

  .stat-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1.25rem 1.75rem;
    border-radius: 2px;
    border-bottom: 2px solid transparent;
  }

  .stat-item.asia-pacific {
    background: var(--color-danger-light);
    border-bottom-color: var(--color-danger);
  }

  .stat-item.other {
    background: #f7f7f7;
    border-bottom-color: var(--color-text-light);
  }

  .stat-number {
    font-size: 1.75rem;
    font-weight: 600;
    font-family: var(--font-serif);
    letter-spacing: -0.02em;
  }

  .asia-pacific .stat-number {
    color: var(--color-danger);
  }

  .other .stat-number {
    color: var(--color-text-secondary);
  }

  .stat-label {
    font-size: 0.8rem;
    color: var(--color-text-light);
    font-family: var(--font-sans);
    max-width: 170px;
    text-align: center;
    margin-top: 0.25rem;
  }

  /* Inequity visual - cleaner, more impactful */
  .inequity-visual {
    max-width: 580px;
    width: 100%;
    text-align: center;
  }

  .inequity-icons {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.75rem;
    margin-bottom: 2.5rem;
  }

  .icon-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
  }

  .icon {
    width: 40px;
    height: 40px;
    stroke: var(--color-danger-muted);
    stroke-width: 1.25;
  }

  .icon-group span {
    font-size: 0.82rem;
    color: var(--color-text-secondary);
    font-family: var(--font-sans);
    line-height: 1.4;
  }

  .inequity-quote {
    font-style: italic;
    color: var(--color-text-secondary);
    padding: 1.25rem 1.5rem;
    background: var(--color-danger-light);
    border-left: 3px solid var(--color-danger);
    border-radius: 0;
    line-height: 1.55;
    text-align: left;
    font-size: 0.95rem;
  }

  /* Solution visual - refined */
  .solution-visual {
    text-align: center;
    max-width: 540px;
    width: 100%;
  }

  .solution-stat {
    margin-bottom: 2.5rem;
  }

  .big-stat {
    font-size: 4.5rem;
    font-weight: 600;
    color: var(--color-success);
    font-family: var(--font-serif);
    display: block;
    line-height: 1;
    letter-spacing: -0.02em;
  }

  .stat-desc {
    font-size: 0.95rem;
    color: var(--color-text-light);
    font-family: var(--font-sans);
    margin-top: 0.5rem;
  }

  .vaccine-info {
    background: var(--color-success-light);
    padding: 1.5rem 1.75rem;
    border-radius: 2px;
    text-align: left;
    border-left: 3px solid var(--color-success);
  }

  .vaccine-info h4 {
    color: var(--color-success);
    margin-bottom: 0.85rem;
    font-size: 1rem;
    font-weight: 600;
  }

  .vaccine-info ul {
    margin: 0;
    padding-left: 1.1rem;
  }

  .vaccine-info li {
    margin-bottom: 0.4rem;
    font-size: 0.85rem;
    color: var(--color-text-secondary);
    font-family: var(--font-sans);
    line-height: 1.5;
  }

  /* Ready visual - cleaner */
  .ready-visual {
    max-width: 540px;
    width: 100%;
  }

  .ready-content h3 {
    text-align: center;
    color: var(--color-primary);
    margin-bottom: 1.75rem;
    font-size: 1.15rem;
    font-weight: 600;
  }

  .pilot-info {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1.75rem;
    flex-wrap: wrap;
  }

  .pilot-location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #f0f7fc;
    padding: 0.65rem 1.1rem;
    border-radius: 2px;
    border-left: 2px solid var(--color-accent-blue);
  }

  .location-icon {
    font-size: 1rem;
  }

  .location-name {
    font-family: var(--font-sans);
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--color-primary);
  }

  .ready-text {
    text-align: center;
    color: var(--color-text-secondary);
    font-size: 0.9rem;
    margin-bottom: 1.75rem;
    line-height: 1.55;
    font-family: var(--font-sans);
  }

  .ready-stats {
    display: flex;
    justify-content: center;
    gap: 2.5rem;
    flex-wrap: wrap;
  }

  .ready-stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: var(--color-success-light);
    padding: 1rem 1.5rem;
    border-radius: 2px;
    border-bottom: 2px solid var(--color-success);
  }

  .ready-stat .stat-value {
    font-size: 1.65rem;
    font-weight: 600;
    color: var(--color-success);
    font-family: var(--font-serif);
    letter-spacing: -0.02em;
  }

  .ready-stat .stat-label {
    font-size: 0.75rem;
    color: var(--color-text-light);
    font-family: var(--font-sans);
    margin-top: 0.15rem;
  }

  /* CTA visual - refined */
  .cta-visual {
    max-width: 520px;
    width: 100%;
  }

  .cta-content {
    text-align: center;
  }

  .checkmarks {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
    margin-bottom: 2rem;
    text-align: left;
  }

  .check-item {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    background: var(--color-success-light);
    padding: 0.7rem 1rem;
    border-radius: 2px;
  }

  .check {
    width: 20px;
    height: 20px;
    background: var(--color-success);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    flex-shrink: 0;
    font-size: 0.7rem;
  }

  .check-item span:last-child {
    font-family: var(--font-sans);
    font-size: 0.85rem;
    color: var(--color-text-secondary);
    text-align: left;
  }

  .final-message {
    padding: 1.5rem 1.75rem;
    background: var(--color-primary);
    border-radius: 2px;
    color: white;
    text-align: left;
  }

  .message-text {
    font-size: 0.9rem;
    margin-bottom: 0.6rem;
    opacity: 0.85;
    font-family: var(--font-sans);
  }

  .message-highlight {
    font-size: 1.05rem;
    font-weight: 600;
    margin: 0;
    letter-spacing: -0.01em;
  }

  /* Footer - refined, minimal */
  footer {
    background: var(--color-primary);
    color: white;
    padding: 4rem 2.5rem;
  }

  .footer-content {
    max-width: 640px;
    margin: 0 auto;
    text-align: center;
  }

  footer h2 {
    font-size: 1.5rem;
    margin-bottom: 0.85rem;
    font-weight: 600;
    letter-spacing: -0.01em;
  }

  footer p {
    font-size: 0.95rem;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.75);
    margin-bottom: 2.5rem;
    font-family: var(--font-sans);
  }

  .sources {
    text-align: left;
    background: rgba(255, 255, 255, 0.06);
    padding: 1.25rem 1.5rem;
    border-radius: 2px;
    margin-bottom: 2.5rem;
    border-left: 2px solid rgba(255, 255, 255, 0.2);
  }

  .sources h3 {
    font-size: 0.8rem;
    margin-bottom: 0.75rem;
    color: var(--color-accent-blue);
    font-family: var(--font-sans);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 500;
  }

  .sources ul {
    margin: 0;
    padding-left: 1rem;
  }

  .sources li {
    font-size: 0.8rem;
    color: rgba(255, 255, 255, 0.65);
    margin-bottom: 0.3rem;
    font-family: var(--font-sans);
  }

  .credit {
    font-size: 0.8rem;
    color: rgba(255, 255, 255, 0.45);
    margin: 0;
    font-family: var(--font-sans);
  }

  /* Responsive - Tablet */
  @media (max-width: 1024px) {
    .section-container {
      flex-direction: column;
    }

    .steps-column {
      flex: none;
      width: 100%;
      position: relative;
      z-index: 2;
    }

    .step {
      justify-content: center;
      padding: 2rem;
    }

    .step-content {
      max-width: 400px;
    }

    .sticky {
      position: sticky;
      top: 0;
      height: 100vh;
      width: 100%;
    }

    .visualization-container {
      max-width: 700px;
    }
  }

  /* Responsive - Mobile */
  @media (max-width: 768px) {
    .hero h1 {
      font-size: 2rem;
    }

    .step-content {
      max-width: 320px;
      padding: 1.5rem;
    }

    .stat-breakdown {
      flex-direction: column;
      gap: 1rem;
    }

    .inequity-icons {
      grid-template-columns: 1fr;
    }

    .pilot-info {
      flex-direction: column;
      gap: 1rem;
    }

    .ready-stats {
      flex-direction: column;
    }

    .visualization-container {
      padding: 1rem;
    }
  }
</style>
