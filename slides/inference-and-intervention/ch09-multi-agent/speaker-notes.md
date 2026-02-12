# Speaker Notes — Chapter 9: Multi-Agent Interventions

## Overview
Alright, this is the chapter where we confront something we've been quietly ignoring. Up to now, we've treated the world as passive — nature rolls the dice, and we optimize against it. But governments aren't dice. Other donors aren't dice. Implementing partners aren't dice. They're all watching what we do, and they're adjusting their behavior based on our choices. Today, game theory gives us the formal tools to deal with that reality — and by the end, you'll see how the right contract design can take you from 500 lives saved to 4,500 without spending a single extra dollar.

## Slide: Learning Objectives
So here are our five objectives for today, and they build on each other in a very deliberate sequence. First, we need the vocabulary — defining games with players, strategies, and payoffs. Then the core analytical skill: finding Nash equilibria. From there we add timing with sequential games and backward induction. We connect it all back to the DAGs you already know through causal-form games. And the capstone is the MNH donor-government interaction, where we'll see that getting the contract design right matters just as much as getting the allocation right.

## Slide: Chapter Overview
Here's our roadmap. *(pause)* Five stops today. We start with game theory foundations — players, strategies, payoffs. Then we move to Nash equilibrium, which is really the central idea of this whole chapter. From there, extensive form games add timing and sequence. The causal form connects everything back to the influence diagrams you already know. And we finish with the workforce absorption game, which ties it all together in one complete application.

Now look at that callout at the bottom. *(pause)* This is the key shift. In Chapter 7, it was one decision-maker against nature. In Chapter 8, we optimized how to allocate resources. Now? Other agents are acting strategically. They're watching us, and they're making their own moves. That's why we need game theory.

## Slide: The Single-Agent Assumption Breaks Down
Look at these two columns. On the left, that's the world we've been living in for the last two chapters. The donor chooses an intervention, nature rolls the dice, we compute expected value and optimize. Nice and tidy. The implicit assumption? Other actors are just part of the environment — they don't respond to what we do.

Now look at the right column. *(pause)* This is reality. The donor commits high funding, and the government *observes* that and thinks, "Great, they're paying for it — I can redirect my budget elsewhere." Implementing partners see how intensely we're monitoring and adjust their effort accordingly. The environment is not passive. Other agents are optimizing their own payoffs in response to our choices.

And that red callout drives the point home with a specific example. When a donor increases salary support for health workers, what do some governments do? They *decrease* their own budget allocation for the same line item. If you ignore that strategic response, you're going to overestimate your program's impact — potentially by a lot.

## Slide: Strategic Actors in MNH
So who are these strategic actors? In a typical MNH program, you've got at least four. *(pause)* Look at this table. The donor organization wants to maximize lives saved per dollar. The national government is trying to balance health outcomes against fiscal constraints — they've got a whole budget to manage, not just the health line. Implementing partners need to deliver results but also sustain their own operations. And other donors? They're maximizing their own impact metrics, which may or may not align with yours.

Each of these agents is making decisions while thinking about what the others will do. That's what makes this a game, not just an optimization problem. And the green callout at the bottom is the promise of this chapter: game theory gives us formal tools to predict what everyone will do and to design contracts that make everyone's incentives line up.

## Slide: The Three Elements of a Game
Every game — and I mean every game, from poker to international diplomacy to MNH funding — has exactly three elements. Players, strategies, and payoffs.

In our MNH context: the players are the donor and the government. Their strategies are the funding and co-financing levels they can choose. And the payoffs blend lives saved with cost burdens and political capital.

Now, look at that callout about rationality. *(pause)* This is important. Rational doesn't mean selfish. It means each player chooses what maximizes *their own* payoff — but those payoffs can absolutely include altruistic goals. A government that genuinely cares about health outcomes is still rational; it just has different payoffs than a government focused purely on fiscal savings. Rationality is about consistency of choice, not about what you care about.

## Slide: Normal Form: The Payoff Matrix
Okay, the payoff matrix. This is the simplest way to represent a game. Rows are one player's strategies, columns are the other's, and each cell shows both players' payoffs.

Here's our co-financing game. *(pause)* Look at the top-left cell: when the donor funds high and the government co-finances high, we get 2,400 lives saved but at high cost to the government. Bottom-right: both go low, only 800 lives, moderate cost. The tension is already visible — the best collective outcome is top-left, but each player might be tempted to go elsewhere.

One thing to practice: reading each cell as a pair. The first number is always the donor's payoff, the second is the government's. Get comfortable with that convention — you'll be reading a lot of these today.

## Slide: Payoffs Capture Competing Priorities
Now let's get more precise about these payoffs by assigning actual utility scores. The donor's utility is straightforward — lives saved. The government's utility is lives saved minus a fiscal cost penalty. They care about outcomes, but they also feel the pain of spending.

Work through the math with me. Top-left cell: the donor gets 2,400 from lives saved. The government gets 2,400 lives minus 50 times 30 million in costs, which gives 900. *(pause)*

But here's the thing — look at the orange callout. Notice that the government gets the same utility, 900, whether it co-finances high or low when the donor funds high. And 550 either way when the donor funds low. That can't be right in the real world. The numbers depend entirely on our cost-sharing assumptions, and these simplified ones are too crude. We need to refine this.

## Slide: Refined Payoff Matrix
Here's a more realistic version where the government actually bears different costs depending on what it chooses. *(pause)*

Now this is getting interesting. Look at the green callout — it walks you through the interpretation. The best collective outcome is still top-left: high funding plus high co-financing gives us 2,400 plus 1,200 equals 3,600 total utility. The government actually prefers high co-financing when the donor funds high — 1,200 beats 1,100. And the donor always prefers high funding.

But here's the question that sets up everything that follows: what happens when the government starts to suspect the donor will fund high no matter what? *(pause)* Keep that question in mind.

## Slide: Dominant Strategies
A dominant strategy is one that's best for you regardless of what the other player does. That's a powerful concept — it means you don't even need to know what the other side is thinking.

Let's check systematically. The donor: if the government plays high, the donor prefers high funding — 2,400 beats 1,800. If the government plays low, the donor still prefers high — 1,400 beats 800. So high funding dominates for the donor no matter what.

Now the government: if the donor funds high, the government prefers high co-financing — 1,200 beats 1,100. If the donor funds low, the government still prefers high — 800 beats 600. High co-financing dominates for the government.

*(pause)* So both players have dominant strategies, and they point in the same direction. The outcome — high funding, high co-financing — is what we call a dominant-strategy equilibrium. This is the best-case scenario, where everyone's individual incentives happen to align with the collective good. Enjoy this moment, because it's about to get more complicated.

## Slide: Nash Equilibrium
Alright, Nash Equilibrium — this is the central concept of game theory. *(pause)* A strategy profile is a Nash equilibrium when no player can improve their payoff by unilaterally changing their strategy. Everyone is doing the best they can, given what everyone else is doing.

Here's the practical procedure for finding it — the underline method. For each column, underline the row player's best response. For each row, underline the column player's best response. Any cell where both payoffs are underlined? That's your Nash equilibrium.

Look at the matrix. The donor's 2,400 is underlined in the first column, and 1,400 in the second — those are best responses. The government's 1,200 is underlined in the first row, and 800 in the second. The top-left cell has both underlined, so high funding, high co-financing is our unique Nash equilibrium. Practice this method — you'll use it again and again.

## Slide: When Incentives Misalign: A Harder Game
Now here's where it gets real. *(pause)* Suppose the government faces high political costs for co-financing. Maybe they're diverting funds from visible infrastructure projects that voters care about. The payoffs shift.

Look at the new matrix. Check the government's best responses now. If the donor funds high: low co-financing gives 1,100, high gives only 700. Low wins. If the donor funds low: low co-financing gives 600, high gives 500. Low wins again.

Low co-financing now dominates for the government. The Nash equilibrium shifts to high funding, low co-financing — the donor pours in money, the government free-rides. Total utility drops from 3,100 to 2,500. *(pause)* This is the realistic scenario. This is why we need game theory — because when political costs are high, good intentions alone don't produce good outcomes.

## Slide: The Prisoner's Dilemma in Health Funding
Let me show you why this pattern looks familiar. On the left, the classic Prisoner's Dilemma — you've probably seen this before. Both players would prefer to cooperate, but each has an individual incentive to defect. They end up at defect-defect, worse off than if they'd both cooperated.

Now look at the right — our MNH version. *(pause)* The structure is similar but not identical. Both would prefer mutual cooperation, but the government's incentive pushes toward free-riding. The difference here is that the donor's dominant strategy keeps funding flowing regardless, so we end up at fund-and-free-ride rather than mutual defection.

The green callout identifies the way out: commitment devices. Contracts, conditionalities, repeated interaction over time. Without those mechanisms, you're stuck in the bad equilibrium. The structure of the game is working against you.

## Slide: Multiple Equilibria and Coordination
Here's a different kind of problem. Some games don't have one equilibrium — they have two, and that creates its own headache.

Look at this workforce cadre game. If both the donor and government invest in midwives, that's a Nash equilibrium — neither wants to deviate. If both invest in community health workers, that's also an equilibrium. But look at the off-diagonal cells: if one invests in midwives and the other in CHWs, the payoffs are terrible for both — 400 and 300, or 300 and 400. Total waste.

*(pause)* Here's the thing — both players actually prefer the midwives equilibrium. It's Pareto superior. But without communication, without coordination, they might end up miscoordinated. The donor trains midwives while the government hires community health workers, and both investments are largely wasted.

The takeaway is that coordination games explain why joint planning between donors and governments is essential. The problem isn't conflicting interests — they actually agree on what's best. The problem is making sure both sides invest in the *same* thing.

## Slide: Escaping Bad Equilibria
So how do you actually escape a free-riding equilibrium? Four approaches from mechanism design.

First, conditional funding. "We fund high only if you co-finance at least 30%." That directly changes the payoffs. Second, repeated interaction — when you're funding over multiple cycles, there's a reputation to build and maintain. Third, binding contracts with milestone-triggered disbursements. And fourth, third-party enforcement — bringing in the World Bank or Global Fund with their own conditionalities.

Look at the MNH example on the right. *(pause)* A co-financing escalator: the government's contribution must increase by five percentage points per year. Miss a milestone, and the next tranche gets cut by 50%. That changes the whole game — free-riding now costs you future funding. This is exactly how real program agreements are structured.

## Slide: Extensive Form Games
Okay, let's move to a different way of representing games. *(pause)* So far we've been using matrices — everything happens simultaneously. But in reality, moves happen in sequence. The donor announces its funding commitment, and *then* the government decides on co-financing.

Look at this game tree. The donor moves first — high or low. The government observes that choice and then responds. At the end of each branch, we see the payoffs for both players.

Why does this matter? Because the sequential structure changes the strategic logic. When the government can *see* what the donor has done before it responds, that gives the government information — and strategic leverage. This is exactly what happens in practice when funding commitments are announced before government budget cycles.

## Slide: Backward Induction
This is the algorithm for solving sequential games, and it's beautifully simple. You start at the end and work backward.

Step 1: What does the government do? If the donor chose high funding, the government picks low co-financing — 1,100 beats 700. If the donor chose low funding, the government still picks low — 600 beats 500. So no matter what the donor does, the government free-rides.

Step 2: The donor *knows* this. So it anticipates the government's response and asks, "Given that the government will free-ride either way, am I better off funding high or low?" High gives 1,400, low gives 800. The donor funds high.

*(pause)* The outcome: high funding, low co-financing, payoffs 1,400 and 1,100. The donor funds generously *knowing* the government will free-ride — because even with free-riding, high funding is better than the alternative. That's a depressing but realistic result.

## Slide: First-Mover Advantage in Donor Commitments
But here's where it gets interesting. The order of moves doesn't just describe the game — it changes what's possible. *(pause)*

When the donor commits first without conditions, the government observes and free-rides. We just saw that. But what if the donor can commit *conditionally*? "I'll fund high if and only if you co-finance at least 30%."

Look at the flow diagram. The donor announces the condition, then the government chooses. Now the government faces a real choice: co-finance high and get high donor funding, payoff 700. Or don't co-finance and get low donor funding, payoff 600. Seven hundred beats 600, so the government cooperates.

*(pause)* Conditionality restores cooperation. By credibly restricting its own future choices — "I'm tying my own hands here" — the donor can induce better behavior. This is the logic behind every milestone-based disbursement you'll ever see.

## Slide: Subgame Perfect Equilibrium
Subgame perfect equilibrium refines Nash equilibrium for sequential games. The idea is that the strategies have to be optimal not just overall, but in *every subgame* — every possible branch of the tree.

Look at the two columns. Without conditionality, the subgame perfect equilibrium is high funding, always low co-financing. The government's strategy of always free-riding is credible because it's genuinely optimal at every decision point.

With conditionality, the equilibrium shifts to conditional high funding, high co-financing. Now cooperating is the government's best response in the relevant subgame because low co-financing triggers reduced funding.

*(pause)* But look at that orange callout — this is crucial. Non-credible threats don't work. If everyone knows the donor would never actually withdraw funding — maybe there's political pressure, maybe there's a sunk-cost mentality — then the conditionality has no bite. The government calls the bluff and free-rides anyway. Credibility is everything in this game.

## Slide: Games as Causal Models
Now let's connect game theory back to everything you've learned in this course. *(pause)* The causal-form game represents a game as a multi-agent influence diagram. Each player has their own decision node and their own objective node, and the causal structure shows how those decisions interact through shared outcomes.

Look at this diagram. Donor funding and government co-financing both flow into health outcomes. But each player evaluates those outcomes through their own utility function — the donor cares about lives saved, the government weighs lives against fiscal cost.

The advantage of this representation? It makes the causal *pathways* explicit. We can see *why* the payoffs have the values they do, not just what the values are. And we can add chance nodes — disease burden, political stability — just like we did in Chapters 7 and 8.

## Slide: Converting Between Game Representations
So now we have three ways to represent the same game, and each one is good for something different.

The normal form — that's our matrix — is best for finding Nash equilibria in small games. You can see all the strategy combinations at once and use the underline method. The extensive form — the tree — is best when timing matters. Who moves first? Can they observe the other player's choice? Can they commit? The causal form — the DAG — is best for understanding *why* payoffs have their values.

Look at the MNH example at the bottom. *(pause)* In the matrix, we see that high funding plus low co-financing gives a payoff of 1,400 for the donor. The causal form tells us *why*: high funding increases equipment and training, but low co-financing means inadequate staffing for sustainability. The 1,400 lives reflects a short-term gain that will erode without government support. Same number, but now you understand the mechanism.

## Slide: Adding Chance Nodes
The causal form also naturally incorporates uncertainty — and this is where game theory meets the decision analysis from Chapters 7 and 8.

Look at this expanded diagram. We've got the donor's funding decision, the government's co-financing decision, and now a chance node in the middle: political stability. Neither player controls it, but it affects everything downstream. If instability is high, even mutual cooperation may yield poor outcomes.

*(pause)* This is the bridge. In Chapter 7, we computed expected payoffs under uncertainty with a single decision-maker. Now we do exactly the same thing, but with multiple strategic decision-makers. Same math, richer framework.

## Slide: Strategy Tables
Now here's where we need to be very precise about what we mean by a "strategy." *(pause)*

In extensive form, a strategy isn't just a single action — it's a *complete plan* specifying what you'll do at every decision point you might reach. The government has two information sets: what to do if the donor funds high, and what to do if the donor funds low. With two choices at each, that's two-to-the-two equals four possible strategies.

Look at the table. Always High — cooperate no matter what. Always Low — free-ride no matter what. Match — cooperate if and only if the donor cooperates. And Oppose — do the opposite of whatever the donor does.

The "Match" strategy is particularly interesting. It's basically tit-for-tat: "I'll cooperate if you do." That contingent behavior is what makes conditional agreements possible. The strategy table makes the full landscape of possible plans explicit.

## Slide: Conditional Funding Agreements
Here's how contingent strategies look in practice. *(pause)* The donor's conditional strategy: "I fund high IF the government co-finances at least 30% of recurrent costs AND absorbs at least 80% of trained workers by year 3."

Look at the donor's strategy table. Unconditional high — fund no matter what. Conditional high — fund if the government cooperates, pull back if not. Conditional low — the opposite, which doesn't make much sense. And unconditional low — never fund.

The green callout identifies the winner: conditional high is the dominant strategy when the donor can credibly commit. It rewards government cooperation and punishes free-riding. This is exactly the structure of milestone-based payment agreements. And it works — but only if the commitment is credible.

## Slide: Milestone-Based Payments as Commitment
Here's what conditional strategies look like when they become actual contracts. *(pause)*

Look at this milestone table. 25% of the tranche is released when the government creates a budget line for health workers — that's verified by an audited budget document. Another 25% when 200 workers are on the government payroll by year one. Another 25% when 400 are absorbed by year two. And the final 25% when full absorption hits 500 by year three.

Each milestone is observable, verifiable, and tied to a specific funding release. That's the operationalization of a contingent strategy.

But the orange callout raises the fundamental question. *(pause)* Milestones only work if the donor *actually* withholds funding when they're missed. If the government believes the donor will disburse regardless — because of political pressure, or sunk-cost thinking, or just because cutting off funding feels cruel — then the conditionality is empty words. Credibility is the foundation of all of this.

## Slide: The Setting
Alright, now we bring everything together in one complete game-theoretic analysis. *(pause)* This is the workforce absorption game, and it's the capstone of the chapter.

Here's the setup. A large MNH program trains 500 community health workers with a substantial multi-year investment. The government has to absorb these workers onto its own payroll within three years. If it doesn't, workers leave for the private sector or emigrate, and the entire investment is wasted.

Both players know the stakes. Both act strategically. The donor chooses its funding level — full or reduced. The government chooses its absorption level — full, partial, or none. This captures a challenge that every large-scale health workforce program faces. Let's see how it plays out.

## Slide: The Payoff Matrix
Here's the payoff matrix — a 2-by-3 game this time, six possible outcomes. *(pause)*

The donor's payoffs reflect lives saved over ten years. At the best outcome — full funding, full absorption — that's 4,500 lives. At the worst — full funding, no absorption — just 500. An enormous investment essentially wasted.

Now look at the government's side. And this is where the problem lives. The government's *highest* utility comes from no absorption — 1,000 when the donor funds fully. Why? Because no absorption means avoiding the recurring expense of putting hundreds of workers on the government payroll. The government still gets the benefit of trained workers during the donor-funded period, but it doesn't have to pick up the tab afterward.

*(pause)* That misalignment right there — the government's best outcome is the donor's worst — is the root of the entire problem.

## Slide: Finding the Nash Equilibrium
Let's use the underline method and see what happens. *(pause)*

Government's best responses: if the donor funds fully, no absorption gives 1,000, which beats partial at 900 and full absorption at 600. If the donor reduces, no absorption gives 800, which beats partial at 700 and full at 400. No absorption dominates for the government.

Donor's best responses: regardless of what the government does — full absorb, partial, or none — full funding always beats reduced. 4,500 beats 2,200. 2,800 beats 1,500. 500 beats 300.

*(pause)* So the Nash equilibrium is full funding, no absorption. Payoffs: 500 for the donor, 1,000 for the government. The donor makes a substantial investment in training 500 workers, deploys them, and then the government doesn't absorb a single one. A classic free-rider tragedy. And this isn't a theoretical curiosity — this happens in real programs when contracts aren't structured properly.

## Slide: Redesigning the Game: Commitment Devices
But here's the good news. The donor can change this outcome through contract design. *(pause)*

Device 1: milestone payments. Restructure the disbursement so that the government only gets the full package if it hits absorption targets. 20% upfront, then 25% at each milestone. If the government doesn't absorb, it gets only the initial-phase training — payoff drops from 1,000 to 350. That's a massive hit.

Device 2: a bonding agreement. The government puts funds in escrow, forfeited if targets are missed. That directly penalizes non-absorption.

Device 3: combine both. With milestone payments and a bonding agreement together, full absorption becomes the dominant strategy for the government. *(pause)* This is mechanism design in action — you're not changing what anyone wants; you're changing the rules of the game so that the rational choice aligns with the socially optimal outcome.

## Slide: The Transformed Game
Look at the new payoff matrix with milestone payments in place. *(pause)*

Under conditional funding, the government now prefers full absorption at 600, over partial at 500, over no absorption at 350. The ranking has flipped. Full absorption is now the government's best response to conditional funding.

The new Nash equilibrium: conditional funding, full absorption. Donor payoff: 4,500. Government payoff: 600.

*(pause)* Let that number sink in. The donor went from 500 lives saved to 4,500 lives saved. A nine-times improvement. Not by spending more money — same budget. Just by restructuring the incentives. Same resources, radically different outcomes. That is the power of game theory applied to program design.

## Slide: Lessons from the Absorption Game
Five principles to take away from this analysis. *(pause)*

One: map the game first. Before you commit a single dollar, identify the players, their strategies, and their payoffs. Two: check for dominant strategies. If free-riding dominates, unconditional funding will fail — guaranteed. Three: design for subgame perfection. Your conditionalities have to be credible. If you'd never actually withhold funding, everyone knows it, and the game doesn't change. Four: use milestones, not lump sums. Phased disbursement turns a one-shot game into a sequential game with built-in accountability. Five: align payoffs, don't just add conditions. The best mechanism makes cooperation *genuinely attractive* for both sides, not just punitive for defection.

## Slide: R: Representing and Solving a 2x2 Game
Alright, let's get our hands dirty with some code. *(pause)* Here we're implementing the payoff matrices in R and writing a function that checks best responses for both players to find Nash equilibria. You'll define the donor payoff matrix and the government payoff matrix separately, then loop through every cell asking: is this a best response for the donor given the government's column? Is this a best response for the government given the donor's row? Where both answers are yes, that's your Nash equilibrium. Run this and confirm you get full funding, no absorption — exactly what we found by hand.

## Slide: R: Payoff Matrix Heatmap
Now let's visualize the full 2-by-3 payoff matrix. *(pause)* This heatmap uses color to encode the donor's payoff — green for high, red for low — with both players' values printed as text labels in each cell. You can immediately see the pattern: the donor's payoff is highest in the top-left and lowest in the top-right. The government's payoff increases as you move right. That visual tension — the donor wants to go left, the government wants to go right — is the whole game captured in one image.

## Slide: R: Extensive Form — Backward Induction
Here we implement backward induction in code. *(pause)* You define all the terminal payoffs, then use R to find the government's best response at each information set — after full funding and after reduced funding. Then you work backward: what does the donor get at each branch, given the government's anticipated response? The code confirms what we solved by hand: the subgame perfect equilibrium is full funding, no absorption. And seeing it confirmed computationally — that the government's dominant strategy is always no absorption — really drives home why conditionality isn't optional.

## Slide: R: Simulating a Repeated Game
This last exercise is one of my favorites. *(pause)* We simulate 20 rounds of the funding game, comparing two donor strategies: unconditional funding — always fund high regardless — versus tit-for-tat, where the donor conditions this round's funding on the government's behavior last round.

The government starts by free-riding for the first few rounds, testing the donor. Under unconditional funding, the government keeps free-riding forever — why wouldn't it? Under tit-for-tat, the donor punishes free-riding by reducing funding, the government feels the pain, and eventually switches to cooperation.

Watch the cumulative payoff lines diverge. *(pause)* Tit-for-tat starts behind because of those early punishment rounds, but it dominates over time as cooperation takes hold. That's the power of repeated interaction — it creates the shadow of the future that makes cooperation rational.

## Slide: Key Takeaways
Four essential lessons from today. *(pause)*

First, game theory models the strategic interactions that dominate real-world MNH programs. Ignoring other agents' strategic behavior is no longer an option.

Second, Nash equilibrium reveals the stable outcome when everyone optimizes individually. And in MNH, that often means a free-riding equilibrium — unless you've designed your contracts carefully.

Third, backward induction shows that the sequence of moves matters enormously. Conditional commitments, milestone payments — these tools transform the game's equilibrium by changing what's credible.

And fourth, strategy tables and the causal form connect game theory back to the influence diagrams from Chapters 7 and 8, giving us a unified framework for multi-agent decision problems. It's all one toolkit.

## Slide: Looking Ahead
Next time, we make a big shift. *(pause)* We've spent nine chapters building causal models from expert knowledge and using them for inference and intervention. Chapter 10 asks a fundamentally different question: can we discover causal structure from data itself?

Structure learning, instrumental variables, the limits of observational data — these tools close the loop between theory and evidence. We'll ground everything we've built in real-world health information system datasets. It's where the rubber meets the road.
