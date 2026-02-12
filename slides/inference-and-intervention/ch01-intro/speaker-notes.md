# Speaker Notes — Chapter 1: Introduction to Causal Analysis

## Overview
This chapter sets the stage for the entire course. The big idea is deceptively simple: if you want to make good decisions about where to invest scarce resources, you need to understand what *causes* what — not just what correlates with what. We introduce the two core tasks of any manager (figuring out what's happening, and deciding what to do), show how correlation-based analysis can lead you catastrophically astray, and preview the causal modeling toolkit that the rest of the course builds on.

## Slide: Learning Objectives
These five objectives map directly to the arc of the chapter. We start with the manager's two questions (assessment vs. intervention), move through the "correlation is not causation" warning with concrete MNH examples, then introduce the building blocks of causal models. By the end of this session, students should understand *why* this toolkit exists — the "how" comes in later chapters.

## Slide: Chapter Overview
Think of this as the roadmap for today. We move from the philosophical ("What does a manager actually do?") to the practical ("Here's a diagram that can save you from a billion-dollar mistake"). The five-step flow — Assessment, Intervention, Correlation traps, Causal framework, MNH application — mirrors the journey every analyst goes through when they encounter a new problem.

## Slide: The Manager's Two Questions
This is the foundation of the whole course. Every manager, whether they're running a hospital or a multinational health program, faces exactly two questions: "What's going on?" and "What should I do about it?" The first is situational assessment — detective work. The second is intervention — choosing which levers to pull. The critical insight is that you can't answer the second question well without answering the first one properly, and answering the first one properly requires causal thinking.

## Slide: Situational Assessment in Practice
The point here is that causal reasoning isn't just for academics — it's what practitioners already do, just informally. A police inspector weighing evidence about a cause of death, a technical advisor diagnosing why health outcomes are declining — they're all doing situational assessment. The difference is that they're doing it in their heads, with all the biases and blind spots that implies. Causal models make this reasoning explicit and shareable.

## Slide: The Maxwell Example
This is from the Ryall & Bramson textbook and it's a great hook. Robert Maxwell, the media mogul, was found dead off his yacht. The McKinsey-style approach would be to build an issue tree — heart attack? suicide? murder? — and check off categories. But causal thinking asks a different question: what *caused* each possibility, and what *evidence* would each cause produce? It's the difference between organizing information and actually reasoning about it. This sets up the idea that causal models help us both trace causes backward and predict evidence forward.

## Slide: Managers Manage Scarce Resources
This slide makes a point that sounds obvious but has profound implications. Resources are always limited. Every dollar you spend on CPAP machines is a dollar you didn't spend on training midwives. Constraints force choices, and choices require understanding what causes what. If you don't know which investments actually *cause* better outcomes, you're just guessing — and guessing with millions of dollars and thousands of lives at stake.

## Slide: The Feather Touch Cautionary Tale
This is the "scare them straight" slide. The TruSmartz consulting example shows what happens when you run a regression without thinking about causal structure. The data shows a negative correlation between demand generation and service utilization — so the naive recommendation is to *stop* doing demand generation. But the real story is that program managers treated demand generation and subsidies as substitutes: when they ran one, they didn't run the other. The correlation captured the manager's decision-making pattern, not the causal effect of the programs. This is the kind of mistake that costs lives.

## Slide: The Causal Truth
Now we reveal what was actually going on. The DAG shows that demand generation and subsidies are linked by a decision node — managers choose between them — and both have positive effects downstream. The negative correlation in the data was an artifact of the substitution pattern, not a real causal effect. The correct recommendation is to run both programs together, not to cancel one. This is the single most important example in the chapter because it demonstrates, concretely, how a causal model corrects a dangerous error.

## Slide: Regression vs. Causal Model: The Numbers
This table drives the point home with hard numbers. The single-stage regression literally recommends the worst option — stopping subsidies and demand generation. The causal model correctly identifies running both as the best intervention, with an impact of +816 units versus the regression's recommended action that would lose -832 units. That's a swing of over 1,600 impact units. In the MNH context, those units are lives. Let that sink in.

## Slide: Trap 1: Confounding
Now we move to the three classic traps. Confounding is when a hidden third variable drives both the supposed cause and the supposed effect. The MNH example is vivid: countries with more health workers have *higher* mortality. Does deploying health workers cause deaths? Of course not — health workers are sent to the sickest areas. Disease burden is the confounder that drives both deployment and mortality. If you don't account for it, you get the relationship backwards.

## Slide: Trap 2: Reverse Causation
This one trips people up constantly in development work. Countries receiving more donor funding have higher mortality rates. Does funding cause death? No — high mortality attracts funding. The causal arrow runs in the opposite direction from what the naive analysis suggests. This is why you can't just look at correlations and draw policy conclusions.

## Slide: Trap 3: Selection Bias
Selection bias is subtler than the other two. The data you see isn't a random sample — it's filtered by some selection process. In the MNH example, only well-resourced hospitals report data to DHIS2. So when you analyze DHIS2 data, you're only looking at the hospitals that are already doing well. The facilities where CPAP would make the biggest difference — the under-resourced ones — are invisible in your data. Your analysis is biased before you even start.

## Slide: Three Traps Summary
This summary table is worth memorizing. All three traps share a common thread: they create statistical associations that look like causal effects but aren't. Confounding, reverse causation, and selection bias each fool you in a different way, but the antidote is the same — explicit causal modeling that forces you to think about *why* the association exists, not just *that* it exists.

## Slide: Elements of a Causal Model
Here we introduce the basic vocabulary. A causal model is just a directed graph: nodes are variables, arrows represent causal relationships, and signs tell you the direction of effect. The critical rule is that an arrow from A to B means changing A can change B, but not vice versa — causation has a direction. And the "acyclic" part of DAG means no feedback loops (at least in this framework). This is deliberate — it forces you to think carefully about the direction of causation.

## Slide: A Simple MNH Causal Model
This three-node chain — Investment → Coverage → NMR — is the simplest possible model of the MNH program. More money increases coverage, and more coverage reduces mortality. It's a starting point, not a finished product. The important thing is that even this simple model already tells you something: investment doesn't directly reduce mortality; it works *through* coverage. That means if coverage isn't increasing, throwing more money at the problem won't help. But this model is clearly too simple — what about confounders? What about the quality of care? That's what the rest of the course is about.

## Slide: Preview: What's Coming
This roadmap gives students the big picture. Chapters 2-3 build qualitative models (drawing the diagrams), Chapters 4-5 add numbers (probabilities), Chapter 6 tackles common analytical pitfalls, Chapters 7-9 move to decision-making, and Chapter 10 circles back to learning causal structure from data. Each piece builds on the last. By the end, students will have a complete toolkit for going from raw data and expert interviews to actionable investment decisions.

## Slide: The MNH Investment Challenge
This slide grounds everything in the scale of the problem. We're talking about 182,000 maternal deaths, 950,000 newborn deaths, and 1.2 million stillbirths per year in sub-Saharan Africa alone. The target for programs like this is to save hundreds of thousands of lives. At that scale, getting the causal analysis wrong doesn't just waste money — it costs lives that could have been saved.

## Slide: The Causal Investment Question
The three pillars — People, Products, and Systems — are the standard investment categories in MNH programming. The fundamental question is: which combination of investments across these three pillars will *cause* the greatest reduction in mortality? Note the emphasis on *cause*. Correlation analysis might tell you which countries happen to have the best outcomes, but it can't tell you which investments will move the needle. That requires causal reasoning.

## Slide: Why Naive Data Analysis Fails
This two-column comparison makes the point concrete. The naive correlation says "Country A gets the most funding and has the most deaths — therefore funding causes deaths!" The causal reasoning says "Country A has the highest burden *and* the greatest potential for lives saved — the investment is targeted at the cause." Same data, opposite conclusions. Which analysis would you want to base a billion-dollar investment on?

## Slide: Building a Richer Causal Model
Now we sketch out what a more realistic model looks like. Budget allocation is a decision node (we control it), and it flows through three mediating pathways — workforce, equipment, and data systems — into quality of care, which then drives mortality. This is still a simplification, but it's already much richer than the three-node chain. Notice the confounders we haven't drawn yet: baseline disease burden, government capacity, political stability. Those will be added in coming chapters.

## Slide: R: Setting Up the Environment
Live coding walkthrough. Students install and load dagitty, ggdag, and ggplot2 — the three packages they'll use throughout the course.

## Slide: R: A Simple MNH Causal Model
Live coding walkthrough. Students create their first DAG in R using dagitty, defining the three-node Investment → Coverage → NMR chain and visualizing it with ggdag.

## Slide: R: A Confounded Model
Live coding walkthrough. Students build a confounded DAG — Hospital Delivery and Neonatal Mortality, with Complication Severity as a confounder — and visualize it with exposure and outcome coloring.

## Slide: R: Finding Adjustment Sets
Live coding walkthrough. Students use dagitty's adjustmentSets() function to discover that Complication Severity must be controlled for. This is the computational payoff — the DAG tells you exactly what to adjust for.

## Slide: R: A Richer MNH Model
Live coding walkthrough. Students build the full MNH theory-of-change DAG with budget, workforce, equipment, data systems, quality, NMR, and baseline burden, then identify adjustment sets for the Budget → NMR relationship.

## Slide: Key Takeaways
Three things to remember from this chapter. First, causal modeling serves two purposes: understanding what's happening (assessment) and deciding what to do (intervention). Second, correlation is not causation — confounding, reverse causation, and selection bias all create misleading associations. Third, a causal model makes your assumptions explicit, testable, and actionable. This isn't just theory — it's essential for allocating large-scale program funding effectively.

## Slide: Looking Ahead
Next time we'll learn the formal language of causal diagrams: four node types, signed directed links, and the three fundamental triplet structures that govern how information flows through a causal model. This is where we go from "causal thinking is important" to "here's exactly how to do it."
