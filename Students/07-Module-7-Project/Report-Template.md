# DAT 5668 project report

Salih Tutun, PhD · DAT 5668 · Agentic AI: Autonomous Decision-Making

Fill this out with your group. We grade with `Grading-Rubric.md` (**69 absolute + 30 ranking** on the Final Project; proposal is **1** point separately). Name your dataset. List the approaches you combined (one approach earns less; three or more that really run earn more). Write your own rules. **Most important: explain your results and evaluation in your own words** — not a pasted ChatGPT paragraph.

Group members:

Business problem (one real process the firm already runs):

Starter card used, if any (or write “own problem”):

Family (LLM, RL, or hybrid):

## Dataset used (required)

- Exact name + link/citation:
- Tier (synthetic / public static / live API / multi-source / validated synthetic):
- Why this source fits observe or act (one or two sentences in your voice):

## Approaches combined (required)

List each **distinct** approach that **actually runs**, and what job it does (baseline, policy, veto, tool, …). Fewer approaches → less credit.

1.
2.
3. (if any)

Other data / tool notes (no confidential employer files; a fitted ML model may only be a tool):

## 1. The problem and the artifact

In a few sentences, in your own words: what decision is being made, who feels the pain, and what “solved” means as a number the firm already tracks. Then say how a teammate could open this notebook next Monday and run it again.

## 2. Agent loop

What happens in *this* process — not a copy of the Session 1 definition.

- Observe:
- Decide:
- Act:
- Feedback:

## 3. Why this family

Why LLM, RL, or hybrid for this work (not because the model name sounds cool)? Who releases the frequent action?

## 4. Your rules (you define these)

List the measurable decision / reward / veto / threshold rules your agent uses.

## 5. Evaluation and results (write this carefully)

Baseline you **ran** (a fair simple rule, chatbot, or heuristic — not a straw man):

| Metric | Your agent | Baseline | Your rule / threshold |
| --- | --- | --- | --- |
| Task success |  |  |  |
| Cost |  |  |  |
| Latency |  |  |  |
| Safety, or grounding if the task is documents |  |  |  |
| Business KPI |  |  |  |

### Explain the results in your own words (required)

Write 1–2 short paragraphs as your team would say them out loud. Cover: what the scorecard shows, whether you beat the baseline (or lost — that is fine if you say so), what surprised you, and what you would fix next. Do **not** paste generic AI text here. This write-up carries real points.

Would you deploy this? What still fails? When should a person step in?

## 6. What you tried (hard work)

A quick before/after or two settings you compared:

## 7. Governance note

- Human checkpoint:
- What you store for an audit:
- What must not go into a public model:
- Buy vs build:

## 8. How the work was split

What each member built or wrote.
