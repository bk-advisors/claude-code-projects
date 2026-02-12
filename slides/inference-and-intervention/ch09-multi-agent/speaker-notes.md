# Speaker Notes — Chapter 9: Multi-Agent Interventions

## Overview
This is where the course confronts reality: the world pushes back. Chapters 7–8 treated the environment as passive — nature rolls the dice and we optimize against it. But governments, other donors, and implementing partners aren't dice. They're strategic actors who observe our choices and adjust their behavior accordingly. Game theory gives us the formal tools to model these interactions, find stable outcomes (Nash equilibria), and design contracts that align incentives. The MNH workforce absorption game at the end shows how contract design can transform outcomes from 500 lives saved to 4,500 — a 9× improvement — without spending an extra dollar.

## Slide: Learning Objectives
Five objectives that build from foundations to application. Defining games with players, strategies, and payoffs is the vocabulary. Finding Nash equilibria is the core analytical skill. Sequential games and backward induction add timing. Causal-form games connect game theory back to the DAGs from earlier chapters. The MNH donor-government interaction is the capstone — showing that getting the contract design right matters as much as getting the allocation right.

## Slide: Chapter Overview
The five-step flow mirrors the chapter's progression. We start with game theory foundations (players, strategies, payoffs), move to the central solution concept (Nash equilibrium), add sequential structure (extensive form and backward induction), connect it all back to causal models (the book's causal-form innovation), and culminate with the workforce absorption game that ties everything together. The callout makes the key shift explicit: Chapter 7 was one decision-maker against nature, Chapter 8 optimized allocation. Now other agents act strategically.

## Slide: The Single-Agent Assumption Breaks Down
The two-column comparison shows why we need game theory. In Chapters 7–8, other actors were part of the environment — chance nodes with fixed probability distributions. In reality, when the donor commits high funding, the government *observes* this and reduces co-financing. Implementing partners adjust effort based on monitoring intensity. The red callout drives the point home with a concrete example: when a donor organization increases salary support, governments may decrease their own budget for the same line item. Ignoring this strategic response means overestimating program impact.

## Slide: Strategic Actors in MNH
Four strategic agents interact in a typical MNH program. The donor organization maximizes lives saved per dollar. The national government balances health outcomes against fiscal constraints. Implementing partners balance results delivery against operational sustainability. Other donors maximize their own impact metrics. Each makes decisions considering what the others will do. The green callout is the promise of the chapter: game theory gives us tools to predict behavior and design incentive-compatible contracts.

## Slide: The Three Elements of a Game
Every game has players, strategies, and payoffs. In the MNH context: the donor and government are players, their strategies are funding and co-financing levels, and payoffs blend lives saved with cost burdens and political capital. The key assumption — rationality — doesn't mean selfish. It means each player chooses what maximizes *their* payoff, and those payoffs can incorporate altruistic goals. A government that genuinely cares about health outcomes is still rational; it just has different payoffs than one focused purely on fiscal savings.

## Slide: Normal Form: The Payoff Matrix
The payoff matrix is the simplest representation of a game. Each cell contains both players' payoffs for a given strategy combination. The Co-financing Game shows the basic tension: the best collective outcome is (High Funding, High Co-financing) with 2,400 lives, but each player's incentives may pull them elsewhere. Reading the matrix — understanding that each cell shows *(Donor's payoff, Government's payoff)* — is a skill students need to practice.

## Slide: Payoffs Capture Competing Priorities
Now we assign utility scores that reflect each player's actual priorities. The donor values lives saved. The government values lives saved minus a fiscal cost penalty. The orange callout flags that in this simplified version, the Government gets the same utility under different scenarios — which signals we need a more realistic model. The point is that payoff design matters: small changes in how we model costs completely change the game's equilibrium.

## Slide: Refined Payoff Matrix
With more realistic cost assumptions, the game becomes interesting. The best collective outcome (High, High) gives 3,600 total utility. The government prefers high co-financing when the donor funds high (1,200 > 1,100). The donor always prefers high funding. The green callout walks through the interpretation, and the key question at the end sets up the tension: what happens when the government suspects the donor will fund regardless?

## Slide: Dominant Strategies
A dominant strategy is one that's best regardless of what the other player does. Checking systematically: the donor prefers High Funding whether the government co-finances or not (2,400 > 1,800 and 1,400 > 800). The government prefers High Co-financing whether the donor funds high or low (1,200 > 1,100 and 800 > 600). Both have dominant strategies, and they align — (High, High) is a dominant-strategy equilibrium. This is the best-case scenario where incentives happen to point in the same direction.

## Slide: Definition of Nash Equilibrium
Nash Equilibrium is the central solution concept: no player can improve by changing their strategy alone. The underline method — for each column, underline the row player's best response; for each row, underline the column player's best response; cells with both underlined are NE — is the practical procedure students should master. In our refined game, (High Funding, High Co-financing) is the unique NE.

## Slide: When Incentives Misalign: A Harder Game
Now the government faces high political costs for co-financing. With the new payoffs, Low Co-financing dominates for the government (1,100 > 700 when donor plays High; 600 > 500 when donor plays Low). The NE shifts to (High Funding, Low Co-financing) — the donor funds generously, the government free-rides. Total utility drops from 3,100 to 2,500. This is the realistic scenario that makes game theory essential.

## Slide: The Prisoner's Dilemma in Health Funding
The side-by-side comparison with the classic Prisoner's Dilemma makes the structure clear. Both players would prefer mutual cooperation, but individual incentives push toward a suboptimal equilibrium. In the MNH version, it's slightly different — the donor's dominant strategy keeps funding flowing regardless, so the equilibrium is (Fund, Free-ride) rather than (Defect, Defect). The green callout identifies the solution: commitment devices — contracts, conditionalities, or repeated interaction — are needed to sustain cooperation.

## Slide: Multiple Equilibria and Coordination
Some games have multiple Nash equilibria. The workforce cadre game has two: (Midwives, Midwives) and (CHWs, CHWs). Both are stable, but (Midwives, Midwives) is Pareto superior. The risk is miscoordination — the donor invests in midwife training while the government hires CHWs, wasting both investments. The key takeaway is that coordination games explain why joint planning between donors and governments is essential. The problem isn't conflicting interests — it's ensuring both sides invest in the *same* thing.

## Slide: Escaping Bad Equilibria
Four mechanism design approaches for moving from free-riding to cooperation. Conditional funding ("we fund high only if you co-finance ≥30%") directly changes payoffs. Repeated interaction builds reputation over funding cycles. Binding contracts with milestone-triggered disbursements create accountability. Third-party enforcement via World Bank or Global Fund conditionalities adds external pressure. The MNH example — a co-financing escalator with consequences for missing milestones — is exactly how real program agreements work.

## Slide: Game Trees
Extensive-form games add timing. The tree shows the donor choosing High or Low first, then the government responding. Payoffs at terminal nodes show all four outcomes. The sequential structure matters because the government can *observe* the donor's choice before responding — which is exactly what happens in practice when funding commitments are announced before government budget cycles.

## Slide: Backward Induction
This is the algorithm for solving sequential games. Start at the end: the government chooses Low Co-financing regardless of the donor's move (1,100 > 700 after High Funding; 600 > 500 after Low Funding). Working backward: the donor anticipates this and chooses High Funding (1,400 > 800). The outcome is (High Funding, Low Co-financing) with payoffs (1,400, 1,100) — the government free-rides, and the donor funds generously knowing this will happen.

## Slide: First-Mover Advantage in Donor Commitments
The order of moves changes the outcome. When the donor commits first without conditions, the government can observe and free-ride. But if the donor can commit *conditionally* — "High funding if and only if you co-finance ≥30%" — the game changes. The government now faces a real choice: co-finance and get high funding (payoff 700), or don't co-finance and get low funding (payoff 600). It chooses cooperation. Conditionality restores the good equilibrium.

## Slide: Subgame Perfect Equilibrium
SPE refines Nash equilibrium for sequential games by requiring equilibrium in every subgame. Without conditionality, the SPE is (High Funding, Always Low) — the government's strategy of always free-riding is credible because it's optimal at every decision point. With conditionality, the SPE shifts to (Conditional High, High Co-finance). The orange callout is crucial: non-credible threats don't work. If the donor would never actually withdraw funding, the conditionality has no bite. Credibility is everything.

## Slide: Games as Causal Models
The causal-form game is the book's innovation — representing games as multi-agent influence diagrams. Each player has their own decision node and objective node, and the causal structure shows how decisions interact through shared outcomes. This connects game theory directly to the DAGs from Chapters 1–6. The advantage: it makes the causal *pathways* explicit. We can see *why* payoffs have their values, not just what the values are.

## Slide: Converting Between Game Representations
Three representations, each with a purpose. Normal form (matrix) is best for finding Nash equilibria in small games. Extensive form (tree) is best for analyzing timing and commitment. Causal form (DAG) is best for understanding *why* payoffs have their values and connecting to the causal reasoning toolkit. The MNH example illustrates: the causal form reveals that (High Funding, Low Co-finance) gives 1,400 lives because high funding increases equipment and training, but low co-financing means inadequate staffing for sustainability.

## Slide: Adding Chance Nodes
The causal form naturally incorporates uncertainty alongside strategic interaction. Political stability enters as a chance node that neither player controls. If instability is high, even mutual cooperation may yield poor outcomes. This is where game theory meets the decision analysis from Chapters 7–8 — we compute expected payoffs conditional on uncertainty, exactly as before, but now with multiple strategic decision-makers.

## Slide: Representing Contingent Strategies
A strategy in extensive form is a *complete* plan specifying what to do at every decision point. With 2 information sets and 2 actions each, the government has 4 possible strategies: Always High, Always Low, Match (cooperate if and only if the donor does), and Oppose. The "Match" strategy — tit-for-tat — is particularly interesting because it makes the government's cooperation contingent on the donor's. The strategy table enumerates all possible plans, making the strategic landscape explicit.

## Slide: Conditional Funding Agreements
The donor's conditional strategy is operationalized as: "I fund high IF government co-finances ≥30% of recurrent costs AND absorbs ≥80% of trained workers by year 3." This is a contingent strategy — the donor's action depends on observable government behavior. The green callout identifies "Conditional High" as the dominant strategy when the donor can credibly commit. This is exactly the logic behind milestone-based payment agreements used in real MNH programs.

## Slide: Milestone-Based Payments as Commitment
The milestone table shows how conditional strategies become real contracts: 25% at budget line creation, 25% at 200 workers on payroll, 25% at 400 absorbed, final 25% at full absorption. The orange callout raises the fundamental question: milestones only work if the donor *actually* withholds funding when missed. If the government believes the donor will disburse regardless — due to political pressure or sunk-cost fallacy — the conditionality is empty. Credibility is the foundation of commitment power.

## Slide: The Setting
The Workforce Absorption Game is the chapter's capstone. The donor organization trains 500 community health workers with a substantial multi-year investment. The government must absorb these workers onto its payroll within 3 years. If it doesn't, workers leave and the investment is wasted. Both players know the stakes, both act strategically. The setup captures a challenge that every large-scale health workforce program faces.

## Slide: The Payoff Matrix
The 2×3 matrix shows six possible outcomes. The donor values lives saved (4,500 at best, 300 at worst). The government values lives saved minus fiscal cost — and crucially, gets its *highest* utility from No Absorb (1,000) because it avoids the recurring expense of putting hundreds of workers on payroll. This misalignment of incentives is the root of the problem.

## Slide: Finding the Nash Equilibrium
The underline method reveals the tragedy. No Absorb is dominant for the government (1,000 > 900 > 600 after Full Funding; 800 > 700 > 400 after Reduced). Full Funding is dominant for the donor. The NE is (Full Funding, No Absorb) with payoffs (500, 1,000) — a substantial investment in training followed by zero absorption. This is a classic free-rider outcome, and it happens in real MNH programs when contracts aren't structured properly.

## Slide: Redesigning the Game: Commitment Devices
The donor can change the equilibrium through contract design. Device 1 (milestone payments) restructures disbursement so non-absorption means the government gets only initial-phase training, dropping its payoff from 1,000 to 350. Device 2 (bonding agreement) requires the government to deposit funds in escrow, forfeited if targets are missed. Device 3 combines both, making Full Absorb the dominant strategy. This is mechanism design — changing the rules so that the rational choice aligns with the socially optimal outcome.

## Slide: The Transformed Game
The revised payoff matrix with milestone payments changes everything. Under Conditional funding, the government now prefers Full Absorb (600) over Partial (500) over No Absorb (350). The new NE is (Conditional Funding, Full Absorb) with payoffs (4,500, 600). The key takeaway is stunning: the donor achieved a 9× improvement in expected impact — from 500 to 4,500 lives — by restructuring incentives rather than increasing funding. Same budget, radically different outcomes.

## Slide: Lessons from the Absorption Game
Five principles for multi-agent program design. Map the game first — identify players, strategies, and payoffs before committing funds. Check for dominant strategies — if free-riding dominates, unconditional funding will fail. Design for subgame perfection — conditionalities must be credible. Use milestones not lump sums — phased disbursement turns a one-shot game into a sequential game with accountability. Align payoffs don't just add conditions — make cooperation genuinely attractive for both sides.

## Slide: R: Representing and Solving a 2x2 Game
Live coding walkthrough. Students implement the payoff matrices and a Nash equilibrium finder that checks best responses for both players, confirming the (Full Funding, No Absorb) equilibrium.

## Slide: R: Payoff Matrix Heatmap
Live coding walkthrough. Students create a heatmap visualization of the full 2×3 payoff matrix, with color encoding the donor's payoff and text labels showing both players' values.

## Slide: R: Extensive Form — Backward Induction
Live coding walkthrough. Students implement backward induction by finding the government's best response at each information set, then the donor's optimal choice anticipating those responses.

## Slide: R: Simulating a Repeated Game
Live coding walkthrough. Students simulate 20 rounds of the funding game comparing unconditional funding (always High) with tit-for-tat (conditional on government's last action), showing how tit-for-tat induces cooperation and dominates over time.

## Slide: Key Takeaways
Four essential lessons. Game theory models the strategic interactions that dominate real-world MNH programs. Nash equilibrium reveals the stable outcome — often a free-riding equilibrium when incentives are misaligned. Backward induction shows how the sequence of moves matters and why conditional commitments transform outcomes. Strategy tables and the causal form connect game theory to the influence diagrams from Chapters 7–8, providing a unified multi-agent decision framework.

## Slide: Looking Ahead
Chapter 10 returns from theory to practice. We've spent Chapters 1–9 building causal models from expert knowledge and using them for inference and intervention. Chapter 10 asks: can we discover causal structure from data? Structure learning, instrumental variables, and the limits of observational data close the loop between theory and evidence — grounding everything we've built in real-world DHIS2 datasets.
