# Speaker Notes — Chapter 4: Quantitative Causal Models

## Overview
Alright, this is the chapter where we shift gears. Up until now, we've been drawing arrows and talking about the direction of effects — which variables cause which. Today we put numbers on those arrows. We're going to transform our qualitative DAGs into Bayesian networks that can compute actual probabilities, and by the end of this session, you'll be able to answer questions like "What is the probability of high neonatal mortality given that a facility has low staffing and no CPAP?" That's a fundamentally different kind of analysis from what we've been doing.

## Slide: Learning Objectives
So here are the five things I want you to walk away with today. We're going to build up in layers. First, we need the language of probability — distributions, axioms, how to talk about uncertainty with numbers. Then we'll move to conditional probability and how to organize it into tables called CPTs. Third, Bayes' rule — the engine that lets us update our beliefs when new evidence comes in. Fourth, a theoretical result called the Causal Markov Condition that makes all of this computationally feasible. And fifth, we'll actually build a working Bayesian network in R and query it. Each piece is necessary for the next, so we're going to take them in order.

## Slide: From Qualitative to Quantitative
Let's set up why we're doing this.

## Slide: Why Structure Alone Is Not Enough
Think back to Chapters 2 and 3. We built DAGs — we figured out which variables influence which, and in what direction. That was valuable. But look at the left column on this slide: qualitative models tell us *which* variables matter and *which direction* the effects go. *(pause)* Now look at the orange box on the right. "How much does staffing affect quality?" "How likely is high NMR given equipment shortages?" "Which intervention has the largest expected impact?" Those are the questions that actually matter for decision-making, and our qualitative models can't answer any of them.

To answer those questions, we need numbers. Specifically, we need probability distributions attached to every node in the DAG. That's what this chapter is about — giving our causal models the ability to compute.

## Slide: The Quantitative Upgrade
Here's the equation, and it's beautifully simple. Take the qualitative DAG we already built — that's Chapters 2 and 3. Add probability tables to every node. What you get is a Bayesian network. *(pause)*

Look at the MNH example. Qualitatively, we know Staffing leads to Quality, which leads to NMR. That's useful but vague. Now, quantitatively — if 40% of facilities have adequate staffing, and 80% of adequately staffed facilities deliver good quality care — suddenly we can *compute* the probability of high NMR. We're not just reasoning about direction anymore. We're calculating exact numbers. And that green box at the bottom is the definition to remember: a Bayesian network equals a DAG plus a conditional probability table for every node.

## Slide: Probability Fundamentals
Okay, before we can build a Bayesian network, we need to get the probability basics right. Let's talk about the language of quantitative uncertainty.

## Slide: Variable States
Before we can assign any probabilities, we need to define what values each variable can take. And there's one critical rule: the states must be MECE — mutually exclusive and collectively exhaustive. That means every facility falls into exactly one category, and the categories cover everything.

Look at the table. Staffing is either Adequate or Low — a facility can't be both, and it has to be one or the other. Same for CPAP, Quality of Care, and NMR. *(pause)* Now, you might be thinking, "NMR is actually a continuous number — why are we chopping it into just High and Low?" Good question. We discretize for tractability. Working with {High, Low} is much more manageable than working with a continuous distribution, and in practice it works well when you care about categories of outcomes rather than exact numbers. This is standard practice in applied Bayesian networks.

## Slide: Events: Sets of States
Now that we have variable states, we can talk about events — the building blocks of probability statements. A simple event is just a variable in a particular state: "Staffing equals Adequate." A compound event combines simple events: "Adequate staffing AND CPAP available."

Look at the right column. The intersection, the union, the complement — these are the logical building blocks. And here's a practically useful one: the complement rule. If P(Staffing = Adequate) is 0.40, then P(Staffing = Low) is just 1 minus 0.40, which is 0.60. No additional information needed. Make sure you're comfortable with these operations before we move forward, because everything in this chapter builds on them.

## Slide: Probability Axioms
Three axioms. That's it — everything in probability theory rests on these three rules. *(pause)* Non-negativity: probabilities can't be negative. Normalization: the probability of *something* happening is 1. Additivity: if two events can't happen simultaneously, the probability of one or the other is the sum.

Most of you have seen these before, but I want to emphasize something. Look at the consequences listed below. The complement rule, the fact that probabilities live between 0 and 1, the requirement that state probabilities sum to 1. These aren't just mathematical niceties. When you're building a model and eliciting probabilities from experts — which we'll do in practice — it's surprisingly easy to accidentally violate these axioms. And if you do, your model will produce contradictions. So these axioms are your sanity checks.

## Slide: Frequency vs. Subjective Probability
This distinction is going to matter a lot for the kind of work we do. *(pause)*

On the left, the frequentist interpretation. "40% of facilities have adequate staffing" — that comes from data, maybe a facility survey. You visit a bunch of facilities, count the ones with adequate staffing, divide by the total. On the right, the subjective or Bayesian interpretation. "I believe there's a 70% chance this district will reduce NMR by 2030." That's an expert judgment — it doesn't come from repeating an experiment; it comes from experience and reasoning.

Now here's the practical point. In our work, we use both. CPTs combine survey data where it's available with expert judgment where data is sparse. And in data-limited settings — which is where most of the MNH programs we're studying operate — subjective priors aren't a weakness. They're a necessary and valuable input. Dismissing expert judgment because it's "subjective" means you have no model at all.

## Slide: MNH Example: Marginal vs. Conditional Probability
Let me show you why this distinction matters with real numbers. The marginal probability of neonatal death is about 25 per 1,000 live births. That's across all births. But the conditional probability — given that the birth was preterm — jumps to about 100 per 1,000. That's four times higher. *(pause)*

So preterm birth is clearly a strong risk factor. But here's the causal thinking question we should be trained to ask by now: is preterm birth a *cause* of neonatal death, or is it a *marker* for other causes like maternal health, facility quality, and access to care? Conditional probability alone can't tell us. For that, we need a causal model that separates the direct effect from the confounders. This is exactly the kind of reasoning that keeps coming back throughout this course.

## Slide: Conditional Probability
Now let's formalize conditional probability. This is the foundation of Bayesian networks.

## Slide: Definition and Interpretation
Here's the formula: P(A given B) equals P(A and B) divided by P(B). *(pause)* The intuition is straightforward: "Among all the cases where B is true, what fraction also have A?" So P(NMR equals High given Staffing equals Low) means: among facilities with low staffing, what fraction have high neonatal mortality?

Now, I want you to look at the bottom of this slide very carefully. P(NMR = High given Staffing = Low) is 0.55. P(Staffing = Low given NMR = High) is 0.75. Those look similar, but they are very different numbers answering very different questions. The first asks: "Of under-staffed facilities, how many have high mortality?" The second asks: "Of high-mortality facilities, how many are under-staffed?" Confusing these two is one of the most common and costly errors in applied analysis. Do not confuse them.

## Slide: Stochastic Independence
Independence means knowing one variable tells you absolutely nothing about the other. We test it by checking whether P(A given B) equals P(A) — in other words, does learning B change your belief about A?

Look at the MNH test. P(NMR = High) overall is 0.35. But conditional on adequate staffing, it drops to 0.15. And conditional on low staffing, it jumps to 0.55. Since 0.15 is not equal to 0.35, and 0.55 is not equal to 0.35, staffing and NMR are clearly not independent. Staffing is informative about mortality. *(pause)* And that's exactly what our causal model from Chapter 2 predicts — there's an open path between staffing and NMR through quality of care. The math confirms what the diagram told us.

## Slide: Conditional Probability Tables (CPTs)
Okay, now we get to the heart of a Bayesian network. A CPT — Conditional Probability Table — lists the probability of a child node given every combination of its parent states. Every row sums to 1 because each row is a conditional distribution.

Look at this Quality of Care CPT. Four rows — one for each combination of Staffing and CPAP. When staffing is adequate and CPAP is available, there's an 85% chance of good quality. When staffing is adequate but CPAP is unavailable, it drops to 55%. When staffing is low but CPAP is available, it's 50-50. And when both are absent — low staffing, no CPAP — there's only a 20% chance of good quality. *(pause)* That's the quantitative version of what we already knew qualitatively. Now we can see *how much* each input matters.

## Slide: MNH CPT: Neonatal Outcome Given CPAP and Training
Here's another CPT, this time for neonatal outcome given equipment and training status. And the headline number is striking: survival ranges from 96% when both CPAP and training are in place, all the way down to 70% when neither is present. That's a 26 percentage point gap. *(pause)*

Think about what that means in concrete terms. For every thousand births, that's the difference between 40 deaths and 300 deaths. That's the quantitative payoff of investing in both people and products together.

The orange note at the bottom is worth mentioning — these numbers are illustrative but grounded in the literature. In a real application, you'd populate these tables from facility-level data, expert elicitation, or some combination of both.

## Slide: Joint Probabilities
Now let's talk about how variables co-occur. This is where we start computing with these probability tables.

## Slide: The Factoring Rule
The chain rule says P(X and Y) equals P(X given Y) times P(Y). Simple multiplication. Let me walk you through the example. *(pause)*

What's the probability that a facility has both low staffing AND poor quality? P(Poor Quality given Low Staffing) is 0.65, and P(Low Staffing) is 0.60. Multiply them: 0.65 times 0.60 equals 0.39. So about 39% of facilities have both problems simultaneously. *(pause)*

This is the basic building block of Bayesian network computation: start with what you know — the marginals and the CPTs — and multiply. Software automates this for bigger models, but you need to understand the mechanics to interpret the results correctly and to debug when something looks wrong.

## Slide: Joint Probability Tables
A joint probability table shows every combination of two variables. Let me walk you through how to read this one.

The cell values are joint probabilities — P(Quality = Good AND Staffing = Adequate) is 0.28. The row totals are marginal probabilities of Quality — P(Good) is 0.49. The column totals are marginal probabilities of Staffing — P(Adequate) is 0.40. And the grand total is always 1.00.

Now, look at the numbers and notice what they tell us. 28% of facilities are both well-staffed and good quality. 39% are both poorly staffed and poor quality. And the row marginals show that 51% of facilities — more than half — have poor quality care overall. That's a pretty grim baseline, and it tells you exactly how much room there is for improvement.

## Slide: Computing Joint Distributions from CPTs
Here's the three-step procedure for computing any joint distribution from a Bayesian network. Step one: start with the marginals. Step two: apply the CPTs. Step three: multiply. *(pause)*

Let me trace through this. P(Staffing = Adequate AND Quality = Good) equals P(Quality = Good given Staffing = Adequate) times P(Staffing = Adequate). That's 0.70 times 0.40, which gives us 0.28. And that matches what we saw in the joint table on the previous slide.

This forward computation — multiplying marginals by CPTs — is exactly what the software does under the hood when you query a Bayesian network. Understanding the mechanics makes debugging much easier when results don't look right.

## Slide: MNH Example: Three-Variable Joint Distribution
Now let's see this in action across three variables: Training, Competency, and Outcome. This is a full worked example.

We're given that 45% of staff have completed training. Then we have CPTs for Competency given Training, and Outcome given Competency. The table shows all four paths through the network with their joint probabilities worked out.

Look at the bottom line: overall P(Survival) is 87.4%. Now here's the policy question. What if training coverage increased from 45% to 80%? P(Survival) rises to 91.4%. That might not sound like a huge jump, but do the math — that's an additional 40 lives saved per 1,000 births. *(pause)* This is the kind of quantitative policy analysis that becomes possible once you have a Bayesian network. You can ask "what if" questions and get specific numerical answers.

## Slide: Bayes' Rule
Now here's where it gets really interesting. Bayes' rule lets us reason backwards — from evidence to cause.

## Slide: Derivation from Conditional Probability
Bayes' rule follows directly from the definition of conditional probability. We can write the joint probability P(A and B) in two different ways — as P(A given B) times P(B), or as P(B given A) times P(A). Since they're both equal to the same joint probability, we can set them equal and rearrange.

The result is: P(A given B) equals P(B given A) times P(A) divided by P(B). *(pause)*

The formula itself is simple. What makes it powerful is what it *does*. It lets you flip the direction of conditioning. If you know P(Evidence given Cause) — which is often easy to estimate — Bayes' rule gives you P(Cause given Evidence) — which is what you actually want to know. This is the fundamental operation of situational assessment. You observe what happened, and you reason backwards to figure out what's likely true.

## Slide: The Terminology of Bayes' Rule
Four terms to internalize. The prior — what you believed before seeing any evidence. The likelihood — how probable the evidence is if your hypothesis is true. The posterior — your updated belief after incorporating the evidence. And the marginal likelihood — a normalizing constant that ensures everything sums to 1.

The key insight is right there on the slide: posterior is proportional to likelihood times prior. *(pause)* What does that mean in practice? If the evidence strongly favors your hypothesis — high likelihood — the posterior shifts far from the prior. If the evidence is weak or ambiguous, the posterior stays close to the prior. This is how rational belief updating works, and it's the mathematical backbone of everything we do in Chapters 5 through 10.

## Slide: Computing P(B): The Law of Total Probability
The denominator of Bayes' rule — P(B) — requires us to sum over all possible hypotheses. This is the law of total probability. It's essentially a weighted average of the likelihoods, where the weights are the priors.

For a binary hypothesis, it's just two terms. P(B) equals P(B given A = Yes) times P(A = Yes) plus P(B given A = No) times P(A = No).

The denominator acts as a normalizing constant that ensures the posterior probabilities sum to 1 across all hypotheses. Students sometimes find this the trickiest part mechanically, so let's work through a concrete example. That's exactly what the next slide does.

## Slide: MNH Bayes' Rule: Diagnosing Facility Gaps
Alright, here's where we put Bayes' rule to work on a real MNH question. A neonatal death has occurred. What's the probability the facility lacked CPAP?

Here's what we know. The prior: 65% of facilities lack CPAP. The likelihood of death given no CPAP is 5%. The likelihood of death given CPAP is available is 1.5%. *(pause)*

Step 1: compute P(Death) using the law of total probability. That's 0.05 times 0.65 plus 0.015 times 0.35, which equals 0.03775. Step 2: apply Bayes' rule. P(No CPAP given Death) equals 0.05 times 0.65 divided by 0.03775, which gives us 0.861.

So the evidence — a neonatal death — shifted our belief from 65% to 86%. That's a 21 percentage point jump. Death is strong evidence of equipment absence.

## Slide: MNH Bayes' Rule: Interpreting the Result
Look at the side-by-side comparison on this slide. On the left, the prior: 65% chance the facility lacked CPAP. On the right, the posterior: 86%. The evidence shifted our belief by 21 percentage points.

Now, what does this mean for someone managing an MNH program? *(pause)* It means mortality audit data can be used to prioritize CPAP distribution. If a facility reports neonatal deaths, Bayes' rule tells us that facility is disproportionately likely to be lacking equipment. Target those facilities first. This connects the abstract math we just did to a real decision that an MNH program manager would actually make. Bayes' rule isn't just elegant — it's practical.

## Slide: Factorization & the Causal Markov Condition
Okay, let's talk about what makes Bayesian networks actually work at scale. How do DAGs simplify probability?

## Slide: DAG Implies Factorization
The Causal Markov Condition is the theoretical bridge between DAGs and probability. Here's what it says: each variable in a DAG is conditionally independent of its non-descendants, given its parents. *(pause)*

That sounds abstract, so let me show you what it means concretely. Look at the illustration. For the chain Staffing leads to Quality leads to NMR, the full joint distribution factorizes as: P(Staffing) times P(Quality given Staffing) times P(NMR given Quality). Notice something important — NMR depends on Quality *only*, not directly on Staffing. Even though staffing affects NMR, it does so entirely through quality. The DAG encodes that, and the factorization respects it. We only need to specify P(NMR given Quality), not P(NMR given Quality and Staffing).

## Slide: Why Factorization Matters
This slide is about why you should care about that mathematical property. It's about computational tractability. *(pause)*

Without a DAG, if you have 20 binary variables, you need to specify over a million parameters — 2 to the power of 20 is about 1,048,576. That's completely impractical. But with a DAG where each node has at most 3 parents, you need at most 160 parameters. That's a reduction by a factor of 6,500.

This is why Bayesian networks are practical for real-world problems. The causal structure tells us which variables are conditionally independent, and those independencies dramatically reduce the amount of information we need to specify. Without the DAG, the problem is intractable. With it, it's manageable.

## Slide: Independence from the DAG
Let me connect this back to d-separation from Chapter 2. Look at the chain: Staffing leads to Quality leads to NMR.

Are Staffing and NMR independent? No — there's an open path through Quality. But are they conditionally independent *given* Quality? Yes — conditioning on Quality blocks the chain. Once you know the quality of care at a facility, learning about its staffing level tells you nothing additional about its NMR.

And look at how this shows up in the CPTs. The NMR CPT has a Quality column but no Staffing column. The qualitative structure from Chapter 2 directly constrains the quantitative model in Chapter 4. The DAG tells us what we need to put in the CPTs — and equally importantly, what we can leave out.

## Slide: MNH Application: Quantifying the Model
Now let's put the whole thing together with a concrete MNH model. Time to add numbers.

## Slide: The Quantified MNH DAG
Here's our Bayesian network: four nodes. Staffing and Equipment are root nodes — they sit at the top with just marginal probabilities. Quality of Care sits in the middle as a child of both Staffing and Equipment. And NMR is the outcome, depending only on Quality.

Four nodes, three CPTs. That's a compact little model, but it encodes the full joint distribution over all 16 possible combinations of variable states. It's small enough that we can work through the math by hand, but rich enough to illustrate every concept we've covered today.

## Slide: Full CPTs for the MNH Model
Here are all the numbers. The root marginals: P(Adequate Staffing) is 0.40, P(Equipment Available) is 0.35. *(pause)*

The Quality CPT has four rows. When both parents are favorable — adequate staffing and available equipment — there's an 85% chance of good quality. When both are unfavorable, it drops to 20%. And the NMR CPT is simple: good quality maps to a 15% chance of high NMR, poor quality maps to 60%.

These tables right here — this is the complete specification of the model. From these numbers alone, we can answer any probability query about these four variables. Let me show you.

## Slide: Querying the Model: Best vs. Worst Case
Let's compute the extremes. Best case: adequate staffing and available equipment. That gives 85% chance of good quality, and when we work through the NMR probabilities, we get P(NMR = High) of 21.8%. *(pause)*

Worst case: low staffing, no equipment. Now there's only a 20% chance of good quality, and P(NMR = High) jumps to 51%.

That's a 29.2 percentage point spread between the best and worst cases. I'd encourage you to trace through the math yourself — multiply the CPTs, weight by the quality distribution, sum up. It's the same three-step process we covered earlier, and working through it by hand builds real confidence in what the model is doing.

## Slide: Sensitivity Analysis: Which Parent Matters More?
Now here's the analysis that program managers actually need. If you had to choose — do you fix staffing first, or equipment first? *(pause)*

Look at the table. Fixing staffing alone — going from low to adequate while keeping equipment unavailable — reduces P(NMR = High) by 17.7 percentage points. Fixing equipment alone reduces it by 13.5 percentage points. And fixing both reduces it by 29.3 percentage points.

So staffing has the larger individual effect. But notice something in the comparison at the bottom. The effects are synergistic — fixing both gives you 29.3 points of reduction, which is not quite the sum of the individual effects. That's because staffing and equipment interact through the quality CPT. In a resource-constrained setting, this analysis tells you where to invest first: workforce. And it tells you that investing in both is more than the sum of the parts.

## Slide: Exercise: Compute the Probabilities
Alright, your turn. I want you to work through three problems by hand using the CPTs from the previous slides. *(pause)*

Problem 1: compute P(Quality = Good) — the marginal probability of good quality across all facilities. You'll need to sum over all four combinations of Staffing and Equipment. Problem 2: compute P(NMR = High) — the overall probability of high NMR. Use your answer from Problem 1 and the NMR CPT. Problem 3: apply Bayes' rule to compute P(Staffing = Low given NMR = High). This one asks you to reverse the direction — given that a facility has high NMR, what's the probability it has low staffing?

Take a few minutes. The hints are on the slide if you get stuck. We'll check the answers when we get to the R workshop.

## Slide: R Code Workshop
Okay, let's move to R and build this thing for real.

## Slide: R Block 1: Define the Network Structure
This is our first piece of code. We're using bnlearn's model string syntax to define the DAG structure. The notation is compact — square brackets for each node, and a vertical bar plus colon for conditioning. So `[Quality|Staffing:Equipment]` means Quality depends on both Staffing and Equipment.

Once you run this, you can inspect the structure with `nodes()` and `arcs()` to confirm it matches our four-node diagram. This is just the skeleton — no numbers yet.

## Slide: R Block 2: Specify CPTs
Now we add the numbers. We're creating CPT arrays for all four nodes and combining them into a fitted Bayesian network using `custom.fit()`. *(pause)*

The trickiest part here is getting the array dimensions right — the ordering of dimensions in R's array function matters. Walk through this carefully and make sure your CPT arrays match the tables we worked with on the slides. Once you've got all four CPTs, `custom.fit()` combines them with the DAG structure into a complete Bayesian network object.

## Slide: R Block 3: Query the Network
Now the fun part — asking questions. We use `cpquery()` for approximate inference via simulation, and `gRain` for exact inference using junction trees.

The key queries: P(NMR = High given Low Staffing) — we expect about 0.44. P(NMR = High given Adequate Staffing and Available Equipment) — we expect about 0.22, which matches our best-case calculation. And `querygrain()` gives us the overall marginal P(NMR) across all facilities. *(pause)* That last one is the answer to Exercise Problem 2 — about 39% of facilities have high NMR under current conditions.

## Slide: R Block 4: Visualize the Network
Here we visualize the network two different ways. First, bnlearn's built-in plot using Rgraphviz — quick and functional. Second, ggdag for publication-quality figures where you can control positioning, coloring, and styling. Both approaches give you the same structure; it's just a matter of how polished you need the output.

## Slide: R Block 5: Interventional Queries
This is the computational highlight of the chapter. The `mutilated()` function implements the do-operator. Remember from Chapter 2 — the do-operator severs incoming arrows to a variable and sets it to a fixed value. That gives us the *causal* effect rather than a mere observational correlation.

So we can compare P(NMR given do(Staffing = Adequate)) — what happens if we *intervene* to make staffing adequate — with P(NMR given Staffing = Adequate) — what we observe at facilities that happen to have adequate staffing. *(pause)* In this particular model, because there are no confounders between Staffing and NMR, the two numbers happen to be close. But the distinction is foundational, and it becomes critical in more complex models. This previews what we'll dig into in Chapter 7.

## Slide: Key Takeaways
Let me pull it all together. The core equation for today: Bayesian Network equals DAG plus CPTs. With that, you can compute exact probabilities for any combination of variables. Bayes' rule lets you update beliefs — reasoning backward from evidence to causes. The Causal Markov Condition makes computation tractable by exploiting conditional independence. And sensitivity analysis reveals which interventions have the largest expected impact.

These are the tools that transform causal thinking from a qualitative exercise — drawing arrows and reasoning about direction — into a quantitative decision-support system that produces actionable numbers.

## Slide: Looking Ahead
Next chapter, we drive the engine we just built. We constructed a Bayesian network today; in Chapter 5, we use it for diagnostic inference. That means updating beliefs with multiple evidence streams simultaneously, reasoning backward from outcomes to causes, and working with a phenomenon called "explaining away" — where one piece of evidence changes the relevance of another. The MNH application will be analyzing why NMR remains high in a specific country using real-world data patterns. We built the engine; now we learn to drive it.
