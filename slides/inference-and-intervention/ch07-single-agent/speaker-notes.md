# Speaker Notes — Chapter 7: Single-Agent Interventions

## Overview
This is the pivot point of the entire course. Chapters 1–6 were about figuring out what's going on — inference, diagnosis, understanding the system. Now we flip the question: given what we know, what should we *do*? We introduce influence diagrams, expected value calculations, the value of information, and the critical distinction between observing and intervening (the do-operator). By the end, students have a complete framework for choosing among MNH interventions under uncertainty.

## Slide: Learning Objectives
Five objectives that take students from passive analysis to active decision-making. We start by extending our causal models into influence diagrams (adding decisions and objectives to the mix), then learn how to compute expected value, quantify how much better information is worth, and understand the crucial difference between seeing that something is correlated and actually doing something about it. Everything culminates in a full MNH decision analysis.

## Slide: Chapter Overview
The five-step flow maps the chapter's logic. First we build the decision framework (influence diagrams), then the math for comparing options (expected value), then ask whether we should invest in learning more before deciding (value of information), then address the deepest conceptual issue — observing vs. intervening — and finally apply it all to a real MNH investment decision. The callout is the key message: we're shifting from "What is happening?" to "What should I do?"

## Slide: Two Modes of Causal Reasoning
This side-by-side comparison crystallizes the course's structure. Inference asks: given that we see high NMR, what do we think about staffing? Intervention asks: if we deploy CPAP, what happens to NMR? Same Bayesian network, completely different questions. The critical distinction in the orange callout — P(NMR | CPAP=Yes) ≠ P(NMR | do(CPAP=Yes)) — is worth spending time on. Observing that CPAP facilities have lower NMR is not the same as knowing that deploying CPAP will lower NMR. The first reflects existing correlations; the second requires causal reasoning.

## Slide: Why the Distinction Matters
The CPAP example makes the observe-vs-intervene distinction concrete. Facilities with CPAP have 30% lower NMR — but they also have better staff, training, and management. The observed 30% conflates the causal effect of CPAP with everything else that comes along with it. The true causal effect might be 12% — still valuable, but the naive number would lead you to overinvest in equipment and underinvest in the human factors that actually drive most of the association.

## Slide: Three Node Types in Influence Diagrams
Now we extend the toolkit. A Bayesian network has only chance nodes — uncertain variables. An influence diagram adds two more: decision nodes (rectangles, things we control) and objective nodes (hexagons, what we're trying to optimize). This is what makes the framework actionable. The callout at the bottom makes the progression clear: Bayesian network → inference, influence diagram → optimal decisions.

## Slide: A Simple Influence Diagram
This is the simplest possible MNH decision model. One decision (Deploy CPAP?), one chance variable (Neonatal Outcomes influenced by both CPAP and Baseline Severity), and one objective (Lives Saved). The key structural feature is that the arrow from the Decision to Outcomes is a *causal* effect — it represents what happens when we act. The arrow from Baseline Severity to Outcomes is a contextual influence that we don't control.

## Slide: Information Links
Information links are dashed arrows pointing into decision nodes. They don't represent causation — they represent what the decision-maker knows when they make their choice. The pilot results example is perfect: if leadership can observe pilot results before deciding whether to scale up, that information changes the optimal strategy. The presence or absence of information links is what separates "decide now" from "learn first, then decide."

## Slide: The Expected Value Framework
Here's the core math. Expected value is just the probability-weighted average of all possible outcomes. The CPAP deployment table shows three scenarios: equipment works with trained staff (50% chance, 2,400 lives), equipment works without trained staff (20% chance, 800 lives), and equipment failure (30% chance, 0 lives). Multiply each outcome by its probability and sum: EV = 1,360 lives. This is the number we compare against alternatives.

## Slide: Comparing Two Interventions
This is the decision point. CPAP deployment has an expected value of 1,360 lives at $14,706 per life. Workforce training has 1,920 lives at $10,417 per life. Workforce training wins on both dimensions. But the key caveat in the green callout is crucial: this assumes we know the probabilities correctly. What if we're wrong about the attrition rate? That leads us to the value of information.

## Slide: Decision Trees
The decision tree formalizes the expected value calculation as a procedure. Start at the objective node, work backward through chance nodes (computing expected values) and decision nodes (picking the best option). This "fold back" or "backward induction" procedure is the algorithm for solving any influence diagram. Students should recognize this as the same logic they'll use in Chapter 8 for multi-country allocation and Chapter 9 for game theory.

## Slide: Multi-Stage Decisions
Real MNH decisions aren't one-shot — they're sequential. The pilot → observe → scale-up structure reflects how programs actually work. The value of running a pilot depends entirely on how much it changes your subsequent decision. If you'd do the same thing regardless of pilot results, the pilot is worthless. If the pilot could genuinely swing you from one strategy to another, it's worth the $2M and 6 months.

## Slide: Expected Value of Perfect Information (EVPI)
EVPI answers a deceptively simple question: how much would it be worth to know the truth before deciding? Without info, we choose workforce training (EV = 1,920). With perfect info about attrition, we'd sometimes switch to CPAP (when attrition is high), giving EV = 2,112. The difference — 192 lives or about $2M — is the maximum we should pay for any information about attrition. This sets the ceiling for pilot program budgets.

## Slide: Expected Value of Sample Information (EVSI)
EVSI is the realistic version of EVPI. A pilot doesn't give you perfect information — it gives you an imperfect signal. The pilot changes your beliefs (updating probabilities) but doesn't eliminate uncertainty. The decision rule is clean: run the pilot if the EVSI exceeds the cost. The green callout explains when the pilot has value — it only matters when the signal could change your decision, which happens when the pilot reveals high attrition and you switch from workforce to CPAP.

## Slide: The do-Operator
Now we formalize the observe-vs-intervene distinction. do(X = x) means we force X to take value x, regardless of what would normally cause X. This is different from passively observing X = x. The two-column comparison makes it vivid: observing that a facility has CPAP means all correlations are intact (including confounders). Intervening to give a facility CPAP severs the incoming arrows — confounders are blocked. Only the second tells you the causal effect.

## Slide: Graph Surgery
Graph surgery is the mechanical procedure for computing do-expressions. To find P(Y | do(X=x)), you literally delete all arrows pointing into X in the DAG, then compute probabilities in the modified graph. The side-by-side DAGs show this clearly: in the original, Resources confounds CPAP and NMR. After surgery (cutting Resources → CPAP), the only remaining path is the direct causal effect CPAP → NMR. This is the computational backbone of do-calculus.

## Slide: The Decision Context
Now we apply everything to a full MNH scenario. The program must choose between three strategies for a new target country: CPAP deployment, workforce training, or a split. This is realistic — program leaders face exactly these kinds of portfolio allocation decisions. The three-strategy setup lets us see how diversification (the split) compares to concentration.

## Slide: Building the Influence Diagram
The full influence diagram has the decision node (Strategy Choice) flowing through Equipment Availability and Staffing Adequacy to Quality of Care and then Lives Saved. Government co-financing enters as an uncertain variable affecting both equipment sustainability and staff retention. The 60/40 split between low and high co-financing is the dominant source of uncertainty — and it's the variable the program can least control.

## Slide: Expected Value Analysis
The numbers tell a surprising story. CPAP-only has the lowest EV (1,840 lives). Workforce has more (2,040). But the split strategy wins with 2,080 — and importantly, it has the lowest variance. The split performs reasonably under both co-financing scenarios. This is portfolio diversification applied to public health: don't put all your eggs in one basket when facing uncertain government commitment.

## Slide: Sensitivity Analysis
This slide asks: at what point does the uncertainty actually change our decision? If we believe there's more than a 44% chance of high government co-financing, workforce-only becomes optimal (higher upside when the government cooperates). Below 44%, the split's lower variance makes it safer. The practical implication is in the green callout: the program should focus advocacy efforts on securing government commitments, because that's what determines the optimal strategy.

## Slide: R: Expected Value Calculation
Live coding walkthrough. Students implement the three-strategy expected value computation in R, confirming the split's advantage.

## Slide: R: EVPI Calculation
Live coding walkthrough. Students compute EVPI — the value of learning government co-financing intentions before committing funds.

## Slide: R: Sensitivity Analysis Visualization
Live coding walkthrough. Students create a sensitivity plot showing how expected lives saved varies with P(High co-financing) for each strategy, identifying the crossover point.

## Slide: R: Graph Surgery with bnlearn
Live coding walkthrough. Students implement graph surgery in bnlearn by comparing the original confounded model with the intervened model where incoming arrows to CPAP are severed.

## Slide: R: Tornado Diagram
Live coding walkthrough. Students build a tornado diagram showing which parameters most affect the split strategy's expected value, helping prioritize what to learn more about.

## Slide: Key Takeaways
Four essential lessons. Influence diagrams extend causal models to support decision-making. Expected value and EVPI give us principled tools for comparing options and valuing information. The do-operator distinguishes correlation from causation at the deepest level. And diversification — splitting your investment — often beats concentration when facing uncertainty. These tools transform causal understanding into actionable investment decisions.

## Slide: Looking Ahead
Chapter 8 scales up. Instead of one country with three strategies, we face ten countries with uncertain co-financing, sequential pilot-then-scale decisions, and the real cost of delay measured in lives lost during the waiting period. The single-agent framework from this chapter becomes the workhorse for multi-country resource allocation.
