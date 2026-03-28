# Speaker Notes — Storytelling with Data

## Overview
This session is about the full craft of data storytelling — not just how to make a chart, but how to think diagnostically and predictively about the story behind and ahead of the data. We use two case studies from BK Advisors' data visualization portfolio (Africa Measles, HPV-PNG) to illustrate the framework.

## Slide: The Chart That Started a Project

Last year I read an article on Our World in Data about measles vaccination — "Measles vaccines save millions of lives each year" by Saloni Dattani and Fiona Spooner. 94 million lives saved over 50 years. That's a powerful number.

But what actually stopped me wasn't the number. It was a heatmap. They had this visualization of measles cases across US states from 1929 to 2022. Before the vaccine, it's a wall of color — cases everywhere, every year. Then around 1963, the color just drops off. A cliff. You could see the intervention working without reading a single label.

*(pause)*

I stared at that chart and thought: what does this look like for Africa? Africa is where the burden is heaviest, where the most lives have been saved by vaccination campaigns. So I opened R, pulled the WHO data, and started building my own version. That afternoon became the africa-measles project. And it taught me something I keep re-learning: the most important part of a data story is the question that got you to open the dataset in the first place.

## Slide: Part I — Philosophy (Section Divider)

Let's start with where stories begin.

## Slide: Where It Starts

It all starts with curiosity. That itch of a question you want to answer.

But the question builds from a few places. A phenomenon you've observed. A curiosity about what caused it. A desire to measure it. And eventually — a need to communicate it to someone who can act on it. That last one matters more than people think.

*(pause)*

I've been doing data visualization since 2015, and I've come to think of the full arc of a data story as four modes. Diagnostic — why did this happen? Descriptive — what does the data show? Prescriptive — what should we do about it, and how do we communicate it? And predictive — what will happen next? Most data storytelling courses focus on the middle two — the descriptive and prescriptive parts — and skip the bookends.

## Slide: What's the Norm

Here's the standard analysis process most of us learned — define a problem, collect data, clean it, explore it, visualize it, report it. Done.

*(pause)*

It's fine when you're starting out. It's linear, it's manageable, it gets you from A to B. But it skips the curiosity, the meaning, the creative side. It tells you how to get from data to chart, but not why you should care, who you're making it for, or what you want them to do with it.

## Slide: Start with an Audience of One

I strongly believe that data visualization is complementary to good writing and storytelling. The story comes first.

Morgan Housel barely uses charts, but you can't stop reading his writing. He doesn't need a chart to make you feel the weight of a number. He uses context, comparison, and a well-placed anecdote.

So when I start a new data story, I begin with one person. A specific reader, colleague, or client. And I ask: what would make this person stop scrolling and actually read?

Three questions before you touch data: Who are you making it for? Why should it matter to them? What will move them to act?

## Slide: Part II — Making a Story (Section Divider)

Now let's get into the process. Five steps, adapted from Aman Bhargava's excellent framework, but through a consulting lens.

## Slide: Step 1 — Find Your Question

Every data story starts with an itch. Something doesn't add up. Something surprises you.

Here's a useful test. Can you fill in this sentence: "I am curious about X, so I will measure Y to see if Z is true." If you can't complete it, you don't yet have a question — you have a topic.

*(pause)*

Look at these two examples. "Measles in Africa" — that's a topic. It's vague. "Did the 2001 WHO/UNICEF initiative cause the dramatic decline in measles cases across African countries?" — that's a question. It's specific, testable, and leads somewhere.

## Slide: Step 2 — Make It Measurable

A question becomes answerable when you can translate it into operations on data.

The pattern is almost always the same: filter — which countries, which years? Group — by what category? Summarize — count, rate, ratio. Compare — before versus after, country A versus country B.

In consulting, this is the step where you turn a Terms of Reference into an analytical question.

## Slide: Step 3 — Analyze

Four basic operations power most findings: filter, group, summarize, compare. You don't need statistical expertise. You need clarity of thought.

*(pause)*

And here's something important — when analysis yields nothing interesting, don't reach for fancier methods. Go back and revisit the question. A better question almost always beats a better algorithm.

## Slide: Step 4 — Synthesize

This is the step most people skip, and it's the most important. Declare what you found — in one sentence.

The "so what?" test: if you can't answer "so what?" in one clear sentence, you're still doing exploration, not explanation. Exploration is the work you do for yourself. Explanation is the communication you prepare for your reader.

Look at these two examples. On the left — twelve charts with various normalizations. That's exploration. On the right — one clear sentence about coordinated campaigns driving a 90% decline. That's explanation.

## Slide: Step 5 — Choose Your Form

The chart type is the last decision, not the first. What most people get wrong about data visualization is thinking it starts with choosing between a bar chart and a line chart. It starts with having something to say.

*(pause)*

And sometimes the right form isn't a chart at all. For the HPV story in Papua New Guinea, the right form was a scrollytelling experience. Because the audience needed to experience the scale of the problem, not just see a number.

The form is the last decision. The question is the point.

## Slide: Part III — The Missing Pieces (Section Divider)

Now here's where my approach goes beyond the standard framework. This is the part I've developed from my consulting practice and my physics education.

## Slide: Most Data Stories Stop Here

The five-step process is prescriptive — it tells you how to make a data story. But it operates almost entirely in the present tense. Here's data, here's a finding, here's a chart.

What's missing are two other modes of thinking. Diagnostic thinking — why did this happen? What's the causal chain? And predictive thinking — what will happen next? What are the scenarios?

## Slide: The Diagnostic Lens

"Why did this happen?" — that's the diagnostic question.

*(pause)*

This instinct comes from two places. The physics instinct — every effect has a cause, and causes are testable. You don't just observe that an object accelerated. You identify the force. The consulting instinct — clients don't just want to know what happened. "Measles declined" is interesting. "Measles declined because of coordinated campaigns" is actionable.

## Slide: Case Study — Africa Measles Heatmap

Here's a project where diagnostic thinking changed the story.

The descriptive story is simple: measles cases dropped 90% across Africa. That's what the data shows.

But the diagnostic story is richer. The 2001 WHO/UNICEF Measles Initiative marks a visible inflection point in the heatmap. Before 2001, high-burden red tiles everywhere. After 2001, a dramatic shift to blues and greens. But not uniformly — countries with high supplementary immunization coverage saw faster declines, while countries with conflict or weak health systems lagged.

The heatmap's temporal structure reveals the causal mechanism. The visual cliff at 2001 is the diagnosis.

## Slide: The Predictive Lens

"What comes next?" — that's the predictive question.

*(pause)*

If you understand the mechanism — the diagnostic layer — you can model the future. Newton's laws don't just explain why the ball fell. They tell you where it will land.

In consulting, recommendations without projected impact are just opinions. "PNG should vaccinate" is a recommendation. "80% coverage by 2030 projects a 65% reduction in cervical cancer deaths" — that has teeth.

## Slide: Case Study — HPV Vaccination in PNG

Here's a project where predictive thinking drove the form.

The prescriptive story is that PNG should implement HPV vaccination. But the predictive story is what makes it compelling — what the data projects will happen to cervical cancer rates under different scenarios.

The scrollytelling format was deliberately chosen because the prediction needs to be felt, not just seen. As the reader scrolls, the projected future unfolds. Different coverage scenarios are explorable. The abstract becomes tangible.

## Slide: Completing the Loop (Section Divider)

Now let's put it all together.

## Slide: The Four Modes of Data Storytelling

Here's the framework I've arrived at after a decade of practice. Four quadrants, two axes.

Diagnostic — why did this happen? Backward-looking, causal. Descriptive — what is happening? Present state, the data itself. Prescriptive — what should we do? Process-oriented, actionable. Predictive — what will happen next? Forward-looking, modeled.

Most data storytelling frameworks live in descriptive plus prescriptive. The best stories also engage diagnostic plus predictive.

## Slide: The Full Loop

*(pause)*

Descriptive tells them what. Diagnostic tells them why. Prescriptive tells them how. Predictive tells them what if. Most data stories cover one or two. The best ones cover all four.

When you tell a story that covers all four quadrants, you're not just presenting data — you're building an argument. And arguments are what change minds.

## Slide: The Compound Effect

My first data visualization in 2015 was a simple bar chart. Each project since has built on the last. The measles heatmap taught me how temporal structure reveals causal mechanisms. The HPV-PNG project taught me how interactivity makes predictions feel real.

*(pause)*

You don't need to master all four quadrants on day one. But know they exist. And notice when your story is missing one.

Start with a clear question. Make it measurable. Analyze with discipline. Synthesize with conviction. Choose a form that serves the finding. And when you're ready — ask why it happened and what comes next. That's when lowercase storytelling becomes something more.

## Slide: Closing

Thank you. BK Advisors — Storytelling with Data.
