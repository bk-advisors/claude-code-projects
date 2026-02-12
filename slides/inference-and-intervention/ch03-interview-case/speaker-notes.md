# Speaker Notes — Chapter 3: The MNH Diagnostic Case Study

## Overview
This chapter is where theory meets practice. We take the qualitative modeling toolkit from Chapter 2 and apply it to a realistic consulting engagement: diagnosing why Country X's MNH program is underperforming despite substantial investment. The big lesson is the iterative model-building process — start with the simplest possible model, use it to guide interviews, and expand it only as new evidence demands. By the end, students will see how a causal model evolves from a 4-node sketch to a 12-node diagnostic framework that reveals the real bottlenecks.

## Slide: Learning Objectives
Five objectives, all hands-on. This chapter is about *doing* causal modeling, not just understanding the concepts. Students will practice the iterative cycle of hypothesis → interview → model revision, learn to distinguish root nodes (where you intervene) from intermediate nodes (where effects flow through), and see how the final model naturally produces prioritized recommendations.

## Slide: Chapter Overview
This is adapted from the Hubris Health consulting case in Ryall & Bramson's textbook — a health insurance company with declining performance. We've transplanted the same diagnostic methodology into an MNH context. The five-step flow — case setup, then three interview rounds, then final recommendations — mirrors how real consulting engagements work. Each interview round expands the model and reveals new bottlenecks.

## Slide: The Iterative Process
This is the methodological heart of the chapter. The key principle is "start simple and add complexity only when you need it." You don't walk into a consultation and build a 20-node DAG on day one. You start with the most stripped-down model — maybe three or four nodes — and let the interviews tell you what's missing. Each time the model fails to explain what stakeholders are telling you, that's a signal to add new variables or links. The model drives the questions, and the answers drive the model.

## Slide: Key Principles from the Book
Four principles that guide good diagnostic modeling. First, focus on significant drivers — not every variable is equally important. Second, look for common causes that explain multiple symptoms simultaneously, because those are your highest-leverage intervention points. Third, use the model to generate *specific* questions — vague questions get vague answers. Fourth, the final model should tell a coherent causal story from decisions to outcomes. These principles apply whether you're diagnosing an MNH program or a corporate strategy problem.

## Slide: The Program Brief
Here's the scenario. Country X's MNH program has spent nearly all its money (96% disbursed) but hasn't achieved its targets — coverage is 42% against a target of 70%, and both NMR and MMR are significantly off track. The puzzle is clear: the money went out the door, but the outcomes didn't materialize. Why? That's what our diagnostic needs to answer. This gap between spending and results is the central mystery of the case.

## Slide: Initial Situational Assessment
We start by walking backwards from the objective. What causes NMR reduction? Quality of care. What causes quality? Intervention coverage. What causes coverage? Investment. But investment has been made — nearly all funds were disbursed. So the break must be somewhere between investment and coverage. This is a simple but powerful deduction: the bottleneck isn't about money, it's about the transmission mechanism. Something between "money spent" and "lives saved" is broken.

## Slide: The Initial (Simple) Model
This four-node chain — Investment → Programs Implemented → Coverage → NMR — is deliberately too simple. And that's the point. We want students to see what's wrong with it: it treats "Programs Implemented" as a black box, it doesn't identify which programs are failing or why, there are no confounders, and the only decision variable is the initial investment. This model tells us almost nothing actionable. We need interviews to crack open that black box.

## Slide: MOH Director Interview
Now we go talk to people. The MOH Director gives us three crucial pieces of information. First, equipment is in the hospitals but staff don't know how to use it — a competency gap. Second, 3,000 health workers were trained but old practices persist — training isn't translating to behavior change. Third, the staff-to-patient ratio is 1:22 against a standard of 1:4 — a massive staffing shortage. Each quote maps directly to a new variable in our model. This is how interviews expand the DAG.

## Slide: Updating the Model: Round 1
We've gone from 4 nodes to 7. The key insight is the gap between inputs and effective use — equipment was procured (check), training was delivered (check), but staff competency and equipment utilization remain low. The checkmarks and X marks in the diagram tell a vivid story: things that money can buy directly are fine; things that require sustained capacity are failing. This reframes the problem from "did we invest enough?" to "are the investments translating into practice?"

## Slide: What Questions to Ask Next?
This is where the model earns its keep. Without a model, you'd go into your next interviews with general questions. With the model, you know *exactly* what to ask: Why aren't trained workers applying their training? Why is equipment procured but not used? Is staffing the binding constraint? The model converts a vague diagnosis into specific, testable hypotheses. Each hypothesis points you to a specific stakeholder group — in this case, facility directors who see the front-line reality.

## Slide: Hospital Director Interviews
Round 2 takes us to the facilities, and it's revelatory. Finding 1: of 40 nurses trained on CPAP, only 18 remain — staff attrition is wiping out training investments. Finding 2: CPAP machines are breaking down with no biomedical technician and 3-month parts delays — equipment maintenance is nonexistent. Finding 3: eclampsia patients face 4-6 hour transport delays — the referral system is failing independently. Each finding adds a new variable to the model: retention, maintenance, referrals. These are the transmission failures the initial model completely missed.

## Slide: Updating the Model: Round 2
Now we have 10 nodes, and a critical pattern emerges. Staff retention and equipment maintenance are common causes — they each affect multiple downstream variables simultaneously. Retention affects both competency (trained staff leave) and utilization (not enough staff to run the equipment). Maintenance affects equipment utilization directly. These are fork structures, which means they're high-leverage intervention points. Fixing retention alone would unblock multiple pathways.

## Slide: Identifying Triplet Structures
This is where students connect the theory from Chapter 2 to a real-world model. The expanded DAG contains all three triplet types. Chains: Training → Competency → Coverage. Forks: Competency ← Retention → Utilization (retention drives both). Colliders: Staffing → Quality ← Equipment (if quality is observed as low and equipment is good, staffing must be bad). Recognizing these structures isn't just academic — it determines what you should and shouldn't control for in your analysis.

## Slide: Community Health Worker Interviews
Round 3 opens up an entirely new dimension: demand. Up to now, we've been focused on the supply side — can hospitals deliver quality care? But the CHW interviews reveal that many mothers never reach the hospital in the first place. Transport takes 3 hours on foot, some families prefer traditional birth attendants, and even "free" services involve unaffordable out-of-pocket costs for transport and food. Supply-side quality improvements don't help if patients can't access them.

## Slide: Updating the Model: Round 3
The complete model now has 12 nodes organized in three layers: supply side (what the program invested in), demand side (whether patients can access services), and outcomes. The final DAG tells a coherent story: investment flows through multiple channels, but is undermined by staff attrition and equipment breakdown on the supply side, and by geographic, cultural, and financial barriers on the demand side. Both supply and demand must work for NMR to decline.

## Slide: The Complete Causal Model
This summary table is the diagnostic punchline. Inputs are adequate (check mark). But the transmission layer is broken (X), the demand side was underestimated (X), and outcomes are below target (X). The bottleneck isn't about how much money was spent — it's about the pathways through which that money was supposed to translate into impact.

## Slide: Evolution of the Model
This evolution table — from 4 nodes to 7 to 10 to 12 — is the pedagogical payoff of the iterative approach. At each stage, the model told us what was missing and what to ask next. The green callout reinforces the core lesson: start simple, add complexity incrementally, and let the model guide your inquiry. Students should be able to apply this same process to any diagnostic engagement.

## Slide: Prioritizing Recommendations
The causal model doesn't just diagnose problems — it prioritizes solutions. High priority goes to staff retention programs (they affect multiple downstream pathways) and equipment maintenance systems (they unblock the products pathway). Medium priority goes to referral networks (independent pathway to mortality) and demand-side interventions (community outreach, transport subsidies). The prioritization follows directly from the DAG structure: root causes with the most downstream effects get addressed first.

## Slide: Why Root Nodes Matter
Root nodes — variables without parents in the model — are where the highest-leverage interventions live. In our model, staff retention and equipment maintenance emerged as critical root nodes that the original investment plan didn't address at all. The key takeaway is in the yellow box: the program invested in the right inputs (training, equipment) but missed the transmission mechanisms (retention, maintenance). Redirecting a portion of the budget to these mechanisms could unblock the entire chain.

## Slide: R: Round 1 — Simple Model
Live coding walkthrough. Students build the 7-node supply-side model in dagitty, starting from the Round 1 interview findings.

## Slide: R: Round 2 — Adding Transmission Failures
Live coding walkthrough. Students expand to 10 nodes by adding retention, maintenance, and referral variables discovered in Round 2.

## Slide: R: Round 3 — Complete Model
Live coding walkthrough. Students build the full 15-node model including demand-side variables from Round 3.

## Slide: R: Identifying What to Measure
Live coding walkthrough. Students use adjustmentSets() and impliedConditionalIndependencies() to determine what the model says they need to measure and what testable predictions it generates.

## Slide: Key Takeaways
Three things. Build models iteratively — start simple, add complexity as evidence warrants. Root nodes are leverage points — staff retention and equipment maintenance were the hidden bottlenecks. The model guides the analysis — each round's model told us what to ask next, what data to collect, and where the bottlenecks were. This is the practical power of causal modeling for program evaluation.

## Slide: Looking Ahead
Next chapter we add numbers to these qualitative models. Conditional probability tables replace the [+]/[-] signs, Bayes' rule lets us update beliefs with evidence, and we get the mathematical machinery for precise inference and decision analysis. We built the skeleton in Chapters 2-3; Chapter 4 adds the flesh.
