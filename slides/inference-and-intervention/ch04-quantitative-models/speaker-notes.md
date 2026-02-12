# Speaker Notes — Chapter 4: Quantitative Causal Models

## Overview
This is where the course shifts from "drawing arrows" to "doing math." We take the qualitative DAGs from Chapters 2-3 and attach probability tables to every node, transforming them into Bayesian networks that can compute actual probabilities. The key new tools are conditional probability tables (CPTs) and Bayes' rule. By the end, students will be able to answer questions like "What is the probability of high neonatal mortality given that a facility has low staffing and no CPAP?" — and they'll understand why that's a fundamentally different question from "What happens if we *give* a facility adequate staffing?"

## Slide: Learning Objectives
Five objectives that build toward the Bayesian network. We start with probability basics (distributions, axioms), move to conditional probability and CPTs, learn Bayes' rule for updating beliefs, understand the Causal Markov Condition that makes everything computationally tractable, and finish by building a working Bayesian network in R. Each piece is necessary for the next.

## Slide: Why Structure Alone Is Not Enough
This motivates the whole chapter. Qualitative models told us *which* variables influence which, and in *what direction*. But they couldn't tell us *how much*. How likely is high NMR if staffing is low? Which intervention saves more lives? To answer these questions, we need numbers — specifically, probability distributions. The orange callout box lists exactly the questions that qualitative models can't answer: "how much," "how likely," "which has the largest impact." Those are the questions this chapter equips students to answer.

## Slide: The Quantitative Upgrade
The equation is simple: Qualitative DAG + Probability Tables = Bayesian Network. The MNH example makes it concrete. Qualitatively, we know Staffing → Quality → NMR. Quantitatively, if P(Staffing = Adequate) = 0.40 and P(Quality = Good | Staffing = Adequate) = 0.80, we can *compute* P(NMR = High). Now we're not just reasoning about direction — we're calculating exact probabilities.

## Slide: Variable States
Before we can assign probabilities, we need to define what values each variable can take. The rule is MECE: mutually exclusive (only one state at a time) and collectively exhaustive (covers all possibilities). We discretize continuous variables — NMR becomes {High, Low} instead of an exact number. This is a modeling choice that trades precision for tractability. It's common practice in applied Bayesian networks and it works well when you care about categories of outcomes rather than exact numbers.

## Slide: Events: Sets of States
Events are the building blocks of probability statements. A simple event is just a variable in a specific state — "Staffing = Adequate." A compound event combines simple events — "Adequate staffing AND CPAP available." The complement rule is practically useful: if P(Adequate) = 0.40, then P(Low) = 0.60 without any additional information needed. Students should be comfortable with intersection, union, and complement before we move forward.

## Slide: Probability Axioms
These three axioms — non-negativity, normalization, and additivity — are the foundation everything else builds on. Most students have seen these before, but it's worth emphasizing the consequences: complement rule, boundedness between 0 and 1, and the requirement that state probabilities sum to 1. These aren't just mathematical niceties — violating them in a model (which is easy to do when eliciting expert probabilities) creates contradictions.

## Slide: Frequency vs. Subjective Probability
This distinction matters enormously for MNH work. Frequentist probability comes from data — "40% of facilities have adequate staffing" based on a facility survey. Subjective probability comes from expert judgment — "I believe there's a 70% chance this district reduces NMR by 2030." In practice, we use both. CPTs combine survey data where it's available with expert judgment where data is sparse. In data-limited settings like sub-Saharan Africa, subjective priors aren't a weakness — they're a necessary and valuable input.

## Slide: MNH Example: Marginal vs. Conditional Probability
This example illustrates the difference between marginal and conditional probability using real-world numbers. The marginal probability of neonatal death is about 25 per 1,000 live births. But the conditional probability given preterm birth is about 100 per 1,000 — four times higher. This tells us preterm birth is a strong risk factor. But here's the causal thinking question: is it a *cause*, or is it a marker for other causes like maternal health and facility quality? That question requires a causal model, not just conditional probabilities.

## Slide: Definition and Interpretation
The formula P(A|B) = P(A ∩ B) / P(B) is the foundation of everything in this chapter. The intuition is straightforward: "among the cases where B is true, what fraction also have A?" The crucial distinction at the bottom of the slide — P(NMR=High|Staffing=Low) vs. P(Staffing=Low|NMR=High) — is one that trips up even experienced analysts. These are *not* the same number, and confusing them leads to serious errors in diagnosis and decision-making.

## Slide: Stochastic Independence
Independence means knowing one variable tells you nothing about the other. We test it by checking whether P(A|B) = P(A). In the MNH example, P(NMR=High) overall is 0.35, but conditional on adequate staffing it's 0.15 and conditional on low staffing it's 0.55. Since these aren't equal, staffing and NMR are not independent — staffing is informative about mortality. This is exactly what our causal model predicts, since there's an open path between them.

## Slide: Conditional Probability Tables (CPTs)
CPTs are the quantitative heart of a Bayesian network. Each CPT lists P(Child | Parents) for every combination of parent states. The Quality of Care CPT has four rows — one for each combination of Staffing × CPAP. Every row sums to 1 because it's a conditional distribution. Students should spend time reading this table: when staffing is adequate and CPAP is available, there's an 85% chance of good quality. When both are absent, only 20%. That's the quantitative version of what we knew qualitatively.

## Slide: MNH CPT: Neonatal Outcome Given CPAP and Training
This CPT quantifies the combined effect of equipment and training on neonatal survival. The headline number: survival ranges from 96% (both available) to 70% (neither available) — a 26 percentage point gap. That's the quantitative payoff of the People + Products investment. The orange note reminds students that while these numbers are illustrative, they're grounded in the literature. In real applications, CPTs would come from facility-level data, expert elicitation, or both.

## Slide: The Factoring Rule
The chain rule P(X,Y) = P(X|Y) × P(Y) is how we compute joint probabilities from conditional ones. The example calculates P(Low Staffing AND Poor Quality) = 0.65 × 0.60 = 0.39 — about 39% of facilities have both problems simultaneously. This is the basic building block: start with marginals, apply CPTs, multiply. Software automates this, but students need to understand the mechanics to interpret results correctly.

## Slide: Joint Probability Tables
A joint probability table shows every combination of two variables. The key reading skill: cell values are joint probabilities, row and column totals are marginals, and the grand total is always 1.00. The example shows how staffing and quality co-occur: 28% of facilities are both well-staffed and good quality, 39% are both poorly staffed and poor quality. The marginals reveal that 51% of facilities have poor quality overall — a grim baseline.

## Slide: Computing Joint Distributions from CPTs
The three-step procedure — start with marginals, apply CPTs, multiply — is the forward computation engine of any Bayesian network. Students should trace through the example: P(Adequate, Good) = P(Good | Adequate) × P(Adequate) = 0.70 × 0.40 = 0.28. This is what the software does under the hood, and understanding it makes debugging much easier.

## Slide: MNH Example: Three-Variable Joint Distribution
This worked example shows the full computation across three variables. The key result: overall P(Survival) = 87.4%. And if training coverage increased from 45% to 80%, P(Survival) rises to 91.4% — an additional 40 lives saved per 1,000 births. This is the kind of quantitative policy analysis that becomes possible once you have a Bayesian network. You can answer "what if" questions with specific numbers.

## Slide: Derivation from Conditional Probability
Bayes' rule is derived from two different ways of writing the same joint probability. The formula itself is simple: P(A|B) = P(B|A) × P(A) / P(B). What makes it powerful is what it *does*: it lets you flip the direction of conditioning. If you know P(Evidence | Cause), Bayes' rule gives you P(Cause | Evidence). This is the fundamental operation of situational assessment — reasoning backward from what you observe to what is likely true.

## Slide: The Terminology of Bayes' Rule
Four terms to internalize: prior (what you believed before), likelihood (how probable the evidence is if your hypothesis is true), posterior (your updated belief), and marginal likelihood (normalizing constant). The key insight: Posterior is proportional to Likelihood × Prior. Strong evidence (high likelihood ratio) shifts the posterior far from the prior. Weak evidence leaves the posterior close to the prior. This is how rational belief updating works.

## Slide: Computing P(B): The Law of Total Probability
The denominator of Bayes' rule requires summing over all hypotheses — this is the law of total probability. It's a weighted average of likelihoods, where the weights are the priors. For binary hypotheses, it's just two terms. The denominator acts as a normalizing constant that ensures the posterior sums to 1. Students sometimes find this the trickiest part mechanically, so it's worth working through slowly.

## Slide: MNH Bayes' Rule: Diagnosing Facility Gaps
This is the capstone example of the Bayes' rule section. A neonatal death has occurred — what's the probability the facility lacked CPAP? Prior: 65% of facilities lack CPAP. Step 1: compute P(Death) = 0.03775. Step 2: apply Bayes' rule to get P(No CPAP | Death) = 0.861. The evidence shifted our belief from 65% to 86% — a 21 percentage point jump. Death is strong evidence of equipment absence.

## Slide: MNH Bayes' Rule: Interpreting the Result
The side-by-side comparison — prior 65% vs. posterior 86% — makes the belief shift vivid. The policy implication is practical: mortality audit data can be used to prioritize CPAP distribution. Target facilities where deaths are occurring, because Bayes' rule tells us those are disproportionately the facilities lacking equipment. This connects the abstract math to a real decision an MNH program manager would make.

## Slide: DAG Implies Factorization
The Causal Markov Condition is the theoretical bridge between DAGs and probability. It says: each node is conditionally independent of its non-descendants given its parents. The practical consequence: the full joint distribution factorizes as a product of CPTs. For the chain Staffing → Quality → NMR, this means P(Staffing, Quality, NMR) = P(Staffing) × P(Quality | Staffing) × P(NMR | Quality). Notice NMR depends on Quality *only*, not directly on Staffing. The DAG encodes this.

## Slide: Why Factorization Matters
This is about computational tractability. Without a DAG, 20 binary variables require over a million parameters. With a DAG where each node has at most 3 parents, you need at most 160 parameters. That's a reduction by a factor of 6,500. This is why Bayesian networks are practical for real-world problems — the causal structure tells us which variables are conditionally independent, and that independence dramatically reduces the amount of information we need to specify.

## Slide: Independence from the DAG
This table connects back to d-separation from Chapter 2. Staffing and NMR are not independent (open path through Quality), but they *are* conditionally independent given Quality (the chain is blocked). The DAG encodes this, and the CPTs respect it — the NMR CPT has a Quality column but no Staffing column. Students should see how the qualitative structure from Chapter 2 directly constrains the quantitative model.

## Slide: The Quantified MNH DAG
Now we put it all together: a 4-node Bayesian network with Staffing and Equipment as root nodes, Quality as a collider, and NMR as the outcome. Four nodes, three CPTs. This compact representation encodes the full joint distribution over all 16 possible combinations of states. It's small enough to work through by hand but rich enough to illustrate all the key concepts.

## Slide: Full CPTs for the MNH Model
Here are all the numbers. Root marginals: P(Adequate Staffing) = 0.40, P(Equipment Available) = 0.35. The Quality CPT has four rows ranging from 0.85 (both parents favorable) to 0.20 (both unfavorable). The NMR CPT maps good quality to 0.15 high NMR and poor quality to 0.60 high NMR. These tables are the complete specification of the model — from here, we can answer any probability query.

## Slide: Querying the Model: Best vs. Worst Case
The best case (adequate staffing, available equipment) gives P(NMR=High) = 21.8%. The worst case (low staffing, no equipment) gives 51.0%. That's a 29.2 percentage point spread — the combined quantitative effect of the two inputs. Students should trace through the math to build confidence: multiply the CPTs, weight by the quality distribution, sum up.

## Slide: Sensitivity Analysis: Which Parent Matters More?
This is the kind of analysis that program managers actually need. Fixing staffing alone reduces P(NMR=High) by 17.7 pp. Fixing equipment alone reduces it by 13.5 pp. Fixing both reduces it by 29.3 pp. Staffing has the larger individual effect, but the combined effect is synergistic — not quite additive, because the two inputs interact through the quality CPT. In resource-constrained settings, this analysis tells you where to invest first.

## Slide: Exercise: Compute the Probabilities
Give students time to work through these three problems by hand. Problem 1 (marginal quality) requires summing over all four Staffing × Equipment combinations. Problem 2 (overall NMR) uses the answer to Problem 1 and the NMR CPT. Problem 3 (Bayes' rule) asks them to reverse the direction and compute P(Low Staffing | High NMR). This is the hands-on practice that cements the concepts.

## Slide: R Block 1: Define the Network Structure
Live coding walkthrough. Students define the DAG structure using bnlearn's model string syntax — a compact notation that specifies parents for each node.

## Slide: R Block 2: Specify CPTs
Live coding walkthrough. Students create CPT arrays for all four nodes and combine them into a fitted Bayesian network. The trickiest part is getting the array dimensions right — worth walking through carefully.

## Slide: R Block 3: Query the Network
Live coding walkthrough. Students use cpquery() for approximate inference and gRain for exact inference. Key queries: P(NMR=High | Low Staffing), P(NMR=High | Adequate Staffing + Available Equipment), and the overall marginal P(NMR).

## Slide: R Block 4: Visualize the Network
Live coding walkthrough. Students visualize the network using both bnlearn's built-in plotting and ggdag for publication-quality figures.

## Slide: R Block 5: Interventional Queries
Live coding walkthrough. This is the computational highlight — students use mutilated() to implement the do-operator, comparing P(NMR | do(Staffing=Adequate)) with observational P(NMR | Staffing=Adequate). This previews Chapter 7's distinction between observing and intervening.

## Slide: Key Takeaways
The core message: Bayesian Network = DAG + CPTs. It lets us compute exact probabilities, update beliefs with Bayes' rule, and compare interventions. The Causal Markov Condition makes computation tractable by exploiting conditional independence. Sensitivity analysis reveals which interventions have the largest expected impact. These are the tools that transform causal thinking from a qualitative exercise into a quantitative decision-support system.

## Slide: Looking Ahead
Next chapter we drive the engine. Chapter 4 built the Bayesian network; Chapter 5 uses it for diagnostic inference — updating beliefs with multiple evidence streams, reasoning backward from outcomes to causes, and applying the "explaining away" phenomenon. The MNH application: diagnosing why NMR remains high in a specific district using real-world data patterns.
