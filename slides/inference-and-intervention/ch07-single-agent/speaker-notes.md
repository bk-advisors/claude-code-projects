# Speaker Notes — Chapter 7: Single-Agent Interventions

## Overview
Alright everyone, welcome to what I think is the real turning point in this course. For six chapters we've been building up our ability to figure out what's going on — inference, diagnosis, understanding the system. Today we flip the question entirely. Instead of asking "What is happening?" we're going to ask "What should I do?" We'll learn the tools that take us from understanding to action: influence diagrams, expected value, the value of information, and the crucial difference between observing and intervening.

## Slide: Learning Objectives
So here's what we're after today — five objectives that take you from passive analysis to active decision-making. *(pause)* First, we're going to extend our causal models into influence diagrams by adding decisions and objectives to the mix. Then we'll learn how to compute expected value — the basic math for comparing options. After that, we'll figure out how to quantify what better information is actually worth before you commit resources. And then we'll tackle the deepest conceptual issue in the whole course — the difference between seeing that something is correlated and actually doing something about it. Finally, we'll pull it all together with a full MNH decision analysis. So by the end of today, you'll have a complete framework for choosing among interventions under uncertainty.

## Slide: Chapter Overview
Take a look at this five-step flow — it maps the entire logic of the chapter. We start by building the decision framework, influence diagrams. Then the math for comparing options, expected value. Then we ask a really practical question: should we invest in learning more before we decide? That's value of information. Then we tackle the deepest conceptual issue — what's the difference between observing something and actually intervening on it? And finally, we apply everything to a real MNH investment decision. *(pause)* And look at that callout at the bottom. That's the key message for today. We're making the shift from "What is happening?" to "What should I do?"

## Slide: From Analysis to Decision
Alright, let's get into it. This section is about the fundamental difference between inference and intervention.

## Slide: Two Modes of Causal Reasoning
Okay, look at these two columns side by side. This really crystallizes the structure of the entire course. *(pause)* On the left, inference — that's Chapters 1 through 6, what we've been doing. We observe evidence and update our beliefs. "District X has high neonatal mortality — what's the most likely cause? Maybe staffing is low." On the right, intervention — that's where we're headed now. We choose an action and predict its consequences. "If we deploy CPAP machines, how much will NMR actually decrease?" *(pause)* Same Bayesian network underneath, but completely different questions. Now look at that orange callout at the bottom — this is worth spending a minute on. P of NMR given CPAP equals yes is *not* the same as P of NMR given do-CPAP equals yes. Observing that facilities with CPAP happen to have lower mortality is not the same thing as knowing that deploying CPAP will lower mortality. The first one reflects existing correlations. The second one requires genuine causal reasoning. That distinction is going to be one of the most important ideas in this chapter.

## Slide: Why the Distinction Matters
So why does this matter in practice? Let me make it concrete with this CPAP example. *(pause)* Look at the observation: facilities with CPAP machines have 30% lower neonatal mortality. Sounds great, right? Ship CPAP everywhere and you'll cut mortality by a third. But wait — those facilities also tend to have more staff, better training, and stronger management. The observed 30% is conflating the causal effect of CPAP with everything else that comes along with being a well-resourced facility. *(pause)* Now look at the intervention line. If we actually deploy CPAP to a facility that currently lacks it — changing nothing else — the true causal effect might be a 12% reduction. Still valuable! But it's a lot less than 30%. And if you based your budget on the naive number, you'd overinvest in equipment and underinvest in the human factors that are actually driving most of that association.

## Slide: Influence Diagrams
Now let's build the toolkit for making these decisions. We're going to add decisions and objectives to our causal models.

## Slide: Three Node Types in Influence Diagrams
So up until now, our Bayesian networks have only had one type of node — chance nodes, which represent uncertain variables. Now we're adding two more. *(pause)* Look at the table. We still have chance nodes — ovals — for things like NMR and Quality of Care. But now we add decision nodes — rectangles — for things we actually control, like budget allocation or which intervention to choose. And objective nodes — hexagons — for what we're trying to optimize, like lives saved or cost-effectiveness. *(pause)* This is what makes the framework actionable. A Bayesian network lets you do inference. An influence diagram — which is just a Bayesian network plus decisions and objectives — lets you find optimal decisions. That's the progression in the callout at the bottom: Bayesian network gives you inference, influence diagram gives you optimal decisions.

## Slide: A Simple Influence Diagram
Here's the simplest possible MNH decision model. Take a look at the diagram. *(pause)* One decision node on the left — "Deploy CPAP?" — that's the rectangle, the thing we control. One chance variable in the middle — "Neonatal Outcomes" — influenced by both our CPAP decision and by Baseline Severity coming in from below. And one objective node on the right — "Lives Saved" — the hexagon, what we want to maximize. *(pause)* Now notice something important about the arrows. The arrow from the Decision to Outcomes is a *causal* effect — it represents what happens when we act. But the arrow from Baseline Severity to Outcomes? That's a contextual influence that we don't control. We can't change the baseline severity. We can only decide whether to deploy CPAP given whatever severity exists.

## Slide: Information Links
Now here's a subtle but really important concept. Information links are dashed arrows pointing into decision nodes. *(pause)* They don't represent causation — they represent what the decision-maker *knows* when they make their choice. Look at this diagram. Pilot Results has an information link into the Scale-Up Decision. That means program leadership can observe the pilot results before deciding whether to scale up. *(pause)* Think about what that means. The presence or absence of that information link is what separates "decide now with what you know" from "learn first, then decide." And that difference, as we'll see shortly, can be worth millions of dollars and thousands of lives.

## Slide: Expected Value Calculation
Okay, now let's talk about how to actually compare options. Time for some math.

## Slide: The Expected Value Framework
Here's the core calculation. Expected value is just the probability-weighted average of all possible outcomes. Nothing more complicated than that. *(pause)* Look at this CPAP deployment table. Three scenarios. There's a 50% chance the equipment works and staff are trained — that saves 2,400 lives. A 20% chance the equipment works but staff aren't trained — that's 800 lives. And a 30% chance of equipment failure — zero lives saved. *(pause)* Multiply each outcome by its probability and add them up: 1,200 plus 160 plus 0 equals 1,360 lives. That's our expected value for CPAP deployment. Now we have a number we can compare against other options. So let's do exactly that.

## Slide: Comparing Two Interventions
Alright, here's the decision. Look at these two options side by side. *(pause)* Option A, CPAP deployment: expected value of 1,360 lives, at a cost of about $14,700 per life saved. Option B, workforce training: expected value of 1,920 lives, at about $10,400 per life. *(pause)* Workforce training wins on both dimensions — more lives saved and better cost-effectiveness. Seems like a clear choice, right? *(pause)* But look at that green callout. This assumes we know the probabilities correctly. What if we're wrong about the attrition rate for the trained workforce? What if attrition turns out to be much higher than we think? That changes everything. And that question — "What if we could learn more before deciding?" — leads us directly to the value of information.

## Slide: Decision Trees
Now let me show you the general procedure for solving these kinds of problems. The decision tree formalizes everything we just did. *(pause)* You start at the objective node — lives saved — and work backward. At each chance node, you compute the expected value by weighting outcomes by their probabilities. At each decision node, you pick the option that maximizes expected value. And you keep working backward — "folding back" is the technical term — until you reach the first decision. *(pause)* This backward induction procedure is the algorithm for solving any influence diagram. Keep it in your back pocket, because you'll use it again in the next chapter for multi-country allocation and in Chapter 9 for game theory.

## Slide: Multi-Stage Decisions
Now, real MNH decisions aren't one-shot — they happen in stages. Look at this flow. *(pause)* Stage 1: decide whether to run a pilot. Then observe the pilot results. Stage 2: decide whether to scale up. And then you get your outcome. *(pause)* This pilot-then-scale structure is how programs actually work in practice. And here's the key insight: the value of running a pilot depends entirely on how much it changes your subsequent decision. If you'd do the same thing regardless of the pilot results, the pilot is worthless — you just wasted $2 million and six months. But if the pilot could genuinely swing you from one strategy to another, then it might be well worth that investment.

## Slide: The Value of Information
Okay, let's put numbers on this. How much should we actually pay for better data?

## Slide: Expected Value of Perfect Information (EVPI)
EVPI answers a deceptively simple question: how much would it be worth to know the truth before you decide? *(pause)* Let's work through it. Without any additional information, we choose workforce training — expected value of 1,920 lives. That's our baseline. *(pause)* Now imagine we could magically learn the true attrition rate before committing. Look at the table. If attrition is low, we'd still pick workforce — 3,200 lives. If it's medium, still workforce — 1,600 lives. But if attrition is high? We'd actually switch to CPAP — 1,360 lives beats the workforce option in that scenario. *(pause)* So the expected value with perfect information is 0.35 times 3,200 plus 0.45 times 1,600 plus 0.20 times 1,360, which gives us 2,112 lives. *(pause)* The EVPI is the difference: 2,112 minus 1,920 equals 192 lives — roughly $2 million in equivalent value. That's the maximum you should ever pay for any information about attrition. It sets the ceiling for your pilot program budget.

## Slide: Expected Value of Sample Information (EVSI)
Now EVSI is the realistic version of what we just calculated. A pilot doesn't give you perfect information — it gives you an imperfect signal. *(pause)* Look at what happens. If the pilot shows "promising," your estimate of low attrition jumps from 0.35 to 0.60. If it shows "mixed," not much changes. If it shows "negative," your estimate of high attrition jumps from 0.20 to 0.55. *(pause)* The pilot updates your beliefs, but it doesn't eliminate uncertainty. And here's the key decision rule: run the pilot if the EVSI exceeds the cost. *(pause)* Now look at the green callout — when does the pilot actually have value? It only matters when the signal could change your decision. And that only happens when the pilot reveals high attrition, which causes you to switch from workforce to CPAP. If the pilot just confirms what you already believed, it didn't change anything.

## Slide: Observing vs. Intervening
Alright, now let's go deep on the most important conceptual distinction in the chapter — the do-calculus and graph surgery.

## Slide: The do-Operator
Here's where we formalize the observe-versus-intervene distinction we've been building toward. *(pause)* do of X equals x means we *force* X to take that value, regardless of what would normally cause X. This is fundamentally different from passively observing X equals x. *(pause)* Look at the two columns. On the left, observing: X takes its value naturally, all causal relationships are still intact, confounders are still active. "Among facilities that *happen to have* CPAP..." On the right, intervening: X is forced to a value, incoming arrows are severed, confounders are blocked. "If we *give* a facility CPAP..." *(pause)* Same variable, same value, completely different meaning. The first tells you about correlations in the world as it exists. The second tells you what would happen if you actually intervened.

## Slide: Graph Surgery
So how do we actually compute this? Graph surgery gives us a mechanical procedure. *(pause)* To find P of Y given do-X-equals-x, you literally delete all arrows pointing into X in the DAG, then compute probabilities in the modified graph. Look at the two diagrams side by side. *(pause)* On the left, the original DAG. Resources is a confounder — it influences both CPAP and NMR. So P of NMR given CPAP includes confounding. On the right, after surgery. We've cut the arrow from Resources to CPAP. Now the only remaining path from CPAP to NMR is the direct causal effect. *(pause)* Look at the orange callout. After surgery, Resources no longer influences CPAP — because we *set* it — so the confounder is blocked. What's left is the true causal effect of CPAP on neonatal mortality. This is the computational backbone of do-calculus, and it's surprisingly elegant once you see it.

## Slide: MNH Application: The CPAP vs. Workforce Decision
Okay, now we put it all together. Let's apply everything we've learned to a full MNH decision analysis.

## Slide: The Decision Context
Here's the scenario. The MNH program has a budget tranche to allocate in a new target country. Program leadership has to choose between three strategies. *(pause)* Strategy A: deploy CPAP machines and PPH bundles across 15 hospitals. Strategy B: train and deploy 200 nurse-midwives across those same hospitals. Strategy C: split — half CPAP, half workforce. *(pause)* Which strategy maximizes expected lives saved? This is realistic — program leaders face exactly these kinds of portfolio allocation decisions. And the three-strategy setup is going to let us see something interesting about diversification.

## Slide: Building the Influence Diagram
Now look at this influence diagram — it's the fullest one we've built so far. *(pause)* The decision node is Strategy Choice on the left. That flows through two intermediate variables — Equipment Availability and Staffing Adequacy — into Quality of Care, and ultimately into our objective, Lives Saved. *(pause)* But notice that confounder at the bottom: Government Co-financing. It affects both equipment sustainability and staff retention, and we don't control it. There's a 60% chance co-financing is low and a 40% chance it's high. That 60/40 split is the dominant source of uncertainty in this whole analysis — and it's the variable the program can least control.

## Slide: Expected Value Analysis
Okay, the numbers. And they tell a surprising story. *(pause)* CPAP-only has the lowest expected value — 1,840 lives. Workforce does better at 2,040. But look at the split strategy — 2,080 lives, the highest of the three. *(pause)* And here's what's really interesting. Look at the variance. Under low co-financing, CPAP drops to 1,200 and workforce drops all the way to 1,000. But the split? It stays at 1,400. Under high co-financing, workforce jumps to 3,600 — the highest single number — but the split still gets you 3,100. *(pause)* The split wins not just on expected value but on consistency. It performs reasonably well under both co-financing scenarios. This is portfolio diversification applied to public health. Don't put all your eggs in one basket when you're facing uncertain government commitment.

## Slide: Sensitivity Analysis
Now let's ask: at what point does the uncertainty actually change our decision? *(pause)* Let p be the probability of high government co-financing. We can write out the expected value for each strategy as a function of p. Setting Strategy B equal to Strategy C and solving, you get p equals 0.44. *(pause)* What does that mean? If you believe there's more than a 44% chance of high government co-financing, workforce-only becomes optimal — it has higher upside when the government cooperates. Below 44%, the split strategy's lower variance makes it the safer bet. *(pause)* And look at the green callout — here's the practical implication. The program should focus its advocacy efforts on securing government co-financing commitments. Why? Because that's what determines the optimal strategy. If you can move the probability above that threshold, you unlock a different and potentially better path.

## Slide: R Workshop: Decision Analysis
Let's move to R and implement all of this. Expected value, EVPI, and graph surgery — hands on.

## Slide: R: Expected Value Calculation
Alright, here we're implementing the three-strategy expected value computation in R. We define each strategy with its scenarios, probabilities, and lives saved, then use dplyr to group by strategy and compute the probability-weighted sum. Run this code and confirm what we calculated by hand — the split wins at 2,080.

## Slide: R: EVPI Calculation
Now we're computing EVPI — the value of learning government co-financing intentions before committing funds. The logic is: find the best decision in each scenario, compute the expected value of always making the right call, and subtract the expected value of the best single strategy. The difference is the maximum you'd pay for that information.

## Slide: R: Sensitivity Analysis Visualization
Here we're creating the sensitivity plot — expected lives saved on the y-axis, probability of high co-financing on the x-axis, with a line for each strategy. You'll see where the lines cross, which tells you the threshold where you'd switch strategies. The dashed line at 0.40 shows our current estimate.

## Slide: R: Graph Surgery with bnlearn
This is where it gets fun. We're implementing graph surgery in bnlearn by building two models — the original with confounding, and the intervened version where we've removed the arrow from Resources to CPAP. The key comparison is querying the same conditional probability in both models. The original gives you the confounded association; the modified one gives you the true causal effect.

## Slide: R: Tornado Diagram
And finally, the tornado diagram. This shows which parameters have the biggest impact on the split strategy's expected value. The wider the bar, the more that parameter matters. This tells you what to spend your research budget on — learn more about the variables with the widest bars, because those are the ones that could actually change your decision.

## Slide: Key Takeaways
Alright, let's bring it all together. Four essential lessons from today. *(pause)* First, influence diagrams extend our causal models with decisions and objectives — that's what makes them actionable. Second, expected value and EVPI give us principled tools for comparing options and putting a price tag on better information. Third — and this is the deep one — observing is not the same as intervening. The do-operator and graph surgery let us isolate true causal effects from confounded associations. And fourth, diversification — splitting your investment — often beats concentration when you're facing uncertainty. *(pause)* Together, these tools transform causal understanding into actionable investment decisions.

## Slide: Looking Ahead
Next time, we scale up. Instead of one country with three strategies, we're going to face multiple countries with uncertain co-financing, sequential pilot-then-scale decisions, and the real cost of delay measured in lives lost during the waiting period. The single-agent framework we built today becomes the workhorse for multi-country resource allocation. See you then.
