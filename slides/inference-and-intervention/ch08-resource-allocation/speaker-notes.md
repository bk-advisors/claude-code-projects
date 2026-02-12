# Speaker Notes — Chapter 8: MNH Resource Allocation

## Overview
This chapter takes the single-agent decision framework from Chapter 7 and scales it to the real problem: allocating pooled funding across multiple countries under deep uncertainty. The parallels to the textbook's rideshare case are deliberate — same analytical structure, different domain. By the end, students understand why naive "allocate to the cheapest country" logic fails, why portfolio diversification matters even in public health, and why the cost of delay is measured in lives.

## Slide: Learning Objectives
Five objectives that escalate in complexity. Framing multi-country allocation as a decision under uncertainty is the foundation. Then we build probability distributions over the key unknowns, learn sequential decision-making (commit → observe → scale), grapple with stakeholder responses (crowding out vs. crowding in), and finally use Monte Carlo simulation to compare strategies with confidence intervals. Every objective maps to a real task a program analyst faces during funding allocation cycles.

## Slide: The Rideshare Problem
This connects back to the Ryall & Bramson textbook. The rideshare company deciding how to allocate drivers between San Francisco and New York faces the same structural problem as an MNH program allocating across countries. The core tradeoff — concentrate in one market for higher potential return vs. spread across markets for lower risk — is universal. The definition box sets up the parallels: market demand uncertainty maps to baseline burden uncertainty, competitor response maps to government co-financing, and regulatory environment maps to health system readiness.

## Slide: From the Rideshare Case to the MNH Program
The mapping table makes the structural parallel explicit. Drivers across cities → funding across countries. Market demand → baseline burden. Competitor legal response → government co-financing. Revenue → lives saved. The key takeaway is that these aren't just superficial analogies — the *analytical tools* transfer directly. Influence diagrams, expected value, decision trees, sensitivity analysis — all built for the rideshare case — apply without modification to MNH allocation.

## Slide: The MNH Program Portfolio
This table grounds everything in scale. The program targets hundreds of thousands of lives saved across 10 countries. Country A alone accounts for 45,000 lives — driven by both high NMR (28.1 per 1,000) and large birth cohort. Countries enter in cohorts, and Country J is still TBD pending the next funding cycle. The distribution of targets already reflects some analytical reasoning, but the core question is: given uncertainty, how should the actual funding be split?

## Slide: What Makes This Hard
Three dimensions of difficulty, each with its own uncertainty. Baseline burden determines the *potential* for impact — Country A has the most room for improvement. Health system capacity determines whether investment can actually be *absorbed* — Country H has great systems but smaller targets. Government readiness is the wild card — it determines long-run sustainability and is the hardest to predict. The orange callout highlights that government readiness is both the most uncertain and the most consequential variable.

## Slide: Sources of Uncertainty
This table catalogs the five major uncertainties. Government co-financing affects long-run impact. Intervention coverage affects short-run lives saved. Workforce retention determines capacity sustainability. Political stability is a binary risk that can derail everything. Other donor behavior changes the marginal value of program funding. The red callout frames the fundamental challenge: we must commit funds *before* resolving these uncertainties. The question isn't "what's the right allocation?" but "what allocation is robust to what we don't know?"

## Slide: The Allocation Decision Space
Now we formalize the decision. The program chooses an allocation vector that sums to the total budget. Three archetype strategies capture the key tradeoff: Concentrate (70%+ to top 3 countries — high EV, high variance), Spread (roughly equal across all 10 — lower EV, lower variance), and Tiered (weighted by burden × capacity with floors and ceilings — the balanced approach). The callout connects back to the rideshare case: same structure, just ten countries instead of two cities.

## Slide: Government Co-Financing Scenarios
Government co-financing is modeled with three scenarios. High (40% probability): government meets commitments, full target achieved. Medium (50%): partial commitment, 60% of target. Low (10%): government reneges, only 25% achieved. The expected achievement rate of 72.5% is the baseline — roughly consistent with historical large-scale public health programs. But this is an average; country-specific probabilities vary significantly.

## Slide: Country-Specific Probability Profiles
This table shows how risk profiles differ by country. Country H has a 60% chance of high co-financing and 83.3% expected achievement — it's the safest bet but has the smallest target. Country I has only 20% chance of high co-financing and 55.8% expected achievement — high risk, high need. The orange callout identifies the core allocation tradeoff: the safest countries have the smallest targets, while the highest-burden countries carry the most uncertainty. You can't optimize expected value and minimize risk simultaneously.

## Slide: Decision Tree for a Single Country
This walks through the EV calculation for a single country. Country A with its 40/45/15 probability split across co-financing scenarios gives EV = 31,838 lives. But the slide's real point is in the callout: this number is meaningless in isolation. The question is whether those dollars would save *more* lives in Country C or Country B. We need to compare expected lives per dollar across countries, not just total lives.

## Slide: Scenario Analysis: Best / Base / Worst
The portfolio-level scenarios are sobering. Best case (all countries achieve high co-financing): ~185,000 lives. Base case (country-specific probability mix): ~131,000 lives (70.7% of target). Worst case (all countries at low co-financing): ~46,000 lives (25%). The worst case losing three-quarters of the target is what motivates portfolio diversification — we can't afford to concentrate bets when the downside is this severe.

## Slide: The Multi-Stage Structure
The program doesn't have to commit everything upfront. The pilot → observe → scale structure creates valuable optionality. Stage 1 commits seed funding. After 12-18 months, pilot results inform Stage 2 decisions. This is exactly the rideshare structure from the book — test a market before going all-in. The value of this sequential approach depends on how informative the pilot signal is.

## Slide: Rolling Back the Decision Tree
Backward induction for Country A's two-stage decision. After a promising pilot (P=0.35), scale up for 38,200 expected lives. After a mixed signal (P=0.45), proceed moderately for 25,300. After a negative signal (P=0.20), redirect funds for 6,400. Working backward: EV(Sequential) = 26,035 lives. This is *less* than the commit-all-upfront EV of 31,838 because less money is committed — but the worst case is dramatically better. Sequential decision-making trades expected value for risk reduction.

## Slide: The Value of Waiting vs. the Cost of Delay
This is the most distinctive slide of the chapter. In commercial allocation, delay costs money. In public health, delay costs lives. Every month of pilot delay means thousands of preventable neonatal deaths occurring across the 10 countries. The two columns lay out the tension: waiting gives better information and reduces portfolio variance, but inaction during the waiting period is measured in deaths. This tension between learning and acting is what makes health allocation fundamentally different from business portfolio optimization.

## Slide: MNH Application: 2-Stage Decision for Country J
Country J illustrates sequential decision-making for a new-phase country. The pilot in 3 subnational regions tests government co-financing, workforce absorption, and political stability before the full commitment. The numbers show the sequential approach yields slightly fewer expected lives (11,200 vs. 12,500 from full commitment) but saves significant resources — resources that can be redeployed to higher-confidence countries. The freed capital is the real win.

## Slide: Crowding Out vs. Crowding In
Now we add a layer of strategic complexity. Crowding out: the program's investment causes the government or other donors to *reduce* their own spending ("they've got it covered"). Crowding in: the program's investment catalyzes *additional* spending from others ("this sector is getting results"). In the crowding-out scenario, every dollar of program investment yields only $0.63 of net new investment. In the crowding-in scenario, it yields $1.50. Same program dollars, dramatically different impact.

## Slide: Modeling Other Donors
Other donors respond to the program's allocation with a probability distribution: 30% chance they redirect away (0.7× multiplier), 45% they maintain (1.0×), 25% they match (1.4×). The expected multiplier is roughly 1.0 — crowding effects roughly cancel on average. But the orange callout makes the important point: the *variance* matters. In 30% of cases, your dollar buys only $0.70 of new investment. Strategic coordination with other donors can shift these probabilities favorably.

## Slide: Preview: Game Theory (Chapter 9)
This slide bridges to Chapter 9 by flagging that stakeholder response is fundamentally a game theory problem. Governments and donors aren't passive — they have their own objectives and respond strategically. Nash equilibrium, commitment devices, signaling, and mechanism design are previewed. The green callout sets the boundary: for now, we treat stakeholder behavior as a chance node. In Chapter 9, we'll upgrade it to a strategic variable with its own decision logic.

## Slide: The 3-Country Problem
Now we apply the full framework to a concrete allocation. The program has a fixed budget for Country A, Country C, and Country B. The table shows expected achievement rates and lives per dollar. The naive approach — allocate by lives per dollar — would send everything to Country A. The orange callout explains why this is wrong: it ignores risk (Country A has more uncertainty) and diminishing returns (marginal impact decreases with scale).

## Slide: Influence Diagram for 3-Country Allocation
The influence diagram has one decision node (allocation vector), coverage nodes per country influenced by the allocation and uncertain factors (government co-financing, donor response), and a single objective (total lives saved). The key feature is that the uncertain variables are country-specific — each country has its own co-financing probability and donor response distribution. This means the optimal allocation depends on the *joint* uncertainty structure.

## Slide: Comparing Strategies
Three strategies for the 3-country sub-portfolio. Concentrate (70/15/15) has the highest EV (57,400) but also the highest standard deviation (14,500). Spread (33/33/33) has the lowest EV (53,200) and lowest SD (9,800). Tiered (45/23/32) sits in between: 56,100 lives with 11,500 SD. The green callout invokes efficient frontier logic from portfolio theory — the Tiered strategy sacrifices modest expected value for a ~20% reduction in risk.

## Slide: Sensitivity to Government Co-Financing
The sensitivity analysis answers a practical question: at what point does the co-financing risk actually change our strategy choice? If Country A's P(High co-financing) exceeds 0.35, Concentrate becomes optimal. Below 0.35, Tiered wins on risk-adjusted grounds. The green callout translates this into action: the program's confidence in Country A's government commitment is the single most important input to the allocation decision.

## Slide: Recommendation with Confidence Intervals
The recommended Tiered allocation (Country A 45%, Country C 23%, Country B 32%) delivers ~56,100 expected lives with a 95% CI of ~34,900–75,600. The four-point rationale covers robustness (within 3% of Concentrate under favorable conditions), diversification (different risk profiles), political feasibility (equity across governments), and adaptive capacity (preserves the option to reallocate based on observed performance).

## Slide: R Block 1: Monte Carlo Simulation
Live coding walkthrough. Students simulate outcomes for each allocation strategy using 10,000 draws, incorporating government co-financing scenarios and country-specific uncertainty.

## Slide: R Block 2: Visualize Strategy Outcomes
Live coding walkthrough. Students create violin plots with embedded box plots showing the full distribution of outcomes for each strategy — making the risk-return tradeoff visually obvious.

## Slide: R Block 3: Optimal Allocation via Grid Search
Live coding walkthrough. Students search over the allocation space in 5% increments to find the EV-maximizing allocation and the maximin (best worst-case) allocation, seeing how the two objectives lead to different answers.

## Slide: R Block 4: Sensitivity Analysis
Live coding walkthrough. Students vary Country A's co-financing probability and plot how it affects the EV of each strategy, identifying the crossover point where Concentrate overtakes Tiered.

## Slide: Key Takeaways
Six lessons that tie the chapter together. Portfolio thinking applies to public health — diversification reduces catastrophic shortfall risk. Sequential decisions add value by resolving uncertainty, but delay costs lives. Government co-financing is the dominant uncertainty. Stakeholder response can amplify or undermine impact. Monte Carlo simulation enables rigorous comparison. And the cost of delay, measured in lives, is what distinguishes health allocation from commercial portfolio optimization.

## Slide: Looking Ahead
Chapter 9 upgrades stakeholder behavior from chance node to strategic agent. Governments, other donors, and implementing partners aren't just uncertain — they're rational actors with their own objectives. Nash equilibrium, commitment devices, and mechanism design provide the tools for navigating these multi-agent interactions. The transition from Chapter 8 to Chapter 9 is the transition from "nature rolls the dice" to "other players make strategic choices."
