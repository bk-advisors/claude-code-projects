# Speaker Notes — Chapter 10: Data-Driven Causal Modeling

## Overview
This is the capstone chapter that closes the loop. Throughout Chapters 1–9, we assumed we knew the causal structure — we built DAGs from expert interviews and theory. Chapter 10 asks the hard question: what if we don't know the DAG? Can we *discover* it from data? The answer is nuanced: data can reveal which variables are connected and sometimes identify causal direction (especially through collider patterns), but multiple DAGs can produce the same statistical distribution. The chapter teaches students to combine data-driven discovery with domain expertise, use instrumental variables to overcome confounding, and avoid the regression pitfalls that plague naive analyses. By the end, students have the complete toolkit: from qualitative modeling through decision analysis to data-driven validation.

## Slide: Learning Objectives
Five objectives that span the gap between statistics and causation. Distinguishing causal models from probabilistic models is the philosophical foundation. Markov equivalence is the key limitation — why data alone can't always resolve causal direction. Structure learning algorithms (PC and hill climbing) are the tools for discovery. Instrumental variables are the workaround when confounders are unobserved. And the control variable decision guide — good controls vs. bad controls — is the practical takeaway for anyone running regressions on MNH data.

## Slide: Chapter Overview
The five-step flow captures the chapter's progression. We start with the fundamental distinction between causation and probability, confront the limits of what data can tell us (Markov equivalence), learn algorithmic tools for DAG discovery (structure learning), find a workaround for hidden confounders (instrumental variables), and close with a practical guide to causal regression that ties everything together. The callout frames the central question: throughout this course we assumed we knew the causal structure — what if we don't?

## Slide: Two Fundamentally Different Questions
This is the deepest conceptual point in the chapter. A statistical question asks about the joint distribution — what correlates with what. A causal question asks what happens under intervention — what *causes* what. The key differences: statistical associations are symmetric (knowing A tells you about B and vice versa), but causation is asymmetric (causing A affects B, not the other way around). The red callout states the fundamental problem: multiple causal structures can produce the same joint distribution. Data alone can't always tell them apart.

## Slide: Three DAGs, One Distribution
This makes the problem concrete with three variables. The chain S → E → M, the fork S ← E → M, and the reverse chain S ← E ← M all encode the same conditional independence: S ⊥ M | E. You could collect a million data points and never distinguish between these three structures using observational data alone. The definition box formalizes this as "observational indistinguishability" — DAGs encoding the same conditional independencies are Markov equivalent.

## Slide: When *Can* Data Distinguish DAGs?
Here's the good news: colliders are identifiable. The structure S → E ← M has a unique statistical signature: S and M are marginally independent but become dependent when you condition on E. No chain or fork produces this pattern. So if you observe this pattern in data, you've identified a collider — and with it, the direction of both arrows. This is why colliders are so important for structure learning: they're the only triplet structure where data can resolve direction.

## Slide: Equivalence Classes
A Markov equivalence class is the set of all DAGs encoding the same conditional independencies. It's represented by a CPDAG — a graph with both directed and undirected edges. Directed edges appear where all DAGs in the class agree on direction (often around colliders). Undirected edges appear where DAGs disagree. The MNH example shows that Quality → NMR is identifiable (directed in all equivalent DAGs), but the direction between Staffing and Equipment remains ambiguous from data alone.

## Slide: Implications for MNH Analysis
The practical warning is crucial: when we learn a DAG from DHIS2 data, we learn an equivalence class, not a unique DAG. Some edges are certain, others are ambiguous. To resolve ambiguity, we need domain knowledge (experts say training causes competency), temporal ordering (past can't be caused by future), experimental data (RCTs), or instrumental variables. The strategy for MNH programs is hybrid: learn the skeleton from DHIS2 data, then use domain expertise and temporal ordering to orient ambiguous edges.

## Slide: Two Approaches to Learning DAGs
Two main families of algorithms. Constraint-based (PC algorithm) tests conditional independencies to build the skeleton, then orients edges using collider rules. It's statistically principled and fast for sparse graphs but sensitive to errors in individual tests. Score-based (hill climbing) searches over DAG space optimizing a scoring function like BIC. It's more robust to individual test errors but can get stuck in local optima. In practice, many analysts run both and compare results for robustness.

## Slide: The PC Algorithm in Detail
The PC algorithm works in five stages. Start with the complete graph (every node connected to every other). Remove edges when conditional independence is detected, starting with marginal independence (conditioning set size 0) and working up to larger sets. Then find v-structures (colliders) by checking separating sets: if X—Z—Y with no X—Y edge, and Z wasn't in the separating set, orient as X → Z ← Y. Finally, apply Meek's rules to propagate orientations without creating new colliders or cycles. The output is a CPDAG.

## Slide: Score-Based Learning: BIC
The BIC score balances two terms: how well the DAG explains the data (fit) and how many parameters it uses (complexity penalty). The complexity penalty prevents overfitting — it discourages adding edges that don't substantially improve the model. Hill climbing with BIC is the most commonly used method in practice, implemented as `hc()` in the bnlearn package. The key insight is that BIC automatically trades off explanatory power against model complexity.

## Slide: Assumptions and Limitations
Both methods rest on strong assumptions. Causal sufficiency (no hidden confounders) is almost certainly violated in DHIS2 data — we don't observe community-level factors, cultural practices, or household income. Faithfulness assumes no exact cancellation of causal effects. Correct functional form matters for independence tests. Sufficient sample size is needed, especially for constraint-based methods. The red callout is the most important message: learned DAGs should be treated as hypotheses, not ground truth. They're starting points for investigation, not final answers.

## Slide: The Endogeneity Problem
Now we shift to instrumental variables. The motivating question is clean: does midwife density cause lower NMR? The problem: district wealth is a confounder that drives both midwife density (wealthy districts attract more midwives) and NMR (wealthy districts have better outcomes for many reasons). Naive regression of NMR on midwife density gives a biased estimate because it conflates the causal effect of midwives with the effect of wealth.

## Slide: The IV Solution
An instrumental variable Z must satisfy three conditions: relevance (Z predicts the treatment), exclusion (Z affects the outcome only through the treatment), and independence (Z is unrelated to confounders). The MNH instrument — distance to nearest training college — is compelling. Districts closer to training colleges have more midwives (relevance), the college's location doesn't directly affect neonatal health (exclusion), and college placement was based on historical/political factors unrelated to current district wealth (independence). This allows us to isolate the causal effect.

## Slide: Two-Stage Least Squares (2SLS)
The mechanics of IV estimation in two stages. Stage 1 predicts midwife density from distance to training college, extracting only the variation driven by geography (exogenous). Stage 2 regresses NMR on the *predicted* midwife density, using only the "clean" variation that's free from wealth confounding. The intuition is powerful: we're comparing districts that differ in midwife density *because of* training college proximity — not because of wealth. This is the closest we can get to an experiment without actually running one.

## Slide: IV Assumptions: When They Fail
Each assumption can fail in ways that matter. If distance barely predicts midwife density (weak instrument), estimates become imprecise and biased. If college towns also have better hospitals (exclusion violation), the IV captures hospital effects too. If colleges were built in wealthy districts (independence violation), the IV is confounded just like OLS. The orange callout flags the key asymmetry: the exclusion restriction is *untestable* — it relies on domain knowledge. The relevance condition *is* testable via the first-stage F-statistic (F > 10 is the rule of thumb).

## Slide: Good Controls vs. Bad Controls
This is one of the most practically important slides in the entire course. Confounders (common causes of treatment and outcome) should be controlled for — it removes the backdoor path. Mediators (variables on the causal path) should NOT be controlled for — it blocks the causal effect you're trying to measure. The two-column layout makes the distinction vivid: controlling for a confounder reduces bias, controlling for a mediator creates bias.

## Slide: The Collider Bias Trap
Controlling for a collider creates a spurious association that didn't exist before. Staffing and Equipment are independent (neither causes the other), but Quality Rating is caused by both. Among facilities rated "Good" (conditioning on the collider), those with low staffing must compensate with better equipment — creating a *negative* association between Staffing and Equipment that's entirely an artifact of the conditioning. The rule is simple: never control for a descendant of the treatment unless you specifically want the controlled direct effect.

## Slide: Summary: Control Variable Decision Guide
This table should be photocopied and taped to every program analyst's desk. Five variable types, five different recommendations. Confounders: control (blocks backdoor). Mediators: don't control (blocks causal path). Colliders: don't control (opens spurious path). Instruments: use in 2SLS, not as a control. Precision variables (causes of Y only): control (reduces variance without bias). The key principle in the definition box: use your DAG to determine what to control for. Regression without a causal model is flying blind.

## Slide: The DHIS2 Data Opportunity
DHIS2 is used across MNH program target countries, providing monthly facility-level data on staffing, equipment, deliveries, C-sections, neonatal outcomes, referrals, and drug stock-outs. With ~3,000 facilities across 10 countries and 5 years of monthly data, we have roughly 180,000 facility-months to work with. The question is whether we can discover causal structure from this observational data — and the answer, with appropriate caveats, is yes.

## Slide: Candidate Causal Variables
Eight variables selected for structure learning: Staffing Adequacy, Equipment Index, Drug Availability, Training Completion, C-Section Rate, Referral Rate, Delivery Volume, and NMR. Each comes from DHIS2 modules or program records. These represent the key pathways through which MNH investments affect outcomes — the same pathways we've been modeling qualitatively since Chapter 2.

## Slide: Expected Causal Structure (Expert Prior)
The expert-elicited DAG shows the expected causal relationships: Training → Staffing → Referral Rate, Drug Availability → C-Section Rate, Staffing → C-Section Rate, and multiple paths converging on NMR. The goal is to compare this expert prior with the data-driven DAG from structure learning. Where they agree, we have high confidence. Where they disagree, we need to investigate further. This hybrid approach — combining expert knowledge with data — is the recommended workflow.

## Slide: R Block 1: Simulate DHIS2-Like Data
Live coding walkthrough. Students simulate a 3,000-facility dataset from a known causal structure, creating realistic DHIS2-like variables with appropriate distributions and causal relationships.

## Slide: R Block 2: PC Algorithm — Learn Structure from Data
Live coding walkthrough. Students apply the PC algorithm to the simulated data, compare the learned CPDAG against the true DAG using Structural Hamming Distance, and count true positives, false positives, and false negatives.

## Slide: R Block 3: Score-Based Learning (Hill Climbing)
Live coding walkthrough. Students apply hill climbing with BIC to the same data, compare with both the PC result and the true DAG, and visualize all three structures side by side.

## Slide: Interpreting Structure Learning Results
The practical interpretation guide. Skeletons (which nodes are connected) are usually well-recovered with n > 1,000. Edge directions are harder — many edges remain undirected in the CPDAG. Collider structures are the best-identified patterns. Long chains are hardest because each intermediate test adds error. The strategy: use learned skeleton plus expert orientation plus temporal ordering to build the final causal model.

## Slide: R Block 4: Instrumental Variable Estimation
Live coding walkthrough. Students simulate an IV scenario (midwife density confounded by district wealth, with distance to training college as instrument), then compare naive OLS (biased), controlled OLS (correct if wealth is observed), and 2SLS IV estimation (correct even without observing wealth).

## Slide: R Block 5: Good vs. Bad Controls in Regression
Live coding walkthrough. Students demonstrate two critical mistakes: controlling for a mediator (Training → Competency → NMR) underestimates the total effect of training, and conditioning on a collider (Staffing → Quality ← Equipment) creates a spurious negative correlation between staffing and equipment.

## Slide: Putting It All Together: The MNH Workflow
The five-step workflow integrates the entire course. Learn structure from DHIS2 data (this chapter). Orient ambiguous edges with expert knowledge (Chapters 2–3). Validate by testing implied independencies against data. Estimate causal effects using IV or adjusted regression. Use the model for intervention decisions (Chapters 7–8). This workflow combines data-driven discovery with expert knowledge, quantitative modeling, and decision analysis — the full toolkit.

## Slide: Key Takeaways
Four core lessons. Data alone cannot determine causation — Markov equivalence means multiple DAGs fit the same data, and domain knowledge is essential. Structure learning discovers candidate DAGs, with colliders being the key to orientation. Instrumental variables overcome confounding when you can't control for confounders directly. And not all controls are good controls — the DAG must guide your regression specification to avoid mediator adjustment and collider bias.

## Slide: Looking Ahead: The Complete Toolkit
The two-column summary puts the entire course in perspective. The left column lists what each chapter contributed: qualitative DAGs (1–3), Bayesian networks (4–5), reasoning pitfalls (6), decision analysis (7), resource allocation (8), game theory (9), and data-driven discovery (10). The right column maps these to the MNH analyst's workflow: build DAGs from interviews, quantify with data, avoid traps, make allocation decisions, anticipate strategic responses, and validate with new data. This is the complete cycle of causal reasoning for global health.

## Slide: Course Summary
The central message of the entire course: causal models are not academic abstractions — they're practical tools for answering the questions that matter most in global health. Where should we invest? What should we do? How do we know it will work? The combination of qualitative modeling (structure), quantitative analysis (parameters), and decision theory (action) provides a complete framework for evidence-based intervention design. For MNH program managers, this toolkit enables rigorous allocation of pooled funding with clear reasoning about *why* each investment is expected to save lives.
