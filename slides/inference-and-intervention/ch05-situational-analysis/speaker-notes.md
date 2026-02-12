# Speaker Notes — Chapter 5: Situational Analysis

## Overview
This is where we put the Bayesian network engine into gear. Chapter 4 showed us how to build the model forward — specifying how causes produce effects. Chapter 5 runs it *backwards*: we observe outcomes (like high NMR in a district) and use Bayes' rule to infer what's most likely going wrong upstream. We work through each of the three triplet structures quantitatively and then apply the full machinery to a realistic district diagnosis. The star of the chapter is the "explaining away" effect in collider structures — the most counterintuitive and practically important result in causal reasoning.

## Slide: Learning Objectives
Five objectives that move from mechanics to application. Computing marginals is the warm-up, then updating beliefs with evidence (Bayes' rule in action), then inference in each triplet structure to see how information flows differently in each. The explaining away phenomenon gets special billing because it surprises even experienced analysts. The chapter culminates in a full district diagnosis — exactly what a program analyst would do with DHIS2 data.

## Slide: Chapter Overview
The five-step flow mirrors the diagnostic workflow. First, establish baseline expectations (marginals). Then, observe evidence and update beliefs. Then understand how information flows through different structures. The explaining away effect gets its own step because it's so counterintuitive. Finally, put it all together in a district diagnosis. The core insight in the callout is worth emphasizing: this chapter reverses the direction from Chapter 4 — from effects back to causes.

## Slide: From Forward to Backward Reasoning
This is the conceptual pivot of the first half of the course. Forward reasoning asks "if staffing is low, what happens to NMR?" — that's prediction. Backward reasoning asks "we see high NMR, what does that tell us about staffing?" — that's diagnosis. Both use the same Bayesian network, just in opposite directions. Every program analyst who looks at DHIS2 data and tries to figure out why a district is underperforming is doing backward reasoning, whether they know it or not. This chapter makes it rigorous.

## Slide: The MNH Inference Model
We use a simplified model throughout: Staffing and Equipment feed into Quality, which feeds into NMR. Training is added later for the full diagnosis. The priors come from Chapter 4: 40% of facilities have adequate staffing, 35% have equipment available, 50% have completed training. These numbers represent our baseline beliefs before seeing any district-specific evidence.

## Slide: What Is a Marginal Probability?
The marginal probability is what you believe when you have no evidence at all. P(NMR=High) computed by summing over all possible staffing and equipment combinations gives you the baseline: the probability of high NMR in a randomly selected district. Think of it as the "default expectation" before any data comes in. The intuition is just weighted averaging — you weight each scenario by how likely it is.

## Slide: Computing Marginal NMR
Here are the CPTs we'll use throughout the chapter. The Quality CPT shows the full interaction between Staffing and Equipment — ranging from 90% good quality (both favorable) to 15% (both unfavorable). The NMR CPT maps quality to mortality: 15% chance of high NMR with good quality, 70% with poor quality. Students should get comfortable with these tables because we'll use them in every subsequent calculation.

## Slide: Marginal P(NMR=High): The Calculation
Walk through this computation step by step. We sum over all four Staffing × Equipment combinations, weighting each by the joint probability of that combination. The result is P(NMR=High) = 0.455 — a 45.5% baseline probability. This is the number we'll compare all our posteriors against. Every time we observe evidence, we'll ask: does this push the probability up or down from 45.5%?

## Slide: What Does "Evidence" Mean?
Evidence means learning the actual state of a variable — "conditioning" in probability language. Before evidence, P(Staffing=Low) = 0.60 (our general prior). After observing NMR=High in a specific district, we want P(Staffing=Low | NMR=High). That's a backward inference: using a child node's value to update beliefs about a parent. This is exactly the situational assessment task every program manager faces.

## Slide: Bayes' Rule: The Engine of Updating
This is the core computation. We need P(NMR=High | Staffing=Low) — which requires marginalizing over Equipment and Quality — divided by P(NMR=High). The result is P(Staffing=Low | NMR=High) = 0.724. Observing high mortality shifts our belief about low staffing from 60% to 72.4% — a 12.4 percentage point increase. High NMR is evidence that staffing is probably inadequate.

## Slide: The General Pattern of Updating
This table is the diagnostic payoff. After observing high NMR, *all* root causes shift toward their "bad" states. But they don't shift equally: staffing moves the most (+12.4 pp), equipment next (+9.1 pp). This tells the program analyst where to investigate first — staffing is the most informative variable to check. The green callout makes the point: the variable with the largest posterior shift has the strongest causal connection to the observed outcome in this model.

## Slide: Serial Structure: The Chain
Now we examine each triplet structure quantitatively. The chain Training → Competency → Mortality lets information flow from training to mortality through competency. If you observe high mortality and don't know competency, you can infer something about training (probably not completed). But once you *know* competency, training becomes irrelevant for predicting mortality. The chain gets blocked.

## Slide: Serial: CPTs and Priors
These CPTs define the serial chain. Training completion gives an 80% chance of high competency (vs. 30% without training). High competency gives an 85% chance of low mortality (vs. 35% with low competency). The marginal P(Competency=High) = 0.55. Students should verify this calculation to build fluency.

## Slide: Serial: Worked Bayesian Calculation
The full calculation: P(Training=Completed | Mortality=High). We first compute P(Mortality=High) = 0.375, then P(Mortality=High | Training=Completed) = 0.250, then apply Bayes' rule to get 0.333. High mortality shifts our belief about training completion from 50% down to 33.3%. High mortality is evidence *against* training having been completed — which makes intuitive sense.

## Slide: Serial: Blocking by Conditioning
Here's the blocking test. If we also know that Competency is Low, does training still tell us about mortality? No — P(Training=Completed | Mortality=High, Competency=Low) = P(Training=Completed | Competency=Low) = 0.222. Mortality becomes irrelevant once competency is known. This is the chain being blocked in action. The practical takeaway: if you can directly measure competency, you don't need mortality data to assess training effectiveness.

## Slide: Diverging Structure: The Fork
The fork PPH Detection ← Workforce Quality → CPAP Usage creates a spurious correlation between PPH detection and CPAP usage. They appear correlated because workforce quality drives both — competent staff are good at detecting PPH *and* good at using CPAP. But improving PPH detection protocols won't fix CPAP usage. You need to address the common cause: workforce quality.

## Slide: Diverging: CPTs and Setup
The CPTs make the fork concrete. Good workforce quality gives 90% chance of good PPH detection and 85% chance of proper CPAP usage. Poor quality drops these to 35% and 25%. The marginals: P(PPH=Good) = 0.598, P(CPAP=Proper) = 0.520. These baselines are what we'll update against.

## Slide: Diverging: Inference from One Child to Another
Here's the fork in action. We observe poor PPH detection and ask: what does this tell us about CPAP usage? Step 1: update Quality given PPH=Poor — P(Quality=Good) drops from 45% to 11.2%. Step 2: use updated Quality to predict CPAP — P(CPAP=Proper) drops from 52.0% to 31.7%. Information flowed from one effect to another through the common cause, even though there's no direct causal link. This is confounding in action.

## Slide: Diverging: Blocking by Conditioning on Common Cause
Once we know Quality is Good, PPH detection tells us nothing about CPAP usage. P(CPAP=Proper | PPH=Poor, Quality=Good) = P(CPAP=Proper | Quality=Good) = 0.85. The fork is blocked. The management implication is in the green callout: if you can directly measure workforce quality, you don't need to infer it from proxy indicators. Direct measurement gives sharper diagnoses.

## Slide: Converging Structure: The Collider
Here's the counterintuitive one. Staffing → Quality ← Equipment is a collider. Staffing and Equipment are *independent* — they're separate investment decisions. But once we observe their common effect (Quality), they become dependent. This is the opposite of chains and forks, where conditioning *blocks* the path. With colliders, conditioning *opens* a path that wasn't there before.

## Slide: Explaining Away: The Core Idea
The scenario makes it click. You observe good workforce quality in a district — surprising. Could be good staffing, good equipment, or both. Now you learn that staffing is actually Low. What happens to your belief about equipment? It must be Available — because *something* has to explain the good quality, and staffing can't be the explanation. Equipment "explains away" what staffing cannot. This is exactly how diagnostic reasoning works in practice: ruling out one cause strengthens the case for the other.

## Slide: Converging: Worked Calculation
Walk through the math step by step. First, observing Quality=Good raises P(Equipment=Available) from the prior of 35% to 51.8%. Good quality is consistent with good equipment. Then, adding the observation that Staffing=Low pushes it further to 64.2%. Equipment must be compensating. The three-row table — prior 35%, after Quality=Good 51.8%, after also Staffing=Low 64.2% — shows explaining away in action.

## Slide: Converging: The Explaining Away Effect
The key takeaway table shows the progressive belief shift. Notice the explaining away effect: once we know quality is good, learning that staffing is low *increases* our belief in equipment availability. In the other structures, this doesn't happen — in chains and forks, conditioning on the middle node blocks the path. In colliders, conditioning on the middle node opens it. This asymmetry is the single most important distinction students need to internalize.

## Slide: The Diagnostic Scenario
Now we put it all together. District Mwanga reports NMR of 35 per 1,000 — well above the national average. We have no direct observations of staffing, equipment, training, or quality. We only have the NMR data and our national-level causal model with CPTs. Our task: use Bayesian inference to update beliefs about all upstream variables and identify the most likely root cause.

## Slide: Step 1: Establish the Full Model
We expand the model to include Training as a third root node, giving us a 5-node Bayesian network. The extended Quality CPT now has 8 rows (2³ parent combinations). The best-case scenario (all three parents favorable) gives 95% good quality; the worst case gives just 8%. This range shows how dramatically the parent configuration matters.

## Slide: Step 2: Compute Posterior Probabilities
The results table is the diagnostic output. After observing NMR=High, all three root causes shift toward their "bad" states. Staffing shifts the most (+11.0 pp), Equipment next (+8.8 pp), Training least (+7.3 pp). This ranking tells the country director where to investigate first: staffing is the variable most likely to be in a bad state. The orange callout highlights this: staffing should be the first thing to check in District Mwanga.

## Slide: Step 3: Identify the Most Likely Configuration
Which specific combination of root causes is most probable? The most likely diagnosis: all three in their bad state (Low staffing, Unavailable equipment, Training not completed), with a posterior probability of 28.4%. This is 2.8 times more likely than the next-best configuration. In plain language: if NMR is high, the most probable explanation is that everything is going wrong simultaneously. This makes sense — each bad state compounds the others.

## Slide: Step 4: Compare with a "Healthy" District
This comparison is powerful. In District Songea (NMR=Low), all root causes shift toward their *good* states — the mirror image of Mwanga. The side-by-side comparison lets the country director see both what's going wrong (Mwanga) and what's going right (Songea). The same framework diagnoses problems and identifies successes. Both directions inform resource allocation.

## Slide: R Block 1: Build a BN with CPTs
Live coding walkthrough. Students build the full 5-node Bayesian network with all CPTs defined as arrays.

## Slide: R Block 2: Query with Evidence
Live coding walkthrough. Students run multiple queries — marginal P(NMR=High), posterior given single evidence, posterior given multiple evidence — to see how beliefs update.

## Slide: R Block 3: Compare Posterior vs. Prior
Live coding walkthrough. Students write a function that computes posteriors for all root nodes given NMR evidence, and compare Mwanga (NMR=High) vs. Songea (NMR=Low).

## Slide: R Block 4: Visualize Belief Updating
Live coding walkthrough. Students create a grouped bar chart showing prior vs. posterior probabilities for each root node, making the belief shifts visually obvious.

## Slide: R Block 5: Full District Diagnosis Workflow
Live coding walkthrough. Students build a reusable diagnosis function that takes any evidence set and returns prioritized root causes with posterior shifts.

## Slide: Key Takeaways
Four things to remember. Marginal probabilities give baseline expectations. Bayes' rule updates those beliefs when evidence arrives, with staffing showing the largest shift in our model. The three structures determine information flow differently. And explaining away — the collider phenomenon — is the most counterintuitive and practically important pattern. When two independent causes compete to explain a common effect, confirming one reduces belief in the other.

## Slide: Looking Ahead
Next chapter tackles two dangerous analytical pitfalls: Simpson's Paradox (when aggregated data reverses the true causal effect) and the Prosecutor's Fallacy (confusing P(Evidence|Hypothesis) with P(Hypothesis|Evidence)). Both are directly relevant to how MNH programs evaluate their country portfolios and make resource allocation decisions.
