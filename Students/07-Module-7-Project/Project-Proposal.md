# DAT 5668 · Agentic AI: Autonomous Decision-Making

# Final Project Proposal

Salih Tutun, PhD · Groups of 1–3 · Half page to one page

---

## Purpose

Write a short proposal **before** you build the full artifact — in your own words — so we can check that:

- the problem is a real business process,
- the family (LLM, RL, or hybrid) fits the work,
- the data plan is legal and feasible,
- you already know what “solved” means in a number the firm tracks.

The proposal feeds the final `Report-Template.md`. It is **not** a substitute for the running notebook or the Session 13 talk. Final grades include a **30-point ranking across all projects** (idea, effort/data/approaches, solution clarity, evaluation clarity, presentation) — start defining clear rules now.

**Due:** check Canvas (aim for about one week before the Dec 14 presentation so you still have time to revise).  
**Format:** Markdown, Word, or PDF · upload to the Canvas proposal dropbox or discussion if one is open.  
**File name:** `Group[X]_Project_Proposal.pdf` (or `.md` / `.docx`).

---

## Header (required)

```
DAT 5668 · Agentic AI: Autonomous Decision-Making
Final Project Proposal

Group: [number or Canvas group name]
Members:
- [Name 1]
- [Name 2]
- [Name 3] (if any)

Date: [submission date]
```

---

## Answer every item (keep it short)

### 1. Business process (2–3 sentences)

What decision is being made, who is affected, and what “solved” means in a **number the firm already tracks**?

Starter cards you may use (or write “own problem”): refund/claims · personalized offer · inventory restock · document review + numeric decision · service handoff · fraud hold vs release.

### 2. Family (2–3 sentences)

Will this be **LLM**, **RL**, or **hybrid**? Why, in terms of the work (documents/exceptions vs repeated numeric decision)? **Who releases the action?**

A prediction-only sklearn / XGBoost / Keras model is not the agent. It may be a **tool** inside the loop.

### 3. Data and tools (3–4 sentences)

**Name** the dataset or API. Which tier (synthetic / public static / live API)? Synthetic is allowed but earns **less credit**. Prefer a free API from [public-apis](https://github.com/public-apis/public-apis) (prefer `No` Auth). Never confidential employer files. Optional: fitted model as a tool.

### 3b. Approaches you will combine (2–4 lines)

List distinct approaches (rule baseline, LLM+tools, Q-learning, bandit, hybrid veto, …). **Fewer approaches = less credit**; aim for 2–3+ with clear roles.

### 4. Agent loop sketch (bullet list)

One line each — specific to your process, not the Session 1 definition:

- Observe:
- Decide:
- Act:
- Feedback:

### 5. Baseline and scorecard plan (3–4 sentences)

What simple rule, fixed offer, or chatbot will you compare against? Which scorecard rows will you fill? **State at least one rule/threshold you will define.** In the final report you will also explain the results **in your own words** — plan for that now.

### 6. Governance preview (2–3 sentences)

Human checkpoint · what you will store for audit · what must not go into a public model.

### 7. Questions for us (2–3 sentences)

What you are unsure about (family split, reward design, API choice, baseline fairness).

---

## Template you can paste

```markdown
DAT 5668 · Agentic AI: Autonomous Decision-Making
Final Project Proposal

Group:
Members:
Date:

1. BUSINESS PROCESS
...

2. FAMILY (LLM / RL / hybrid) AND WHO RELEASES
...

3. DATA AND TOOLS (name + tier)
...

3b. APPROACHES TO COMBINE
...

4. LOOP SKETCH
- Observe:
- Decide:
- Act:
- Feedback:

5. BASELINE AND SCORECARD PLAN
...

6. GOVERNANCE PREVIEW
...

7. QUESTIONS
...
```

---

## Example (hybrid — FX cash sleeve)

**1. Business process**  
A US importer sets a weekly USD / EUR / GBP cash mix. “Solved” means higher USD sleeve value than equal weight on the test window, with a written foreign-currency cap.

**2. Family**  
**Hybrid.** RL (tabular Q) picks the mix; a short language step checks policy text; a fitted risk model is a **veto tool**, not the agent. The Q-policy releases the frequent action unless policy or risk vetoes.

**3. Data and tools**  
Frankfurter FX (no auth) for observe — **tier T3 live API**; Portfolio Optimizer (no auth) as a tool; local language stand-in (optional Gemini). No employer files.

**3b. Approaches to combine**  
(1) Equal-weight **rule baseline** · (2) **Tabular Q** (releases frequent mix) · (3) **LLM policy check** + fitted risk **veto**.

**4. Loop**  
Observe: weekly returns and policy text · Decide: ε-greedy on Q plus veto tools · Act: set mix · Feedback: USD value vs equal weight and veto flags.

**5. Baseline**  
Equal-weight mix. Scorecard: task success (beat equal weight), cost (API calls), latency, grounding (policy cite), KPI (test-window value / drawdown).

**6. Governance**  
Desk can override a veto · store week, mix, Q-action, veto reason · do not paste internal cash forecasts into a public model.

**7. Questions**  
How strict should the foreign-currency cap be in the reward vs a hard veto?

---

## Feedback checklist (instructor / TA)

| Check | Yes / revise |
| --- | --- |
| Real business process + firm KPI |  |
| Family fits the work; who releases is clear |  |
| Dataset **named** + tier noted (synthetic = less credit) |  |
| Approaches plan (aim 2–3+ distinct; roles clear) |  |
| Data plan is public/simulated/API — no confidential files |  |
| Loop is specific; baseline named |  |
| Not a prediction-only DAT 5565 notebook |  |

---

## Common mistakes

- Topic is a model name (“build a DQN”) instead of a business process  
- LLM-only chatbot with no act/feedback or baseline  
- Prediction-only notebook from DAT 5565  
- Confidential employer data  
- Hybrid with no statement of who releases the action  

---

## After feedback

Revise the plan, then build the **running notebook** and fill `Report-Template.md`. Present on **Monday, December 14** (~7 minutes). Written report + notebook due **4:00 pm Central** that day (see Canvas). Late: 10% per day; after five days not accepted.

Questions: salihtutun@wustl.edu
