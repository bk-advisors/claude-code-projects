# Speaker Notes — Chapter 1: Introduction to Causal Analysis

## Overview
Welcome to the course. Today we're going to talk about a deceptively simple idea — one that will change how you think about data, decisions, and program design. The idea is this: if you want to make good decisions about where to invest scarce resources, you need to understand what *causes* what, not just what correlates with what. That distinction is going to be at the center of everything we do together.

## Slide: Learning Objectives
So here are the five things I want you to walk away with today. *(pause)* First, we'll learn to distinguish between two things every manager does — assessing a situation and choosing an intervention. Then we'll work through some real MNH examples that show why correlation is not causation — and how that confusion can lead to catastrophically wrong decisions. We'll look at three specific traps that trip people up, introduce the basic building blocks of causal models, and by the end, you should have a clear sense of *why* this toolkit matters. The "how" — that's what the rest of the course is for.

## Slide: Chapter Overview
Think of this as our roadmap for today. We're going to move from the philosophical — "What does a manager actually do?" — to the practical — "Here's a diagram that can save you from a billion-dollar mistake." *(pause)* See the five steps up there? Assessment, Intervention, Correlation traps, Causal framework, MNH application. That mirrors the journey every analyst goes through when they encounter a new problem. And notice the core insight at the bottom — in a world of scarce resources, figuring out *which* program elements to focus on has to come before deciding *how* to implement them. That requires understanding causality.

## Slide: Situational Assessment
Alright, let's start with the first big idea.

## Slide: The Manager's Two Questions
This is the foundation of the whole course. Every manager — whether you're running a hospital, overseeing a district health program, or managing a multinational MNH initiative — faces exactly two questions. *(pause)* Look at the two boxes. On the left: "What is happening?" That's situational assessment — it's detective work. On the right: "What should I do about it?" That's intervention — choosing which levers to pull.

Here's the critical insight: you can't answer the second question well without answering the first one properly. And answering the first one properly? That requires causal thinking. If you misdiagnose *why* neonatal mortality is high in a district, you're going to prescribe the wrong intervention. It's like a doctor treating the wrong disease.

## Slide: Situational Assessment in Practice
So what does situational assessment actually look like in practice? *(pause)* Look at the examples as they come up. A police inspector weighing evidence about a cause of death. A technical advisor trying to figure out why health outcomes are declining in a particular region. A program director asking, "Why isn't the neonatal mortality rate going down in this country despite everything we've invested?"

They're all doing the same thing — gathering evidence and reasoning about causes. The difference is, they're usually doing it in their heads, with all the biases and blind spots that implies. What causal models do is make that reasoning explicit and shareable. Instead of two people arguing from gut feel, you put the diagram on the table and debate the *structure* of the argument.

## Slide: The Maxwell Example
Now, the textbook by Ryall and Bramson opens with a really compelling example, and I want to walk you through it. *(pause)* Robert Maxwell — big media mogul — was found dead off his yacht in 1991. Now, the classic McKinsey-style approach would be to build an issue tree. How did he die? Break it into MECE categories: heart attack, suicide, murder. Check them off systematically.

But causal thinking asks a fundamentally different question. Not just "what are the categories?" but "what *caused* each possibility, and what *evidence* would each cause produce?" *(pause)* See the difference? The issue tree organizes information. The causal model actually reasons about it. It helps you trace causes backward — what could have led to this? — and predict evidence forward — if this was the cause, what should we expect to find? That's a much more powerful way to think.

## Slide: Managerial Intervention
Okay, now let's move to the second big question — what should I do about it?

## Slide: Managers Manage Scarce Resources
This slide makes a point that sounds obvious but has really profound implications. *(pause)* Resources are always limited. Money, time, personnel, equipment — you never have enough. And that means every intervention involves trade-offs. Every dollar you spend on CPAP machines is a dollar you didn't spend on training midwives. Every month you invest in building data systems is a month you're not spending on direct service delivery.

Now think about a large-scale MNH initiative — pooled investments across multiple countries. The stakes are enormous. Every dollar matters, and those dollars represent lives. So which interventions will actually *cause* the greatest reduction in mortality? *(pause)* If you don't know the answer to that causal question, you're just guessing. And guessing with millions of dollars and thousands of lives on the line — that's not a position anyone wants to be in.

## Slide: The Feather Touch Cautionary Tale
Okay, now I want to scare you a little. *(pause)* This is my "scare them straight" example, and it comes from the textbook, adapted to our MNH context.

Here's the setup. A consulting organization — let's call them TruSmartz — analyzes data on an MNH program across multiple countries. And they find something surprising. Countries with more demand generation for health services actually show *lower* service utilization. Countries running subsidy programs also show lower utilization. So what does the regression model recommend? *(pause)* Stop doing demand generation. Cut the subsidies. That's what the data says, right?

Now, look at the red box at the bottom. What went wrong? The regression captured *correlations in the data*, not *causal effects*. What was actually happening is that program managers were treating demand generation and subsidies as substitutes. When they ran one, they didn't run the other. So the negative correlation between demand generation and utilization wasn't a causal relationship — it was an artifact of how managers were making decisions. And if you followed TruSmartz's recommendation, you'd be cutting programs that actually work.

## Slide: The Causal Truth
Now let's look at what was actually going on. *(pause)* Look at the diagram. See how demand generation and subsidy decisions are linked? Managers treated them as substitutes — when one was active, the other wasn't. That creates a negative correlation between them in the data. But look at the arrows going right — subsidies drive care-seeking behavior, which drives service utilization. Both are positive effects.

So the correct recommendation isn't to stop demand generation — it's to run subsidies *alongside* demand generation, not as a replacement for it. The single-stage regression got the sign completely wrong. The causal model gets it right. *(pause)* This is the single most important example in this chapter, because it shows concretely how a causal model corrects a dangerous error.

## Slide: Regression vs. Causal Model: The Numbers
And now let's put hard numbers on it. *(pause)* Look at this table carefully. The single-stage regression — that's the TruSmartz approach — literally recommends the worst option. It says stop subsidies for +73 impact units, stop demand generation for +282. But the true causal effect? Stopping subsidies costs you -832 impact units. Running both together gives you +816.

That's a swing of over 1,600 impact units between what the regression recommends and what you should actually do. *(pause)* In the MNH context, those units represent lives. Let that sink in. The naive regression doesn't just get it a little wrong — it recommends the exact opposite of the right answer.

## Slide: Correlation Does Not Equal Causation
Now let's dig into *why* correlations mislead us. There are three classic traps, and we're going to walk through each one.

## Slide: Trap 1: Confounding
First up: confounding. *(pause)* This happens when a hidden third variable drives both the thing you think is the cause and the thing you think is the effect.

Here's the MNH example. Look at the data: countries with more health workers deployed have *higher* neonatal mortality. So... does deploying health workers cause deaths? *(pause)* Of course not. What's happening is that health workers get sent to the sickest areas. Disease burden is the confounder — it drives both where workers are deployed *and* where mortality is high. Look at the diagram at the bottom: Disease Burden has arrows going to both Health Worker Deployment and Neonatal Mortality. If you don't account for it, you get the relationship completely backwards.

## Slide: Trap 2: Reverse Causation
Second trap: reverse causation. This one trips people up constantly in development work. *(pause)*

Look at the example. Countries receiving more donor funding have higher mortality rates. Does funding cause death? No — high mortality attracts funding. The causal arrow runs in the opposite direction from what the naive analysis suggests. See the two models side by side? The assumed model says "Donor Funding leads to Higher Mortality." The actual model says "Higher Mortality leads to More Donor Funding." Same data, completely opposite causal story. *(pause)* This is why you can't just look at correlations and draw policy conclusions.

## Slide: Trap 3: Selection Bias
Third trap, and this one is subtler than the other two. Selection bias. *(pause)*

The issue here is that the data you're looking at isn't a random sample — it's been filtered by some selection process. In this MNH example, think about DHIS2 data. Only well-resourced hospitals report to DHIS2. So when you analyze that data, you're only seeing hospitals that are already doing relatively well. The facilities where an intervention like CPAP would make the biggest difference — the under-resourced ones — are invisible in your dataset. Your analysis is biased before you even start, and you might not even realize it.

## Slide: Three Traps Summary
Okay, let's pull it all together. *(pause)* Look at this summary table — it's worth memorizing. All three traps share a common thread: they create statistical associations that look like causal effects but aren't. Confounding, reverse causation, and selection bias each fool you in a different way, but the antidote is the same — explicit causal modeling that forces you to think about *why* the association exists, not just *that* it exists.

That bottom line is the key takeaway: the antidote is explicit causal modeling. And that's exactly what we're going to build next.

## Slide: The Causal Model Framework
Alright, now here's where it gets interesting. We've talked about why you need causal thinking. Now let's talk about the actual tools.

## Slide: Elements of a Causal Model
So what *is* a causal model? *(pause)* It's actually simpler than you might think. It's a directed graph — just nodes and arrows. Nodes represent variables in your system. Arrows represent causal relationships. And signs — plus or minus — tell you the direction of the effect.

Now, there's one critical rule, and I want you to really internalize this. An arrow from A to B means that changing A can change B. But it does *not* mean changing B changes A. Causation has a direction. *(pause)* And see the definition at the bottom? DAG — Directed Acyclic Graph. "Acyclic" means no feedback loops, at least in this framework. You can't follow arrows from any node back to itself. That's deliberate — it forces you to think very carefully about which direction causation runs.

## Slide: A Simple MNH Causal Model
Here's our first causal model, and it couldn't be simpler. Three nodes in a chain. *(pause)* Investment goes to Coverage, Coverage goes to Neonatal Mortality Rate. More money increases coverage — that's the plus sign. Higher coverage reduces mortality — that's the minus sign.

Now, notice something important. Investment doesn't directly reduce mortality. It works *through* coverage. That's the mediator. And that tells you something actionable: if coverage isn't increasing, throwing more money at the problem won't help. You need to figure out *why* coverage isn't responding to investment.

But clearly this model is too simple, right? What about confounders? What about quality of care? What about all the complexity of real health systems? *(pause)* That's exactly what the rest of the course is about. We're going to build richer and more realistic models chapter by chapter.

## Slide: Preview: What's Coming
Speaking of which, here's your roadmap for the full course. *(pause)* Chapters 2 and 3 build qualitative models — that's learning to draw the diagrams and doing a real case study. Chapters 4 and 5 add numbers — probability tables, Bayes' rule, situational analysis. Chapter 6 tackles a common analytical trap called Simpson's Paradox. Chapters 7 through 9 move to decision-making — choosing optimal interventions, allocating resources, even game theory for when donors and governments interact strategically. And Chapter 10 circles back to learning causal structure from data.

Each piece builds on the last. By the end, you'll have a complete toolkit for going from raw data and expert interviews to actionable investment decisions.

## Slide: MNH Application
Now let's ground all of this in the real problem we're here to solve.

## Slide: The MNH Investment Challenge
Look at these numbers. *(pause)* 182,000 maternal deaths per year in sub-Saharan Africa — that's 70% of the global total. 950,000 newborn deaths. 1.2 million stillbirths. The target for a large-scale MNH initiative is to save hundreds of thousands of lives over the program period.

At that scale, getting the causal analysis wrong doesn't just waste money — it costs lives that could have been saved. That's why everything we've been talking about today matters. This isn't abstract statistics. It's the difference between effective programs and wasted resources.

## Slide: The Causal Investment Question
So where does the money go? *(pause)* A typical MNH initiative invests across three pillars. People — the health workforce. Products — MNH innovations and equipment. Systems — data and referral infrastructure.

And the fundamental question is right there in the orange box: which combination of investments across these three pillars will *cause* the greatest reduction in mortality? *(pause)* Notice the emphasis on *cause*. Correlation analysis might tell you which countries happen to have the best outcomes. But it can't tell you which investments will actually move the needle. That requires causal reasoning.

## Slide: Why Naive Data Analysis Fails
Let me show you exactly how this goes wrong. *(pause)* Suppose you compare spending versus outcomes across your target countries. Look at the left column — the naive correlation. Country A receives the most funding and has the highest absolute deaths. "More spending equals more deaths!" Sounds damning, right?

Now look at the right column — the causal reasoning. Country A has the highest burden *and* the greatest potential for lives saved. The investment is targeted at the cause of mortality. It's not correlated with mortality by accident — it's directed there on purpose. *(pause)* Same data, opposite conclusions. Which analysis would you want to base a major investment on?

## Slide: Building a Richer Causal Model
Okay, now let's sketch out what a more realistic model looks like. *(pause)* Look at this diagram. Budget allocation is on the left — that's a decision node, the rectangle, meaning we control it. It flows through three mediating pathways: workforce training, equipment supply, and data systems. Those all feed into quality of care, which then drives mortality reduction.

This is still a simplification, but it's already much richer than the three-node chain we started with. And notice the bullet point about confounders we haven't drawn yet — baseline disease burden, government capacity, political stability. Those all matter, and they'll be added in the coming chapters. The point for now is that even a relatively simple causal diagram gives you a much clearer picture of how investment translates into outcomes.

## Slide: R Workshop
Now let's get our hands dirty with some code.

## Slide: Setting Up the R Environment
Alright, first things first — let's get our tools installed. You'll need three packages: dagitty for specifying and analyzing DAGs, ggdag for making nice visualizations, and ggplot2 for general plotting. If you haven't installed them yet, uncomment that first line and run it. Otherwise, just load the libraries. *(pause)* These three packages are going to be our core toolkit throughout the entire course, so make sure they're working before we move on.

## Slide: R: A Simple MNH Causal Model
Now let's build our first DAG in code. *(pause)* Look at the dagitty syntax — it's pretty intuitive. We define three nodes: Investment, Coverage, and NMR. We specify their positions so they lay out nicely. Then we draw the arrows: Investment causes Coverage, Coverage causes NMR. That's it — that's our three-node chain from earlier, but now it's in R where we can analyze it computationally. The ggdag call at the bottom renders it as a plot.

## Slide: R: A Confounded Model
Now let's make things more interesting. *(pause)* Here we're building a confounded DAG. We have Hospital Delivery and Neonatal Mortality — and sitting above both of them is Complication Severity. Severity causes both hospital delivery decisions *and* mortality outcomes. That's our confounder. Notice how we use ggdag_status to color-code the exposure and outcome — green for Hospital Delivery, red for Neonatal Mortality, amber for the confounder. Makes the structure really pop visually.

## Slide: R: Finding Adjustment Sets
And here's the computational payoff. *(pause)* We call adjustmentSets on our confounded DAG, telling it we want the causal effect of Hospital Delivery on Neonatal Mortality. And what does it return? Complication Severity. The DAG is telling us: "If you want to estimate the true causal effect, you *must* control for complication severity." Without that adjustment, your estimate is biased by confounding. *(pause)* This is incredibly powerful — the DAG does the statistical thinking for you.

## Slide: R: A Richer MNH Model
Finally, let's build the full theory-of-change DAG. *(pause)* We've got Budget flowing to Workforce, Equipment, and Data Systems. Those three feed into Quality, which drives NMR. And we've added Baseline Burden as a confounder that affects both NMR directly and Budget allocation decisions. When we ask for adjustment sets for the Budget-to-NMR relationship, dagitty tells us exactly what we need to control for. Go ahead and run this code and see what it returns.

## Slide: Key Takeaways
Alright, let's wrap up with the three things I want you to remember from today. *(pause)* First, causal modeling serves two purposes: understanding what's happening — that's assessment — and deciding what to do about it — that's intervention. Second, correlation is not causation. Confounding, reverse causation, and selection bias all create misleading associations. And third, a causal model makes your assumptions explicit, testable, and actionable.

This isn't just theory. When you're allocating program funding at scale, getting the causal structure right is the difference between saving lives and wasting resources.

## Slide: Looking Ahead
Next time, we're going to learn the formal language of causal diagrams. *(pause)* Four node types, signed directed links, and the three fundamental triplet structures that govern how information flows through any causal model. That's where we go from "causal thinking is important" to "here's exactly how to do it." See you then.
