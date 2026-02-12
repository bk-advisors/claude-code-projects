# Speaker Notes — Chapter 5: Situational Analysis

## Overview
Alright, welcome to Chapter 5. This is where we put the Bayesian network engine into gear. Last chapter we learned how to build a model *forward* — specifying how causes produce effects. Today, we run the model *backwards*. We observe outcomes, like high neonatal mortality in a district, and use Bayes' rule to figure out what's most likely going wrong upstream. And the star of today's session is something called the "explaining away" effect — it's the most counterintuitive and practically important result in causal reasoning, and I promise it will surprise you.

## Slide: Learning Objectives
So here are our five objectives for today. We're going to start with the basics — computing marginal probabilities by summing out variables. Then we'll learn how to update beliefs when we get new evidence, using Bayes' rule. From there, we'll walk through inference in each of the three triplet structures — serial, diverging, and converging — and see how information flows differently in each one. The explaining away phenomenon gets special billing because, honestly, it surprises even experienced analysts when they first see it quantitatively. And then we'll tie it all together with a full district diagnosis — exactly the kind of thing you'd do if someone handed you DHIS2 data and said "Tell me why this district is underperforming."

## Slide: Chapter Overview
Take a look at the five-step flow on the slide. *(pause)* This mirrors the actual diagnostic workflow you'd follow in practice. First, establish your baseline expectations — those are the marginal probabilities. Then, observe some evidence and update your beliefs. Then understand how information flows through different causal structures. We give explaining away its own step because it's that counterintuitive. And finally, we put it all together in a real district diagnosis. Now look at the callout box at the bottom. This is the core insight: Chapter 4 went forward, from causes to effects. Chapter 5 reverses direction — from effects back to causes. That reversal is the heart of situational analysis.

## Slide: The Manager's Inference Problem
Okay, let's dive into the manager's inference problem — running the model backwards.

## Slide: From Forward to Backward Reasoning
This is the conceptual pivot of the first half of the course, so let me be really clear about what's changing. *(pause)* Look at the two boxes on the slide. On the left, Chapter 4's forward reasoning: "If staffing is low, what happens to NMR?" That's prediction. On the right, Chapter 5's backward reasoning: "We see high NMR — what does that tell us about staffing?" That's diagnosis. *(pause)* And here's what's beautiful about this — both directions use the exact same Bayesian network. Same model, same numbers, just different questions. Every program analyst who pulls up DHIS2 data and tries to figure out *why* a district is struggling — they're doing backward reasoning, whether they know it or not. What we're doing today is making that reasoning rigorous.

## Slide: The MNH Inference Model
Here's the simplified model we'll use throughout this chapter. Staffing and Equipment both feed into Workforce Quality, and Quality feeds into NMR. We'll add Training later when we get to the full diagnosis. *(pause)* Look at the prior probabilities in the table: 40% of facilities have adequate staffing, 35% have equipment available, 50% have completed training. These come from Chapter 4 — they represent our baseline beliefs before we see any district-specific evidence. Think of them as the starting point. What we're about to learn is how to move *away* from these starting points when data comes in.

## Slide: Marginal Probabilities
Now let's talk about marginal probabilities — what's the overall probability of an outcome when we don't know anything yet?

## Slide: What Is a Marginal Probability?
So what *is* a marginal probability? It's what you believe when you have zero evidence. None. *(pause)* If I asked you, "What's the probability that a randomly selected district has high NMR?" — you don't know the district's staffing situation, you don't know about their equipment. So you average over *all possible* staffing and equipment combinations, weighted by how likely each one is. That's it. It's just weighted averaging. The formula on the slide shows you the math — you sum out all the other variables from the joint distribution — but the intuition is really that simple: it's your default expectation before any data comes in.

## Slide: Computing Marginal NMR
Alright, here are the CPTs we'll use for every calculation in this chapter, so get comfortable with these tables. *(pause)* The Quality CPT on top shows how Staffing and Equipment interact. When both are favorable — adequate staffing and available equipment — there's a 90% chance of good quality. When both are unfavorable, that drops all the way to 15%. That's a huge range. *(pause)* The NMR CPT below maps quality to mortality: 15% chance of high NMR with good quality, 70% chance with poor quality. We're going to be coming back to these tables again and again, so take a moment to really absorb the numbers.

## Slide: Marginal P(NMR=High): The Calculation
Okay, let's walk through this step by step. We need to sum over all four Staffing-times-Equipment combinations, weighting each by how likely that combination is. *(pause)* Look at the table. Each row is one combination. The first row — adequate staffing, available equipment — contributes just 0.029 to the total. The last row — low staffing, unavailable equipment — contributes 0.240. That's by far the biggest chunk, because that combination is both common *and* bad for outcomes. *(pause)* Add them all up and you get P(NMR=High) = 0.455 — a 45.5% baseline probability. That's our anchor number. Every time we observe evidence from here on, we'll ask: does this push the probability up or down from 45.5%?

## Slide: Evidence and Updating
Now here's where it gets interesting. How do observations change our beliefs?

## Slide: What Does "Evidence" Mean?
So what do we mean by "evidence" in this context? It just means learning the actual state of a variable. In probability language, we call this "conditioning." *(pause)* Look at the two boxes on the slide. On the left, before any evidence, P(Staffing=Low) = 0.60. That's just our general prior — what we believe across all districts. Now on the right — we observe that NMR is High in a specific district. The question becomes: P(Staffing=Low *given* NMR=High) = ... what? *(pause)* That's a backward inference. We're using a child node's value to update our beliefs about a parent. And this is exactly the situational assessment task that every program manager faces. You see a bad outcome, and you want to know what's causing it.

## Slide: Bayes' Rule: The Engine of Updating
Here's the core computation, so follow along carefully. *(pause)* We need P(NMR=High given Staffing=Low) in the numerator — that requires marginalizing over Equipment and Quality. The calculation gives us 0.549. Then we divide by P(NMR=High), which is our 0.455 from earlier. *(pause)* And the result? P(Staffing=Low given NMR=High) = 0.724. Let that sink in. *(pause)* Observing high mortality shifts our belief about low staffing from 60% all the way to 72.4%. That's a 12.4 percentage point increase. High NMR is telling us that staffing is probably inadequate. The evidence is speaking.

## Slide: The General Pattern of Updating
Now look at this table — this is where the diagnostic payoff really shows up. After observing high NMR, *all* the root causes shift toward their "bad" states. But — and this is the important part — they don't shift equally. *(pause)* Staffing moves the most, 12.4 percentage points. Equipment is next at 9.1. So if you're the program analyst, and you can only investigate one thing first, where do you look? Staffing. It's the variable with the strongest signal. *(pause)* Look at the green callout at the bottom. The variable with the largest posterior shift has the strongest causal connection to the observed outcome in this model. That tells you where to start your investigation.

## Slide: Inference in Serial Structures
Okay, let's shift gears. Now we're going to examine each of the three triplet structures quantitatively, starting with chains.

## Slide: Serial Structure: The Chain
The chain is Training to Competency to Mortality. *(pause)* Here's the key idea: if you observe high mortality and you *don't* know competency, you can infer something about training — it probably wasn't completed. Information flows the whole length of the chain. But once you *know* competency directly — say you tested the health workers — training becomes irrelevant for predicting mortality. Why? Because everything training does, it does *through* competency. If you already know competency, training has nothing left to tell you. The chain gets blocked.

## Slide: Serial: CPTs and Priors
Here are the CPTs for our serial chain. Training completion gives an 80% chance of high competency, versus only 30% without training. And high competency gives an 85% chance of low mortality, compared to just 35% with low competency. *(pause)* The marginal probability of high competency works out to 0.55. Take a moment to verify that calculation — 0.50 times 0.80 plus 0.50 times 0.30. Building that kind of fluency with the arithmetic will pay off as the calculations get more involved.

## Slide: Serial: Worked Bayesian Calculation
Let's work through the full calculation: what's P(Training=Completed given Mortality=High)? *(pause)* Step 1: we need the marginal P(Mortality=High). That's 0.55 times 0.15 plus 0.45 times 0.65, which gives us 0.375. Step 2: P(Mortality=High given Training=Completed) = 0.80 times 0.15 plus 0.20 times 0.65 = 0.250. Step 3: plug into Bayes' rule — 0.250 times 0.50 divided by 0.375 = 0.333. *(pause)* So high mortality shifts our belief about training completion from 50% *down* to 33.3%. High mortality is evidence *against* training having been completed. That makes intuitive sense, right? If mortality is high, the most likely explanation is that the training pathway broke down somewhere.

## Slide: Serial: Blocking by Conditioning
Now here's the blocking test. Suppose we also know that Competency is Low. Does training still tell us anything about mortality? *(pause)* No. Look at the equation: P(Training=Completed given Mortality=High AND Competency=Low) just equals P(Training=Completed given Competency=Low). Mortality drops out of the picture entirely. *(pause)* And that number is 0.222. Once we know competency, mortality becomes irrelevant for assessing training. That's the chain being blocked in action. The practical takeaway here is important: if you can directly measure competency — say through skills assessments — you don't need mortality data to evaluate whether training worked. The direct measurement is more informative than the indirect signal.

## Slide: Inference in Diverging Structures
Now let's look at the fork — a common cause driving two effects.

## Slide: Diverging Structure: The Fork
The fork here is PPH Detection and CPAP Usage, both driven by Workforce Quality. *(pause)* Here's what this means in practice. Competent staff are good at detecting PPH *and* good at using CPAP. So if you look at data across districts, you'll see a correlation — districts that are good at one tend to be good at the other. But is that a causal relationship? Can you improve CPAP usage by training people on PPH detection? No. The correlation exists because workforce quality drives *both*. Fix the common cause — invest in workforce quality — and both improve. But improving one effect won't fix the other.

## Slide: Diverging: CPTs and Setup
The CPTs make this concrete. Good workforce quality gives a 90% chance of good PPH detection and 85% chance of proper CPAP usage. Poor quality drops those to 35% and 25%. *(pause)* The marginals are P(PPH=Good) = 0.598 and P(CPAP=Proper) = 0.520. Those are our baselines — what we expect before any evidence. Now let's see what happens when evidence comes in.

## Slide: Diverging: Inference from One Child to Another
Okay, here's the fork in action. We observe poor PPH detection in a district, and we ask: what does this tell us about CPAP usage? *(pause)* Step 1: update our belief about Quality given PPH=Poor. P(Quality=Good) drops from 45% down to just 11.2%. That's a dramatic shift — poor PPH detection is very strong evidence of poor workforce quality. Step 2: use that updated belief about Quality to predict CPAP. P(CPAP=Proper) drops from 52.0% to 31.7%. *(pause)* So information flowed from one effect to another *through* the common cause — even though there's no direct causal link between PPH detection and CPAP usage. This is confounding in action. The correlation is real, but it's not causal.

## Slide: Diverging: Blocking by Conditioning on Common Cause
But what if we know Quality directly? Say we've done workforce assessments and we know this district has Good quality. Does poor PPH detection still tell us anything about CPAP? *(pause)* Not a thing. P(CPAP=Proper given PPH=Poor AND Quality=Good) = P(CPAP=Proper given Quality=Good) = 0.85. The fork is blocked. *(pause)* Look at the green callout — this has a real management implication. If you can directly measure workforce quality, you don't need to infer it from proxy indicators like PPH detection rates or CPAP usage. Direct measurement gives you sharper diagnoses. It cuts through the noise of the indirect signals.

## Slide: Inference in Converging Structures
Now here's the one I've been building up to. The converging structure — the collider. This is where things get counterintuitive.

## Slide: Converging Structure: The Collider
Staffing and Equipment both feed into Quality. That makes Quality a collider — a common effect of two causes. *(pause)* Here's what's different from everything we've seen so far. Staffing and Equipment are *independent*. They're separate investment decisions — knowing how many staff a facility has tells you nothing about whether they have the right equipment. But — and this is the counterintuitive part — once we observe their common effect, Quality, they become dependent. *(pause)* This is the *opposite* of what happens with chains and forks. In those structures, conditioning on the middle node *blocks* information flow. In a collider, conditioning on the middle node *opens* a path that wasn't there before.

## Slide: Explaining Away: The Core Idea
Let me walk you through the scenario that makes this click. *(pause)* Imagine you observe good workforce quality in a district. That's a pleasant surprise. Could be because staffing is adequate, could be because equipment is available, could be both. Now — you learn that staffing is actually Low. What happens to your belief about equipment? *(pause)* Think about it. Quality is good. But staffing can't be the reason, because staffing is low. So *something else* has to explain the good quality. Equipment must be available — because it's the only remaining explanation. Equipment "explains away" what staffing cannot. *(pause)* This is exactly how diagnostic reasoning works in practice. You rule out one cause, and that strengthens your belief in the other. Doctors do this all the time. Now we have the math to make it precise.

## Slide: Converging: Worked Calculation
Let's walk through the math. *(pause)* First, we observe Quality=Good. What does that do to our belief about Equipment? P(Equipment=Available) rises from the prior of 35% to 51.8%. Good quality is consistent with good equipment, so our belief goes up. *(pause)* Now we add the observation that Staffing=Low. Watch what happens — P(Equipment=Available) jumps to 64.2%. Equipment must be compensating for the staffing deficit. *(pause)* Look at the three-row table at the bottom. Prior: 35%. After seeing good quality: 51.8%. After also learning staffing is low: 64.2%. Each piece of evidence pushes our belief further. That's explaining away in action — you can *see* the progressive shift in the numbers.

## Slide: Converging: The Explaining Away Effect
This table is the key takeaway from the whole triplet structures discussion. *(pause)* Notice the explaining away effect: once we know quality is good, learning that staffing is low actually *increases* our belief in equipment availability. In chains and forks, conditioning on the middle node *blocks* the path — the two outer variables become independent. In colliders, conditioning on the middle node *opens* the path — the two outer variables become *dependent*. *(pause)* This asymmetry — chains and forks block, colliders activate — is the single most important distinction you need to internalize from this chapter. It comes up over and over in real-world diagnosis.

## Slide: MNH Application: District Diagnosis
Okay, now we put all of this together in a complete worked example with realistic data.

## Slide: The Diagnostic Scenario
Here's the situation. District Mwanga reports an NMR of 35 per 1,000 live births — well above the national average. The country director calls you up and asks: "What is most likely going wrong?" *(pause)* What do we have to work with? We know NMR is High. That's it. We have no direct observations of staffing, equipment, training, or quality. All we have is the NMR number and our national-level causal model with CPTs. *(pause)* Our task: use Bayesian inference to update our beliefs about *every* upstream variable, identify the most likely root cause, and tell the country director where to investigate first.

## Slide: Step 1: Establish the Full Model
First, we expand our model. We add Training as a third root node, giving us a five-node Bayesian network. *(pause)* Look at the extended Quality CPT — it now has 8 rows, one for every combination of the three parent variables. The best-case scenario, where all three parents are favorable, gives 95% good quality. The worst case — everything unfavorable — gives just 8%. That's an enormous range, and it shows how dramatically the parent configuration matters. The model is capturing real interactions between these inputs.

## Slide: Step 2: Compute Posterior Probabilities
Here are the diagnostic results. *(pause)* After observing NMR=High, all three root causes shift toward their "bad" states. Staffing shifts the most — up 11.0 percentage points from 60% to 71%. Equipment is next at 8.8 points. Training shifts the least at 7.3 points. *(pause)* So what does this tell the country director? Staffing is the variable most likely to be in a bad state. Look at the orange callout — staffing should be the first thing to check. That doesn't mean equipment and training are fine. It means if you can only send one assessment team, send them to look at staffing first.

## Slide: Step 3: Identify the Most Likely Configuration
But we can go further. Which *specific combination* of root causes is most probable? *(pause)* Look at the rankings. The most likely diagnosis is all three in their bad state — low staffing, unavailable equipment, training not completed — with a posterior probability of 28.4%. That's 2.8 times more likely than the next-best configuration. *(pause)* In plain language: if NMR is high, the single most probable explanation is that everything is going wrong simultaneously. And that actually makes sense when you think about it — each bad state compounds the others. Low staffing makes it harder to use equipment effectively, which makes training less impactful, and so on. Problems cluster.

## Slide: Step 4: Compare with a "Healthy" District
Now this comparison is really powerful. *(pause)* District Songea reports NMR=Low. Look at the side-by-side table. In Songea, all the root causes shift toward their *good* states — it's the mirror image of the struggling district. *(pause)* The country director can now see both pictures at once. On the left in red, District Mwanga — what's going wrong, with staffing as the strongest signal. On the right in green, District Songea — what's going right, with equipment showing the most improvement from the prior. *(pause)* And here's the elegant part — it's the same framework doing both jobs. The same model that diagnoses problems also identifies what's working well. Both directions inform resource allocation. You can learn from your successes just as much as from your failures.

## Slide: R Code Workshop
Alright, let's get our hands dirty with some code. We're going to build all of this in R using bnlearn.

## Slide: R Block 1: Build a BN with CPTs
In this first block, we're defining the full five-node Bayesian network with all the CPTs specified as arrays. Walk through the code with me — we define the DAG structure, then set up the CPT for each node. Pay attention to how the Quality CPT is structured as a multidimensional array. That's the trickiest part to get right, but once you see the pattern, it's straightforward.

## Slide: R Block 2: Query with Evidence
Now we're running actual queries against the network. First, the marginal P(NMR=High) with no evidence — you should get approximately 0.455, matching our hand calculation. Then the posterior with evidence: P(Staffing=Low given NMR=High) should come out around 0.71. And then we layer on multiple pieces of evidence to see how beliefs change as more information comes in. Try changing the evidence and watch the numbers move.

## Slide: R Block 3: Compare Posterior vs. Prior
Here we write a function that computes posteriors for all root nodes given any NMR evidence. Then we use it to compare District Mwanga — NMR=High — with District Songea — NMR=Low. The shift column tells you everything: positive shifts mean the bad state became more likely, negative shifts mean the good state became more likely. This is the computational version of the side-by-side comparison we did on paper.

## Slide: R Block 4: Visualize Belief Updating
Now let's make the belief shifts visual. We're creating a grouped bar chart with prior probabilities next to posterior probabilities for each root node. When you see the bars side by side, the pattern becomes obvious — every bad state gets more probable after observing high NMR, with staffing showing the biggest jump. This is the kind of visualization you'd put in a report for a country director.

## Slide: R Block 5: Full District Diagnosis Workflow
And this last block ties everything together into a reusable diagnosis function. You pass in any set of evidence — maybe just NMR=High, or maybe NMR=High and Quality=Poor — and it returns a prioritized list of root causes ranked by the size of their posterior shift. This is a tool you could actually use in practice. Change the evidence, run it again, and see how the diagnosis changes.

## Slide: Key Takeaways
Alright, let's wrap up with four things I want you to take away from today. *(pause)* First, marginal probabilities give you baseline expectations. Our 45.5% is the starting point before any evidence. Second, Bayes' rule updates those beliefs when evidence arrives — and in our model, staffing showed the largest shift, making it the first place to investigate. Third, the three structures determine how information flows: chains and forks get *blocked* by conditioning on the middle node, while colliders get *activated*. And fourth — explaining away. When two independent causes compete to explain a common effect, confirming one *reduces* your belief in the other. That pattern is everywhere in diagnostic reasoning, and now you have the math to handle it.

## Slide: Looking Ahead
Next time we're tackling two dangerous analytical pitfalls that trip up even experienced analysts. *(pause)* Simpson's Paradox — where aggregated data literally reverses the true causal effect — and the Prosecutor's Fallacy, where people confuse P(Evidence given Hypothesis) with P(Hypothesis given Evidence). Both of these are directly relevant to how the MNH program evaluates its country portfolios and makes resource allocation decisions. See you next time.
