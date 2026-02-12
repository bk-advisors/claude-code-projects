# Speaker Notes — Chapter 2: Qualitative Causal Models

## Overview
Today is our grammar lesson. We're going to learn the formal vocabulary and the rules for building causal diagrams. The big payoff is three simple patterns — chain, fork, and collider — that govern how information flows through *any* causal model, no matter how complex. Once you internalize those three patterns, you can reason about any DAG. And we'll close by building the full MNH qualitative model together.

## Slide: Learning Objectives
Alright, six objectives for today, and they build on each other like a staircase. We start with the building blocks — the four types of nodes. Then we learn how to connect them with directed links and signs. Then we handle the tricky cases where a simple plus or minus isn't enough — that's where conditional certainty tables come in. Then we get to the heart of it: the three fundamental triplet patterns. From there, we learn the formal independence criterion called d-separation. And finally, we put it all together and build a complete MNH DAG. *(pause)* It's a lot of material, I know. But each individual piece is simple. The power comes from combining them.

## Slide: From Intuition to Structure
Why writing down causal beliefs matters — let's talk about that.

## Slide: The Problem with Mental Models
Here's something I want you to think about. Every one of you already has a mental model of how your program works, right? You have beliefs about what causes what. The problem is that those mental models are *implicit*. They live in your head. They're vague. They're often inconsistent. *(pause)* And here's the really tricky part — two people can have completely different models and disagree about a decision without ever realizing *why* they disagree, because neither person has actually written down their assumptions.

Now look at the two columns on this slide. On the left, implicit models — vague, resistant to scrutiny, hidden assumptions, unproductive disagreements. On the right, explicit models using DAGs — precise, shareable, open to critique, and disagreements become *productive*. *(pause)* That's the single biggest practical benefit of what we're learning today. When you draw your beliefs out as a diagram, your assumptions become visible, debatable, and testable.

And that core principle at the bottom — read it with me — a qualitative causal model is a disciplined way of writing down what you believe about how variables relate to one another, *before* you add any numbers. That's all it is. Let's learn how to do it.

## Slide: From Whiteboard Sketch to Formal DAG
So here's the workflow you'll use every single time you build a causal model. Five steps. Identify your variables, classify the node types, draw the arrows, assign signs, and validate the structure.

Let me give you the MNH example to make it concrete. Imagine a program director says, "I think training midwives improves quality of care, and better quality reduces mortality." *(pause)* That one sentence becomes a chain: Training, arrow with a plus sign to Quality, arrow with a minus sign to Mortality. You take an informal belief and translate it into a precise diagram. Simple as that.

The rest of this chapter teaches you the formal rules for each of those five steps.

## Slide: Nodes
The four building blocks of causal diagrams — let's go through them one at a time.

## Slide: Node Type 1: Probabilistic Nodes (Ovals)
Probabilistic nodes are the workhorses of any causal model. These are your uncertain variables — things you don't control and can't predict with certainty. You draw them as ovals.

Look at the MNH examples. Neonatal mortality rate — is it high or low? You don't know for sure. Baseline disease burden — severe, moderate, or low? Again, uncertain. Workforce quality — competent, developing, or inadequate? Same thing.

Now here's the critical rule, and I want you to remember this. Each probabilistic node must have MECE states — mutually exclusive and collectively exhaustive. *(pause)* What does that mean? A baby's NMR category is either high or low. It can't be both at the same time, and it must be one or the other. Getting these state definitions right is absolutely critical, because everything else in the model depends on them. If your states aren't MECE, your whole model breaks down.

## Slide: Node Type 2: Objective Nodes (Hexagons)
Objective nodes are what we're ultimately trying to affect. Lives saved, maternal mortality ratio, cost-effectiveness. You draw them as hexagons, and they have a special property — they're always leaf nodes. That means nothing flows *out* of them. No arrows leave an objective node.

Think of it this way: they sit at the very end of your causal chains and they answer one question — what are we ultimately trying to optimize? *(pause)* In the MNH context, the primary objective is lives saved, but we often track multiple objectives simultaneously — NMR, MMR, cost-effectiveness. They're all sitting there at the right-hand side of your diagram, collecting the effects of everything upstream.

## Slide: Node Type 3: Strategic Option Nodes (Rectangles)
Now these are the levers — the things the program actually controls. Budget allocation, training investment, equipment procurement. You draw them as rectangles, and they're the mirror image of objective nodes. Where objectives are leaf nodes with no arrows going out, strategic options are root nodes with no *causal* arrows coming in.

*(pause)* The distinction here is important. A probabilistic node is something the world determines — you observe it. A strategic option node is something *you* choose. Budget allocation? That's your decision. Whether to fund training? Your call. What equipment to procure? Again, you. These are the handles you can grab. I should mention there's one exception — informational links, which are dashed arrows, can point into decision nodes. We'll cover those shortly.

## Slide: Node Type 4: Function Nodes (Chevrons)
Function nodes are the simplest type, and that's why they sometimes get overlooked. If you know all the parent values, you know the child's value with certainty. No uncertainty at all.

Total budget spent is just the sum of workforce spending plus equipment spending plus systems spending — that's arithmetic, not probability. Coverage rate is facilities equipped divided by total facilities — again, just a formula. *(pause)* Look at the comparison on this slide. A probabilistic node takes parent states and gives you a probability distribution — uncertainty remains. A function node takes parent states and gives you exactly one answer. Zero residual uncertainty.

These are rare in qualitative models, but they become important when we add numbers in Chapter 4, where they represent accounting identities and formulas.

## Slide: Directed Links
Okay, we've got our four node types. Now let's learn how to connect them.

## Slide: Causal Links with Signs
An arrow from A to B means A directly causes B. That's straightforward. But we add one more piece of information — the sign. *(pause)*

Look at the table. Plus means more A leads to more B. Minus means more A leads to *less* B. And zero means no effect for that particular combination — we'll see that in conditional certainty tables soon.

Now look at the diagram at the bottom. Training Investment, plus arrow, to Workforce Quality, minus arrow, to Neonatal Mortality. Read it out loud with me: more training leads to better quality, and better quality leads to lower mortality. *(pause)* Simple, right? But already powerful. With just two arrows and two signs, we've captured a meaningful causal story about how the MNH program works.

## Slide: Parent, Child, and Directed Paths
Now we need the family tree vocabulary of DAGs. Parents are at the tail of arrows, children are at the head. A directed path follows arrows from ancestor to descendant — always going in the direction the arrows point.

Look at the diagram. Budget is a root node — no parents, it's exogenous. NMR is a leaf node — no children, it's the terminal outcome. Training is a child of Budget, Quality is a grandchild.

*(pause)* Now here's a key insight — the sign multiplication rule. The overall sign of a path is the product of the individual link signs along that path. Follow me through this: Budget to Training is plus, Training to Quality is plus, Quality to NMR is minus. So the overall sign is plus times plus times minus, which equals... *(pause)* minus. More budget leads to lower mortality. That's exactly what we'd hope, right? The math of the signs confirms the intuition of the investment.

## Slide: Sign Multiplication Along Paths
This slide formalizes that sign rule with a table of examples. The multiplication logic works just like multiplying positive and negative numbers from algebra class. Plus times plus is plus. Minus times minus is also plus. Plus times minus is minus.

Walk through each row of the table. Budget through Training through Quality to NMR — plus, plus, minus — overall minus. More budget reduces NMR. Budget through Equipment through Quality to NMR — same signs, same conclusion. Disease Burden through Coverage to NMR — minus times minus equals plus. Higher burden, higher NMR. Makes sense.

*(pause)* Now, pay attention to that orange callout. When multiple paths connect two nodes and they have *different* overall signs, qualitative analysis alone can't tell you the net effect. Is it positive or negative on balance? You can't say. That's one of the big reasons we'll need actual numbers when we get to Chapter 4.

## Slide: Informational Links into Decision Nodes
This one's different from everything we've seen so far. Informational links are dashed arrows pointing into decision nodes. They don't represent causation — they represent information availability.

Look at the diagram. That dashed arrow from Baseline NMR Data into Budget Allocation? It means the program observes NMR data *before* deciding how to allocate the budget. *(pause)* This is *not* the same as saying NMR causes the budget. It's saying the decision-maker has access to that information when making their choice.

Why does this matter? Because in Chapter 7, when we get to decision analysis, what you know at the time of your decision determines your optimal strategy. If you can see the NMR data before you allocate funds, you can target your investment. If you can't, you're flying blind. The information structure of the problem matters enormously.

## Slide: Conditional Certainty Tables
When plus and minus are not enough — let's tackle that.

## Slide: When Relationships Are Not Monotonic
So far, a simple plus or minus sign has been enough to describe every relationship. More of A always means more of B, or always means less of B. That's a monotonic relationship. *(pause)* But sometimes the real world is more complicated than that.

The CPAP example is perfect. Do CPAP machines reduce mortality? Well... it depends. If trained staff are available to operate them, yes — you get a minus sign, mortality goes down. But if staff aren't trained? The machines just sit idle. The effect is zero, not minus. *(pause)* This is a conditional relationship. The effect of one input depends on the state of another input. And when you have that, a simple plus or minus won't capture it. You need a conditional certainty table.

Look at the table on this slide. Each cell tells you the qualitative sign for that particular combination of parent states. CPAP available *and* staff trained? Minus — reduces NMR. CPAP available but staff *not* trained? Zero — no effect, machines gathering dust. CPAP unavailable, staff trained? Zero — skill without tools. Both unavailable? Zero — no intervention at all.

## Slide: Reading Conditional Certainty Tables
Now let's look at a richer example — the effect on quality of care when we cross staff competency with equipment availability.

This table tells a more nuanced story. Staff competent and equipment available? Strong positive effect — you've got the full package. Staff competent but equipment unavailable? Still positive, but moderate — skill compensates for missing tools to some degree. Staff developing with equipment available? Also moderate — the equipment helps bridge the competency gap. *(pause)*

But look at the bottom-right corner. Staff inadequate and equipment unavailable? That's not just zero — that's a *minus*. Active harm risk from unsupervised deliveries. That should give you pause.

And here's the key insight in that orange callout — this is really important for MNH programs. People and Products are complements, not substitutes. Investing in one without the other doesn't just give you partial results — in the worst case, it can give you *no* results, or even negative ones. You need both. Keep that in mind.

## Slide: Serial Triplets (Chain)
Alright, now we get to the heart of the chapter. These next three sections — chain, fork, collider — are the most important material we'll cover today.

## Slide: The Serial Triplet Structure
The serial triplet, or chain, is the simplest causal pathway. A causes B, B causes C. A arrow to B, B arrow to C.

Here's how information flows. If you don't know B's value, then learning about A tells you something about C. Information flows right along the chain from A through B to C. *(pause)* But — and this is the key — if you already know B's exact value, then learning about A tells you nothing *new* about C. Conditioning on the mediator blocks the path.

Think of it like a water pipe. Water flows from the reservoir through the pipe to the tap. But if you close the valve in the middle? Nothing from the reservoir reaches the tap. That's exactly what conditioning on B does — it closes the valve.

## Slide: MNH Example: Training → Competency → Mortality
Let's make this concrete with the MNH chain. Training leads to competency, competency leads to mortality.

Look at the two columns. On the left, the green box — we're *not* conditioning on competency. In that case, training and mortality are associated. If I tell you a midwife completed her training, you can reasonably predict her patients will have better outcomes. Information flows through the chain.

*(pause)* Now look at the right column, the orange box. We *are* conditioning on competency. If I already *know* a midwife is competent — maybe I tested her directly — then it no longer matters *how* she became competent. Training, years of experience, natural talent, whatever. The training information is "screened off" by the competency information. The path is blocked.

So what does this mean for the program? It tells us that training's value is entirely mediated through competency. Competency is what actually matters. Training is just one way to get there. If you can measure competency directly, you don't need training records to predict outcomes.

## Slide: Chain Summary
Here's the compact version. Not conditioning on B? A and C are associated — information flows. Conditioning on B? Blocked — the path is shut.

And I love this pipeline analogy. Water flows from the reservoir through the pipe to the tap. Close the valve at B, and nothing from A reaches C. *(pause)* Make sure you can recall this pattern instantly. We'll need it for d-separation.

## Slide: Diverging Triplets (Fork)
Now the second pattern — the common cause structure.

## Slide: The Diverging Triplet Structure
The fork looks like this: A gets an arrow *from* B, and C gets an arrow *from* B. B is in the middle, causing both A and C. Notice the arrows point *away* from B in both directions.

Here's what happens. Because B drives both A and C, A and C end up correlated — even though neither one causes the other. This is a spurious correlation. *(pause)* The classic example? Ice cream sales and drowning deaths. They're correlated. Does ice cream cause drowning? Of course not. Summer heat drives both — more ice cream *and* more swimming. Heat is the common cause, the B in our fork. Once you know the temperature, the correlation between ice cream and drowning disappears.

And notice — the information flow rules are the same as the chain! Unconditionally, information flows between A and C. Condition on B, the common cause, and the flow is blocked. Same pattern, different causal structure.

## Slide: MNH Example: PPH Detection ← Workforce Quality → CPAP Usage
Let's see this in the MNH context. Workforce quality is the common cause. It drives both PPH detection rates and correct CPAP usage.

Look at the left column, the red box. Here's what a naive observer sees: facilities with high PPH detection rates also have high CPAP usage. So they ask, "Does detecting PPH somehow *cause* better CPAP use? Should we invest in PPH detection protocols to improve CPAP outcomes?" *(pause)*

Now look at the right column, the green box. That's the causal reality. Both metrics are driven by workforce quality. Competent staff are good at detecting PPH *and* good at using CPAP correctly. It's not that one causes the other — they share a common driver.

The program implication is in that callout at the bottom. If you see a correlation between two metrics, you have to ask — is there a common driver? Investing in PPH detection protocols won't improve CPAP usage unless you address the underlying cause, which is workforce quality.

## Slide: Fork Summary
Same compact format. Not conditioning on B? A and C appear correlated — spurious correlation from the common cause. Conditioning on B? Blocked — the confounding disappears.

*(pause)* And notice that orange callout — this is exactly the confounding trap from Chapter 1. Remember the health worker deployment example? The fork structure is the formal representation of confounding. And the solution is always the same: condition on the common cause.

## Slide: Converging Triplets (Collider)
Okay, here's where it gets interesting. And honestly, a little counterintuitive. The dangerous exception.

## Slide: The Converging Triplet Structure
The collider looks like this: A causes B, and C *also* causes B. Two arrows "collide" at B. That's why it's called a collider.

Now here's where you need to pay very close attention, because this structure behaves *opposite* to everything we just learned. *(pause)*

With chains and forks, information flows naturally, and conditioning blocks it. With colliders, it's reversed. Unconditionally, A and C are independent. No information flows at all — the path is naturally blocked at the collider. *(pause)* But — and this is the dangerous part — if you condition on B, you *open* the path. A and C become associated. You've created a spurious correlation that didn't exist before.

Read that red warning box with me. Conditioning on a collider *creates* a spurious association that did not exist before. This is the opposite of what happens with chains and forks. This is what we call collider bias, and it trips up even experienced analysts.

## Slide: MNH Example: Staffing → Quality of Care ← Equipment
Both staffing levels and equipment availability contribute to quality of care. Quality is the collider — two arrows point into it.

Now, if you don't condition on quality — look at the left, green box — staffing and equipment are independent. They're separate investment decisions. Knowing one tells you nothing about the other. Fine.

*(pause)* But among facilities with *good* quality of care — meaning you're now conditioning on the collider — something weird happens. If you learn that staffing is low at a good-quality facility, what do you infer? *(pause)* That the equipment must be excellent. Something has to explain the good quality, and if it isn't people, it must be products. The two causes "explain away" each other. That's collider bias, and it creates a spurious *negative* association between staffing and equipment that doesn't actually exist in the population.

## Slide: Collider Summary and the "Explain Away" Intuition
Let me give you an analogy that makes this click. Imagine you know a student passed an exam. That's the collider. Now I tell you the exam was easy. What happens to your belief about the student's talent? *(pause)* It goes *down*. Because if the exam was easy, you don't need much talent to pass. The two causes — talent and exam difficulty — compete to explain the common effect. That's "explaining away."

Now look at that critical table at the bottom of the slide. This is the single most important thing to memorize in this chapter. *(pause)*

Chains and forks: associated unconditionally, blocked by conditioning. Colliders: blocked unconditionally, *opened* by conditioning. The collider is the odd one out. Everything else follows the same pattern — the collider is the exception that flips the rule. Burn this table into your memory.

## Slide: c-Independence and d-Separation
Alright, now we formalize what we just learned into a general criterion we can apply to any graph, no matter how complex.

## Slide: From Triplets to Full Graphs
In simple triplets, the rules are straightforward. But real DAGs are messier. There might be many paths between any two nodes, and each path might contain multiple triplet structures.

So here's the formal definition. Two nodes X and Y are d-separated given a set of conditioning variables Z if *every* path between X and Y is blocked. If they're d-separated, they're conditionally independent given Z. *(pause)*

And a path is blocked if it contains either a chain or fork where the middle node is in your conditioning set, *or* a collider where the middle node and its descendants are *not* in your conditioning set. Same three rules we just learned, now applied path by path across the whole graph.

## Slide: Applying d-Separation: An Example
Let's work through this together. Look at the DAG on this slide. Budget flows to Training, which flows to Quality, which flows to NMR. And Equipment also flows into Quality from below.

*(pause)* First question: Is Training d-separated from NMR given Quality? The path is Training to Quality to NMR. That's a chain, and Quality is in our conditioning set. Chain with the middle node conditioned on — blocked. So yes, Training and NMR are d-separated given Quality. If we know the quality of care, learning about training tells us nothing new about NMR.

Second question: Is Training d-separated from Equipment given Quality? The path is Training to Quality, and Equipment to Quality. Wait — that's Training arrow to Quality, *and* Equipment arrow to Quality. Quality is a collider! And it's in our conditioning set. Collider with the middle node conditioned on — opened. So no, Training and Equipment are *not* d-separated given Quality. *(pause)* Conditioning on quality created a spurious association between training and equipment. This is collider bias in action, right here in our own model.

## Slide: d-Separation Decision Procedure
Here's the algorithm, in four steps. One — list all paths between X and Y. Two — for each path, identify every triplet structure. Three — check if any triplet blocks the path. Four — if *all* paths are blocked, you have d-separation.

Look at the box in the middle. A path is blocked if it contains at least one chain or fork with the middle node conditioned on, *or* a collider with the middle node and all its descendants *not* conditioned on. And d-separation holds only if every single path is blocked. Even one open path means information can flow.

*(pause)* Now, why does this matter practically? Look at that green callout. d-Separation tells us which conditional independencies our model *implies*. And those are testable predictions. If we get data and the data disagrees with what our model says should be independent — our model is wrong. That's the scientific payoff. We've turned our beliefs into falsifiable claims.

## Slide: MNH Application: Full Qualitative DAG
Now let's put it all together and build the full model.

## Slide: Identifying the Variables
We're going to build a comprehensive DAG with about ten key nodes. Let's walk through them.

On the left — one strategic option node: Budget Allocation, with four states: People-heavy, Products-heavy, Systems-heavy, or Balanced. That's our lever.

Then six mediating variables — the ovals: Workforce, Training, Equipment, Referral System, Quality of Care, and Coverage. Each with discrete MECE states.

One contextual variable: Baseline Burden — severe, moderate, or low. This is the confounder we need to account for.

And two objective nodes at the end: NMR and MMR. Those are what we're trying to reduce.

*(pause)* This variable selection step is arguably the most important — and hardest — part of building a causal model. What you include, what you exclude, and how you define the states... those choices shape everything downstream.

## Slide: The Full DAG Structure
And here's the complete picture. Take a moment to look at the layout.

Budget is on the left — that's our decision. It flows through multiple pathways: directly to Workforce, Equipment, Referral System, and Training. Those mediators feed into Quality of Care in the middle. Quality then drives both NMR and MMR on the right. And Baseline Burden sits up top as a confounder, influencing the outcomes directly.

*(pause)* Notice the layered structure: decisions on the left, mediators in the middle, outcomes on the right, confounders above. Each arrow tells a story about how investment translates into outcomes. Trace any path from Budget to NMR — every single one goes through Quality. That makes Quality the central bottleneck of the entire model. Everything has to flow through it.

## Slide: Assigning Signs to Every Link
This table assigns a sign and a rationale to all thirteen links in the DAG. Let me walk through a few.

Budget to Workforce — plus — more funding enables hiring and retention. Budget to Equipment — plus — more funding procures CPAP machines, PPH bundles, ultrasound. Training to Quality — plus — trained staff deliver better care. Quality to NMR — minus — better care reduces mortality. *(pause)*

Every single one should make intuitive sense. And here's what's important — having the rationale written down makes the model *debatable*. If a colleague disagrees with a sign, they can point to exactly which link and exactly which assumption they contest. That's so much more productive than arguing about vague intuitions. "I disagree with your model" becomes "I disagree that more equipment always improves quality — I think it depends on whether staff know how to use it." And now you can have a real conversation.

## Slide: Identifying Triplets Within the Model
Now it's pattern recognition time. Our DAG contains all three triplet types.

Look at the green box — chains. Budget to Training to Quality. Referral System to Coverage to Quality. Budget to Workforce to Quality to NMR. Conditioning on the mediator blocks each of these paths.

The blue box — forks. Workforce and Equipment are both children of Budget. NMR and MMR are both children of Quality. Training and Referral System are both children of Budget. These are common cause structures. Conditioning on the common parent blocks the spurious correlation between the children.

*(pause)* And then the red box — colliders. This is where it gets dangerous. Workforce and Equipment both point into Quality. Training and Equipment both point into Quality. Coverage and Workforce both point into Quality. Quality is a collider for all of these pairs. That means — and this is critical — if you run a regression controlling for quality of care, you create a spurious association between staffing and equipment investment. Collider bias. Be very careful about what you condition on.

## Slide: Testable Implications
Here's the scientific payoff. Our qualitative DAG generates specific conditional independence predictions that we can actually test against data.

Training should be independent of Equipment, given Budget. That's a fork structure. Training should be independent of NMR, given Quality. That's a chain. Workforce and Equipment should *not* be independent given Quality — because Quality is a collider and conditioning on it opens the path. *(pause)*

If we get health data and any of these predictions are violated, we know our model needs revision. And that's the whole point. A model that can't be wrong is a model that can't teach you anything. These testable implications are what make our diagram more than just a pretty picture — they make it a scientific claim.

## Slide: R Code Workshop
Let's build and analyze this DAG in R.

## Slide: R: Define the Full MNH DAG with dagitty
Alright, let's open R. We're going to define our full ten-node MNH DAG using the dagitty package. You'll specify all thirteen causal links — every arrow we just discussed — and then we'll verify the graph is acyclic. *(pause)* If dagitty says it's a valid DAG, we know we haven't accidentally created any feedback loops. That's our first sanity check.

## Slide: R: Visualize the DAG Color-Coded by Role
Now let's see what our model actually looks like. We're going to create a color-coded visualization that distinguishes the different node roles. Budget in blue — that's our decision. Mediators in green — workforce, training, equipment, referral system, coverage, and quality. Baseline burden in amber — the contextual confounder. And NMR and MMR in red — the outcomes we care about. *(pause)* This visual layout makes the flow of the model immediately intuitive. Left to right, decisions to outcomes, with the machinery of change in between.

## Slide: R: Test d-Separation
Here's where we check our hand calculations against the computer. We're going to run five d-separation queries on our MNH DAG.

Is Training d-separated from NMR given Quality? We said yes — it's a chain, conditioning on the middle blocks it. Is Workforce d-separated from Equipment unconditionally? We said no — Budget is a common parent creating a fork. Is Workforce d-separated from Equipment given Budget? We said yes — conditioning on the common cause blocks the fork. Is Workforce d-separated from Equipment given Quality? We said no — Quality is a collider and conditioning on it opens the path. *(pause)*

Run the code and check. If your answers match dagitty's output, you've got the triplet rules down. If any surprise you, go back and trace the path by hand.

## Slide: R: Enumerate All Paths
Now let's use dagitty's paths function to list all directed paths from Budget to NMR and from Budget to MMR. This shows you all the different channels through which investment flows to reach the outcomes.

*(pause)* Notice how many paths there are. Budget reaches NMR through workforce, through training, through equipment, through the referral system and coverage — each one a distinct causal pathway. And we can also look at paths between Workforce and Equipment through the collider Quality, to see how conditioning on Quality would connect variables that are otherwise independent.

## Slide: R: Implied Conditional Independencies
This is the grand finale of the coding session. We're going to use dagitty to generate the *complete* list of conditional independencies implied by our DAG. Every single one of these is a testable prediction our model makes.

*(pause)* Look at the output. Training should be independent of Equipment given Budget. Workforce should be independent of Referral System given Budget. Training should be independent of Baseline Burden. And so on. Each one of these is a claim that, if our model is correct, should hold in the data. When we get to Chapter 10 and start working with real health system data, we can check every single one of these predictions. If the data says two variables are associated when our model says they should be independent, we know exactly where our model needs to be revised.

## Slide: Key Takeaways
Three things I want you to take away from today.

First, a DAG encodes your causal beliefs explicitly using four node types and signed directed links. It takes what's in your head and puts it on paper where people can see it, question it, and improve it.

Second, the three triplet structures — chain, fork, and collider — govern all information flow. Chains and forks are open naturally and blocked by conditioning. The collider is the dangerous exception — blocked naturally and *opened* by conditioning. Please remember that.

*(pause)* Third, d-separation translates graph structure into testable predictions. If the data disagrees with what your model implies, your model needs fixing.

And for MNH specifically, the big insight is that People, Products, and Systems investments are complements flowing through Quality of Care — and that conditioning on Quality creates collider bias between the investment pillars. Be careful what you control for.

## Slide: Looking Ahead
Next session we put these tools to work in a structured case study. We'll be building a DAG from stakeholder interviews, translating people's qualitative beliefs into formal diagrams, and identifying where they agree, where they disagree, and what assumptions are hiding underneath the surface. *(pause)* That sets us up for Chapter 4, where we add actual numbers — probabilities — to the structure we've built. The qualitative skeleton gets quantitative flesh.
