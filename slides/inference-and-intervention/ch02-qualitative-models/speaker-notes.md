# Speaker Notes — Chapter 2: Qualitative Causal Models

## Overview
This is the "grammar lesson" of the course — we're learning the formal vocabulary and rules for building causal diagrams. The big payoff is the three triplet structures (chain, fork, collider), which govern all information flow in any causal model, no matter how complex. Once students internalize these three patterns and how conditioning affects each one, they can reason about any DAG. We close by building the full MNH qualitative model and showing how it generates testable predictions.

## Slide: Learning Objectives
Six objectives today, and they build on each other. We start with the building blocks (node types), then learn how to connect them (directed links with signs), handle complexity (conditional certainty tables), master the three fundamental patterns (triplets), learn the formal independence criterion (d-separation), and finally assemble everything into a full MNH DAG. It's a lot, but each piece is individually simple.

## Slide: The Problem with Mental Models
Every manager already has a mental model of how their program works. The problem is that mental models are implicit — they live in your head, they're vague, they're inconsistent, and two people can disagree without even realizing they have different models. Explicit DAGs fix all of this. When you draw it out, your assumptions become visible, debatable, and testable. This is the single biggest practical benefit of the qualitative modeling approach.

## Slide: From Whiteboard Sketch to Formal DAG
This five-step process — identify variables, classify node types, draw arrows, assign signs, validate structure — is the workflow students will use every time they build a causal model. The MNH example of a program director saying "training improves quality, and quality reduces mortality" shows how naturally this works. You take an informal belief and translate it into a precise diagram. The rest of the chapter teaches the rules for each step.

## Slide: Node Type 1: Probabilistic Nodes (Ovals)
Probabilistic nodes are the workhorses of any causal model. They represent uncertain variables — things you don't control and can't predict with certainty. The key rule is MECE states: mutually exclusive and collectively exhaustive. A baby's NMR category is either High or Low — it can't be both, and it must be one. Getting the state definitions right is critical because everything else in the model depends on them.

## Slide: Node Type 2: Objective Nodes (Hexagons)
Objective nodes are what we're trying to affect — lives saved, mortality ratios, cost-effectiveness. They're always leaf nodes, meaning nothing flows out of them. They sit at the end of causal chains and answer the question: "What are we ultimately trying to optimize?" In MNH programs, the primary objective is lives saved, but we often track multiple objectives simultaneously.

## Slide: Node Type 3: Strategic Option Nodes (Rectangles)
These are the levers — the decisions the program controls. Budget allocation, training investment, equipment procurement. They're drawn as rectangles and they're root nodes, meaning no causal arrows point into them (except informational links, which we'll cover shortly). The distinction matters: a probabilistic node is something the world determines; a strategic option node is something *you* choose.

## Slide: Node Type 4: Function Nodes (Chevrons)
Function nodes are the simplest type — if you know all the parent values, you know the child's value with certainty. Total budget is just the sum of its components; coverage rate is facilities equipped divided by total facilities. No uncertainty, just arithmetic. These are rare in qualitative models but become important when we add numbers in Chapter 4. The key distinction from probabilistic nodes is: zero residual uncertainty.

## Slide: Causal Links with Signs
Now we connect the nodes. An arrow from A to B means A directly causes B. The sign tells you the direction: [+] means more A leads to more B, [-] means more A leads to less B, and [0] means no effect. Training [+] → Quality [−] → Mortality reads as: more training leads to better quality, which leads to lower mortality. Simple, but already powerful.

## Slide: Parent, Child, and Directed Paths
This slide introduces the family tree vocabulary of DAGs. Parents are at the tail of arrows, children at the head. A directed path follows arrows from ancestor to descendant. Root nodes have no parents (they're exogenous), leaf nodes have no children (they're terminal). The key insight is the sign multiplication rule: the overall sign of a path is the product of the individual link signs. Budget → Training → Quality → NMR is [+] × [+] × [−] = [−], meaning more budget leads to lower mortality. That's exactly what we'd hope.

## Slide: Sign Multiplication Along Paths
This formalizes the sign rule with a table of examples. The multiplication logic is just like multiplying positive and negative numbers: two negatives make a positive, a positive times a negative is negative. The orange callout is important — when multiple paths between two nodes have different overall signs, qualitative analysis alone can't tell you the net effect. That's one reason we'll need numbers (Chapter 4).

## Slide: Informational Links into Decision Nodes
Informational links are dashed arrows into decision nodes. They don't represent causation — they represent information availability. "The program observes NMR data before deciding how to allocate budget" means there's an informational link from NMR Data into the Budget Allocation decision. This matters for decision analysis in Chapter 7: what you know when you decide determines your optimal strategy.

## Slide: When Relationships Are Not Monotonic
Sometimes a simple [+] or [−] isn't enough. The CPAP example is perfect: CPAP machines reduce mortality *only if* trained staff are available to operate them. If staff aren't trained, the machines sit idle — the effect is [0], not [−]. This is a conditional relationship, and it needs a conditional certainty table instead of a simple sign.

## Slide: Reading Conditional Certainty Tables
The quality-of-care table is richer. When staff are competent and equipment is available, you get a strong positive effect. When staff are inadequate and equipment is unavailable, you actually get a negative effect — active harm risk from unsupervised deliveries. The critical insight for MNH programs is in the orange callout: People and Products are complements, not substitutes. Investing in one without the other doesn't just give you partial results — it can give you *no* results.

## Slide: The Serial Triplet Structure
Now we get to the heart of the chapter. The serial triplet (chain) A → B → C is the simplest causal pathway. Information flows from A to C through B — if you know A, you can update your beliefs about C. But here's the key: if you already know B's exact value, learning about A tells you nothing new about C. Conditioning on the mediator blocks the path. Think of it like a water pipe: close the valve at B, and nothing from A reaches C.

## Slide: MNH Example: Training → Competency → Mortality
The MNH chain is Training → Competency → Mortality. If you don't know a midwife's competency level, knowing she completed training tells you something about her patients' outcomes. But if you already *know* she's competent (maybe you tested her directly), it no longer matters how she got that way — training, experience, whatever. The training information is "screened off" by the competency information. For the program, this means competency is what matters, and training is just one way to get there.

## Slide: Chain Summary
This compact table and the pipeline analogy are worth remembering. Unconditioned: information flows. Conditioned on the middle: blocked. Water flows through the pipe from reservoir to tap; close the valve and it stops. Students should be able to recall this pattern instantly.

## Slide: The Diverging Triplet Structure
The fork A ← B → C represents a common cause. B drives both A and C, creating a spurious correlation between them. The ice cream and drowning example is classic: they're correlated because summer heat drives both, not because ice cream causes drowning. Once you know the temperature, the correlation disappears. This is the formal representation of confounding from Chapter 1.

## Slide: MNH Example: PPH Detection ← Workforce Quality → CPAP Usage
In the MNH context, facilities with high PPH detection rates also tend to use CPAP correctly. Does detecting PPH cause better CPAP use? No — workforce quality drives both. Competent staff are good at detecting PPH *and* good at using CPAP. If you control for workforce quality, the association between PPH detection and CPAP usage disappears. The program implication: investing in PPH detection protocols won't fix CPAP usage — you need to address the common cause, which is workforce quality.

## Slide: Fork Summary
Same compact format as the chain summary. Unconditioned: A and C appear correlated (spurious). Conditioned on B: blocked. The orange callout explicitly connects this back to Chapter 1's confounding trap — the fork is the formal structure that generates confounding.

## Slide: The Converging Triplet Structure
Here's where it gets counterintuitive. The collider A → B ← C behaves *opposite* to chains and forks. Unconditionally, A and C are independent — no information flows. But conditioning on B *opens* the path and creates a spurious association. This is the "explaining away" effect, and it trips up even experienced analysts. The red warning box is important: conditioning on a collider creates an association that didn't exist before.

## Slide: MNH Example: Staffing → Quality ← Equipment
Both staffing and equipment contribute to quality of care. If you don't condition on quality, staffing and equipment are independent — they're separate investment decisions. But among facilities with *good* quality (conditioning on the collider), if you learn that staffing is low, you infer that equipment must be excellent to compensate. The two causes "explain away" each other. This is collider bias, and it's a real danger in program evaluation.

## Slide: Collider Summary and the "Explain Away" Intuition
The exam analogy makes "explaining away" click: if a student passed (collider), learning the exam was easy makes you think less of their talent. The two causes compete to explain the common effect. The critical table at the bottom — showing how the collider is the opposite of chains and forks — is the single most important thing to memorize in this chapter. Chains and forks: open naturally, blocked by conditioning. Colliders: blocked naturally, opened by conditioning.

## Slide: From Triplets to Full Graphs
Real DAGs are more complex than triplets, but the rules are the same. d-Separation extends the triplet logic to full graphs by asking: for *every* path between two variables, is it blocked? A path is blocked if it contains a chain or fork where the middle node is conditioned on, or a collider where the middle node is *not* conditioned on. If all paths are blocked, the variables are d-separated — conditionally independent.

## Slide: Applying d-Separation: An Example
This worked example tests two d-separation queries on the same DAG. Training and NMR given Quality? That's a chain — blocked, so yes, d-separated. Training and Equipment given Quality? Quality is a collider between Training and Equipment — conditioning on it opens the path, so no, not d-separated. Getting students to work through these examples by hand is the best way to build intuition.

## Slide: d-Separation Decision Procedure
The four-step procedure is algorithmic: list all paths, identify triplets on each path, check if any triplet blocks the path, and conclude d-separation only if every path is blocked. The green callout makes the practical point: d-separation tells us which conditional independencies our model *implies*. These are testable predictions. If the data disagrees, our model is wrong.

## Slide: Identifying the Variables
Now we put it all together. The MNH DAG has about 10 key nodes: one decision (Budget), six mediators (Workforce, Training, Equipment, Referral System, Quality, Coverage), one contextual variable (Baseline Burden), and two objectives (NMR, MMR). Each variable has discrete MECE states. This is the variable selection step — arguably the most important and hardest part of building a causal model.

## Slide: The Full DAG Structure
Here's the complete picture. Budget flows through multiple pathways to reach Quality, which then drives both NMR and MMR. Baseline Burden acts as a confounder. The visual layout shows the layered structure: decisions on the left, mediators in the middle, outcomes on the right, confounders above. Take a moment to trace the paths — each one tells a story about how investment translates into outcomes.

## Slide: Assigning Signs to Every Link
This table assigns a sign and rationale to all 13 links in the DAG. Every one should make intuitive sense: more budget enables more hiring [+], trained staff deliver better care [+], better care reduces mortality [−]. Having the rationale written down is important — it makes the model debatable. If someone disagrees with a sign, they can point to exactly which assumption they contest.

## Slide: Identifying Triplets Within the Model
This is where students practice pattern recognition. The DAG contains all three triplet types: chains (Budget → Training → Quality), forks (Workforce ← Budget → Equipment), and colliders (Workforce → Quality ← Equipment). Each has different implications for what you should and shouldn't condition on. The red callout about Quality being a collider is especially important — it means that controlling for quality of care in a regression would create a spurious association between staffing and equipment investment.

## Slide: Testable Implications
The qualitative DAG generates specific conditional independence predictions that we can test against data. Training should be independent of Equipment given Budget (fork). Training should be independent of NMR given Quality (chain). Workforce and Equipment should *not* be independent given Quality (collider). If DHIS2 data violates any of these predictions, we know our model needs revision. This is the scientific payoff of formal modeling — falsifiable predictions.

## Slide: R: Define the Full MNH DAG with dagitty
Live coding walkthrough. Students define the full 10-node MNH DAG in dagitty, specifying all 13 causal links and verifying acyclicity.

## Slide: R: Visualize the DAG Color-Coded by Role
Live coding walkthrough. Students create a color-coded visualization distinguishing decisions (blue), mediators (green), context variables (amber), and outcomes (red).

## Slide: R: Test d-Separation
Live coding walkthrough. Students run five d-separation queries on the MNH DAG, verifying their hand-calculations against dagitty's results. Key tests include the chain (Training-NMR given Quality), fork (Workforce-Equipment given Budget), and collider (Workforce-Equipment given Quality).

## Slide: R: Enumerate All Paths
Live coding walkthrough. Students use dagitty's paths() function to list all directed paths from Budget to NMR and from Budget to MMR, seeing how the investment flows through multiple channels.

## Slide: R: Implied Conditional Independencies
Live coding walkthrough. Students generate the complete list of conditional independencies implied by the DAG — these are the model's testable predictions that can later be validated against DHIS2 data in Chapter 10.

## Slide: Key Takeaways
Three things to take away. First, a DAG encodes your causal beliefs using four node types and signed links. Second, the three triplets — chain, fork, collider — govern all information flow, and the collider is the dangerous exception (opened by conditioning, not blocked). Third, d-separation translates structure into testable predictions. For MNH, the key insight is that People and Products are complements flowing through Quality — and conditioning on Quality creates collider bias.

## Slide: Looking Ahead
Next session we put these tools to work in a structured case study: building a DAG from stakeholder interviews, translating qualitative beliefs into formal diagrams, and preparing the model for quantification in Chapter 4. The interview case will show how iterative model-building works in practice.
