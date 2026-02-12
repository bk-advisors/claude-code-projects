# Speaker Notes — Chapter 6: Modeling MNH Cost-Effectiveness

## Overview
This chapter is about two analytical traps that ruin real-world decisions: Simpson's Paradox and the Prosecutor's Fallacy. Both arise from ignoring causal structure when interpreting data. The MNH application is especially vivid — naive cross-country comparisons of cost-per-life-saved can literally reverse the correct ranking of where to invest. The chapter shows how causal reasoning resolves both paradoxes and prevents catastrophic misallocation of resources. This is where the theoretical toolkit from Chapters 1-5 saves lives.

## Slide: Learning Objectives
Five practical objectives. Students will learn to spot Simpson's Paradox in aggregated program data, avoid the Prosecutor's Fallacy with Bayes' rule, apply both insights to cost-effectiveness analysis, simulate the paradoxes in R, and make sound resource-allocation recommendations. Every objective maps to a real decision an MNH program analyst faces.

## Slide: The Slimtree Publishing Case
This connects back to the textbook. Ryall & Bramson use a publishing company's P&L to show how making causal structure explicit reveals hidden assumptions. We adapt the same logic to MNH cost-effectiveness. The key parallel: a P&L spreadsheet is already an implicit causal model (inputs minus costs equals profit), just as a CPLS calculation is an implicit causal model (cost divided by lives saved). Making the structure explicit — via a DAG — reveals where the reasoning can go wrong.

## Slide: Transition: From Profit to Lives Saved
The two-column comparison shows the structural parallel between Slimtree Publishing and MNH cost-effectiveness. Same analytical tools, different domain. The paradox works the same way: a product line that looks unprofitable overall but is profitable in every segment maps directly to an intervention that looks ineffective overall but is effective in every country group. The orange callout reinforces that causal reasoning transfers across domains.

## Slide: The Key Metric: Cost Per Life Saved
CPLS is the primary efficiency metric for large MNH programs. Lower CPLS means more lives saved per dollar. The critical point is in the red callout: comparing CPLS across countries without adjusting for confounders is like comparing apples to oranges. A country with high CPLS might actually be the *best* investment when you account for baseline severity, health system capacity, and population density. The raw number is misleading without causal context.

## Slide: Lives Saved Targets by Country
This table grounds the discussion in scale. The program targets nearly 300,000 lives saved across 9 countries. Country A accounts for 26.5% of the target, driven by population size and high baseline NMR. The distribution of targets already reflects some causal reasoning — larger allocations to higher-burden countries — but the key question is whether the CPLS-based comparisons that guide resource allocation are correctly accounting for confounders.

## Slide: The Danger of Naive Rankings
This is the headline slide. The naive approach ranks Country H first (lowest CPLS at $820). But when you adjust for confounders, Country A becomes the most efficient ($980 adjusted). The rankings completely reverse. Country H's low raw CPLS reflects its strong health system — not superior intervention efficiency. Investing everything in Country H would be precisely the wrong decision. This is Simpson's Paradox applied to resource allocation.

## Slide: Definition: Simpson's Paradox
The formal definition: a trend in aggregated data reverses when disaggregated by a confounding variable. The key question is whether to condition on a particular variable, and the answer depends on the causal structure. Is the variable a confounder (condition on it) or a mediator (don't)? You can't answer this question without a DAG. That's why causal reasoning is essential, not optional.

## Slide: Classic Example: UC Berkeley Admissions
The Berkeley admissions example is the most famous illustration of Simpson's Paradox. Overall, men were admitted at higher rates (44% vs. 35%). But within most departments, women were admitted at higher rates. The paradox arose because women disproportionately applied to competitive departments. Department choice was the confounder. This example makes the paradox tangible before we apply it to MNH.

## Slide: MNH Example: CPAP Intervention
Now we bring it home. Aggregated across all countries, CPAP appears to *reduce* survival (72% vs. 78% without CPAP). Alarming! But disaggregated by country group, CPAP improves survival in every stratum — +7 pp in high-burden countries, +3 pp in low-burden countries. The aggregated result is entirely driven by the composition effect: CPAP is used more in high-burden countries where baseline survival is lower. The intervention works; the comparison is misleading.

## Slide: The Confounder: Baseline Severity
The DAG makes the mechanism clear. Baseline severity is a fork (common cause) driving both CPAP usage (high-burden countries use it more) and survival rate (high-burden countries have lower baseline survival). The composition effect overwhelms the treatment effect in the aggregated data. Conditioning on country group — stratifying by baseline severity — removes the confounding and reveals the true positive effect of CPAP.

## Slide: Key Insight: Confounders vs. Mediators
This is the decision rule students must internalize. Condition on confounders (common causes of treatment and outcome) — this removes spurious associations. Do NOT condition on mediators (variables on the causal path between treatment and outcome) — this blocks the very causal effect you're trying to measure. Getting this wrong causes either Simpson's Paradox (not conditioning on confounders) or underestimation (conditioning on mediators). The MNH example makes it concrete: baseline severity is a confounder (condition on it), quality of care improvement is a mediator (don't).

## Slide: The Numbers in Detail
This slide breaks down exactly how the composition effect works. 80% of CPAP cases come from high-burden countries, but only 30% of non-CPAP cases do. The two groups aren't comparable without stratification. In the high-burden stratum, CPAP improves survival from 61% to 68%. In the low-burden stratum, from 82% to 85%. The aggregated numbers are meaningless because they mix groups with fundamentally different baselines.

## Slide: The DAG That Generates Simpson's Paradox
This generalizes the lesson. Simpson's Paradox arises whenever a confounder creates a fork structure: the confounder causes both treatment assignment and the outcome. The resolution is always the same: condition on (stratify by) the confounder. The critical rule in the orange callout — always condition on confounders, never on mediators — is worth repeating multiple times. It's the single most important analytical rule in this chapter.

## Slide: Definition: The Prosecutor's Fallacy
Now we shift to the second trap. The Prosecutor's Fallacy confuses P(Evidence | Hypothesis) with P(Hypothesis | Evidence). The courtroom example makes it vivid: a 1-in-a-million DNA match doesn't mean there's a 1-in-a-million chance of innocence, because in a city of 5 million people, 5 people match. You need Bayes' rule and the base rate to convert one probability into the other. This error is ubiquitous in program evaluation and clinical diagnosis.

## Slide: MNH Example: Preeclampsia Screening
The preeclampsia screening example brings the fallacy into the MNH context. A health worker sees a positive test with 90% sensitivity and tells the patient there's a 90% chance of preeclampsia. This is wrong — 90% is the probability of a positive test *given* disease, not the probability of disease *given* a positive test. With 5% prevalence, most positive tests are false positives. This kind of error affects clinical decision-making every day.

## Slide: Bayes' Rule Calculation
Walk through the math slowly. P(positive) = 0.045 + 0.1425 = 0.1875 — about 18.75% of all women test positive. Then P(disease | positive) = 0.045 / 0.1875 ≈ 0.24. A positive test means only a 24% chance of preeclampsia, not 90%. The low base rate (5% prevalence) means the false positives vastly outnumber the true positives. This is why screening programs need to be evaluated with Bayes' rule, not just sensitivity and specificity.

## Slide: Visualizing the Fallacy
The natural frequency table makes it concrete. Out of 10,000 women, 500 have preeclampsia and 9,500 don't. Of the 1,875 positive tests, only 450 (24%) actually have the disease. The other 1,425 are false positives from the 9,500 healthy women. The prevalence (base rate) must be combined with the likelihood to produce the posterior. Ignoring the base rate is the essence of the Prosecutor's Fallacy.

## Slide: Cost-Effectiveness Data Across Countries
This table shows raw CPLS for three interventions across 8 countries. The temptation is to pick the lowest number — Country H, PPH bundle at $720. But the orange callout warns: low CPLS reflects a strong health system, not necessarily a larger causal impact. Country H's health system is already good, so interventions there are efficient but have less room for improvement. The marginal impact may be much larger in Country A despite its higher raw CPLS.

## Slide: Naive Ranking vs. Causal Ranking
This side-by-side comparison is the policy punchline. The naive ranking concentrates investment in countries with strong health systems. The causal ranking targets countries where the intervention's causal effect is greatest — accounting for baseline NMR, system capacity, population size, and existing coverage. The rankings barely overlap. Getting this wrong doesn't just waste money; it costs thousands of lives.

## Slide: Simpson's Paradox in Cost-Effectiveness
Another Simpson's Paradox example, this time with mortality rates. The PPH bundle appears worse than standard care in aggregated data (3.2% vs. 2.8% mortality). But stratified by health system strength, the bundle reduces mortality in both strata. The bundle is deployed disproportionately in weak-system countries where mortality is higher, which drives the misleading aggregated result.

## Slide: Policy Implication: The Next Funding Allocation
The practical payoff. Without causal reasoning, you allocate to Countries H and E (lowest raw CPLS) and save about 8,200 lives. With causal reasoning, you allocate to Countries A and B (highest marginal impact after adjustment) and save about 14,600 lives. Same budget, 6,400 additional lives saved. The orange callout notes this isn't hypothetical — misallocation due to Simpson's Paradox reasoning has been documented in HIV/AIDS, malaria, and vaccination programs.

## Slide: Interactive Exercise
A group exercise that asks students to apply the chapter's concepts to a concrete scenario. They need to determine where workforce training is more cost-effective at the margin, identify the confounding variable, draw the DAG, and make a recommendation with causal justification. This is the kind of analytical task they'll face in real consulting engagements.

## Slide: R Block 1: Simulating Simpson's Paradox
Live coding walkthrough. Students simulate MNH data with a confounder (country group) that drives both treatment assignment and outcomes, then see the paradox emerge in aggregated vs. disaggregated results.

## Slide: R Block 2: Visualizing Aggregated vs. Stratified
Live coding walkthrough. Side-by-side bar charts showing CPAP appearing harmful in the aggregated view but beneficial in both strata — a visual demonstration of Simpson's Paradox.

## Slide: R Block 3: Naive vs. Confounder-Adjusted Regression
Live coding walkthrough. The naive regression shows a negative CPAP coefficient; the adjusted regression shows a positive one. This demonstrates omitted variable bias — the statistical manifestation of Simpson's Paradox.

## Slide: R Block 4: Bayesian Network with bnlearn
Live coding walkthrough. Students build a Bayesian network that encodes the causal structure and run queries that correctly handle the conditioning, avoiding Simpson's Paradox by construction.

## Slide: R Block 5: Prosecutor's Fallacy Calculator
Live coding walkthrough. Students build a reusable Bayes' rule calculator for diagnostic tests and see how dramatically the positive predictive value changes with prevalence — 24% at 5% prevalence vs. 60% at 20% prevalence.

## Slide: Key Takeaways
Three core lessons. Simpson's Paradox comes from a confounder fork — always stratify by confounders, never by mediators. The Prosecutor's Fallacy confuses P(E|H) with P(H|E) — use Bayes' rule. In MNH cost-effectiveness, naive cross-country comparisons mislead because baseline severity and health system strength confound the treatment-outcome relationship. Causal adjustment saves thousands of lives.

## Slide: Looking Ahead
Next chapter we move from estimation to decision-making. Chapter 6 taught us how to correctly estimate causal effects; Chapter 7 teaches us how to use those estimates to choose optimal interventions under uncertainty. Decision trees, expected value of perfect information, and sensitivity analysis provide the tools for converting causal estimates into investment decisions.
