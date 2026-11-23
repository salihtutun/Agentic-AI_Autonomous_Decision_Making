# DAT 5668 · Agentic AI: Autonomous Decision-Making

# Final Project Grading Rubric

Salih Tutun, PhD · **100 points** · 30% of the course

Grade with the filled `Report-Template.md`, the notebook that actually runs, and the Session 13 talk (~7 minutes). You may build an **LLM**, **RL**, or **hybrid** agent. A chatbot demo or a prediction-only DAT 5565 notebook is not enough. A sklearn / XGBoost / Keras model can sit **inside** the loop as a tool — it cannot be the whole project.

---

## How grading works (read this first)

| Part | Points | What it is |
| --- | --- | --- |
| **A. Absolute checklist** | **70** | The must-haves: named dataset, approaches you combined, your rules, scorecard, **results explained in your own words**, governance, talk |
| **B. Ranking score** | **30** | How your project stacks up against **everyone else’s** this term |

**Ranking matters a lot.** We reward a real idea, hard work, better data, more than one real approach, and a clear story about what the numbers mean. A thin synthetic demo with one approach will not climb the ranking just because something was submitted.

### What earns a strong grade

| If you… | You tend to earn… |
| --- | --- |
| **Name your dataset/API** and go beyond toy synthetic data | Higher Section 5 + ranking |
| **Combine more distinct approaches** (not renamed copies) | Higher Section 6 + ranking |
| Pick a **real business process** with a firm KPI | Higher idea ranking |
| **Work hard**: deep loop, iteration, someone else could rerun it | Higher effort ranking |
| Make the **solution easy to follow** | Higher solution-clarity ranking |
| **Explain results and evaluation in your own words** (not pasted AI prose) | Higher Section 7 + B4 |
| Show a **fair baseline** and a full scorecard | Higher evaluation ranking |

### Say it in your own words (this is huge)

Tables and plots are not enough. In the report **and** in the talk, you must explain — in plain language, as your team — what happened, why the baseline comparison is fair, what surprised you, and whether you would deploy. Copied ChatGPT paragraphs, empty template fillers, or “the model performed well” with no numbers will lose points here and on ranking.

### You write the rules

You choose hold/release, rewards, vetoes, and scorecard thresholds for *your* process. Vague rules earn less; clear, measurable ones earn more.

---

## Credit ladders students should know

### Dataset ladder (you must **name** the source)

| Tier | Examples | Absolute credit (Section 5 source quality) | Ranking note |
| --- | --- | --- | --- |
| **T1 — Synthetic / toy only** | Tiny handmade table; random noise with no realism check | **Lower** (cap applies) | Rarely reaches Exceptional |
| **T2 — Public static dataset** | Named open dataset / CSV with clear provenance | Mid | Solid |
| **T2.5 — Realistic synthetic with validation** | Generated data with documented distributions + sanity checks vs real patterns | Between T1 and T2 | Better than toy; still below live API |
| **T3 — Live free API or multi-source** | Named API(s) from [public-apis](https://github.com/public-apis/public-apis) (prefer No Auth); API + public data **joined in the loop** | **Higher** | Favored in ranking |

**Live vs cached:** one API fetch saved to JSON then replayed forever counts as **public/static (T2)**, not full T3. Full T3 needs the notebook to call the API (or documented refresh) on a normal rerun.

**Required:** state the exact dataset or API name and URL/citation in the report and notebook. Unnamed source → heavy deduction.

Never confidential employer files (including “anonymized” employer dumps).

### Approaches ladder (fewer approaches = less credit)

An **approach** is a distinct decision method that actually runs in your artifact, for example:

- simple rule / heuristic baseline  
- LLM + tools / retrieval  
- bandit  
- tabular Q-learning  
- DQN / DDQN (optional, not required)  
- fitted ML model **as a tool** inside the loop  
- hybrid handoff or policy / risk **veto** module  

| Count of distinct approaches | Absolute credit (Section 6) | Ranking note |
| --- | --- | --- |
| **1 only** (e.g. single LLM or single Q-table, no real baseline method) | **Low** | Weak comparative standing |
| **2** compared or combined with clear roles | Mid | Competitive |
| **3+** meaningfully combined (each has a role; not the same method renamed) | **High** | Favored for top tiers |

**Anti-gaming:** “DQN v1 / DQN v2 / DQN v3” is **one** approach. Multiple tools under one LLM decider count as **one** LLM approach. A baseline that never runs does not count. Diagrams without matching code paths do not count. Approaches must appear in the notebook run, not only in the write-up.

### Other ladders that affect credit

| Ladder | Lower credit | Higher credit |
| --- | --- | --- |
| **Baseline fairness** | Always-approve / strawman / mismatched window | Status-quo or simple strong policy on the **same** data and KPI |
| **Rules specificity** | “Be careful” / vague | If–then on named fields with numbers; rules match the run |
| **KPI strength** | Model accuracy only | Cost, SLA, fill rate, false holds, USD sleeve value, etc. |
| **Iteration evidence** | One shot | Before/after or ablation of ≥2 settings on the scorecard |
| **Failure / escalation** | Agent always acts | When agent must **not** act; veto/escalate fired in a run |
| **Scorecard honesty** | Cherry-picked wins; hidden losses | Full rows; same scope; baseline wins stated clearly |
| **Reproducibility** | Hidden keys, unclear rerun | Restart & Run All; env-based keys; seeds where stochastic |

---

## What full credit looks like (quick view)

| Piece | Full credit |
| --- | --- |
| Dataset | **Named**; tier justified; synthetic alone is allowed but scores lower |
| Approaches | **2–3+ distinct** methods combined or compared with clear roles |
| Loop | Observe, decide, act, feedback specific to this process |
| Family | LLM, RL, or hybrid fits the work; who releases is clear |
| Rules | Written by the team and used in the run |
| Evaluation | Notebook runs; fair baseline; full scorecard; **results explained in the team’s own words** |
| Governance | Checkpoint, audit, privacy, buy vs build |
| Talk | ~7 minutes; names dataset + approaches; any member can say who releases — and can talk through the scorecard |
| Ranking | Stands out on idea, effort, clarity, data, approaches, and honest evaluation story |

---

# Part A — Absolute checklist (70 points)

## Section 1 — Title and team (2 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Title | 1 | Names the business process, not only a model name |
| Team | 1 | All members listed; group of 1–3 |

---

## Section 2 — Problem and artifact (7 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Business process | 2.5 | One real process the firm already runs |
| “Solved” metric (firm KPI) | 2.5 | A number the firm already tracks — not only model accuracy |
| Reusable artifact | 2 | How someone runs this notebook again on a new day / ticket / feed |

**Deductions:** model-name-as-problem (−2); accuracy-only with no ops KPI (−1.5); one-off demo (−2).

---

## Section 3 — Agent loop (10 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Observe | 2.5 | What state or inputs the agent sees |
| Decide | 2.5 | How the action is chosen **using your rules** |
| Act | 2 | What changes in the world or system |
| Feedback | 3 | Reward, penalty, correction, or next-state signal |

**Deductions:** missing any loop step (−2 each); copied textbook wording (−3).

---

## Section 4 — Why this family (6 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Family choice | 1.5 | LLM, RL, or hybrid stated |
| Work-based reason | 3 | Follows the process, not the model brand |
| Who releases | 1.5 | System or person; hybrid must say the split |

---

## Section 5 — Dataset and tools (8 points)

| Criteria | Points | Description |
| --- | --- | --- |
| **Named source** | 2 | Exact dataset or API name + link/citation in report **and** notebook |
| **Source quality (ladder)** | 4 | T1 synthetic/toy only → **≤1.5**; T2.5 validated synthetic → **≤2.5**; T2 public static **or cached API dump** → **≤3.5**; T3 live API / multi-source in the loop → **up to 4** |
| Fit to process | 1 | What the **loop** loads (not a unused file in the repo) |
| Tool use (if any) | 1 | Fitted ML is a tool inside the loop, not the whole artifact |

**Deductions:** unnamed source (−2); confidential data (−all of Section 5); prediction-only notebook (−3); secrets committed (−2); cited public data but loop uses a different toy table (−2 and tier = T1).

---

## Section 6 — Approaches combined (6 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Approaches listed | 1.5 | Named list of distinct approaches that **run** |
| Count / depth (ladder) | 3.5 | **1 approach → ≤1.5**; **2 → ≤2.5**; **3+ meaningful → up to 3.5** |
| Roles clear | 1 | What each approach does (e.g. baseline vs policy vs veto) |

**Deductions:** approaches claimed but not run (−3); renamed duplicates counted as many (−2).

---

## Section 7 — Evaluation, results, and your explanation (15 points)

This section is one of the most important parts of the grade. Numbers without your story are incomplete.

| Criteria | Points | Description |
| --- | --- | --- |
| Running artifact | 2 | Notebook runs end-to-end |
| Your rules, specific | 2 | Measurable decision / reward / veto / thresholds |
| Fair baseline | 2 | Simple rule/chatbot/heuristic **run** on the **same** window/KPI (strawman → **≤1**) |
| Scorecard | 3 | Task success, cost, latency, safety/grounding, business KPI for agent **and** baseline |
| **Results in your own words** | **4** | Plain-language write-up: what the scorecard shows, why, what you tried, what still fails — **written by the team**, not AI filler |
| Deploy judgment + failures | 2 | Would you deploy? When must the agent **not** act / escalate? |

**Scorecard (required in report; preferably printed from notebook):**

| Metric | Your agent | Baseline | Rule / threshold |
| --- | --- | --- | --- |
| Task success |  |  |  |
| Cost |  |  |  |
| Latency |  |  |  |
| Safety or grounding |  |  |  |
| Business KPI |  |  |  |

**What “own words” means:** a stranger from ops could read 1–2 short paragraphs and understand the outcome. Name the metrics. Say if the baseline won. Do not paste generic AI text.

**Deductions:** no baseline (−3); missing scorecard rows (−1 each); vague rules (−2); screenshots-only (−3); cherry-picked wins / hidden baseline wins (−2 and B4 capped); **no real explanation of results (−4)**; **obvious AI-written evaluation with no team voice (−3 and B4/B5 capped)**.

**Honesty:** saying the baseline won — clearly — still earns full deploy credit. Safety/grounding includes **correct non-actions** (veto, escalate, refuse).

---

## Section 8 — Governance (6 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Human checkpoint | 1.5 | Named trigger + who approves (not only “human in the loop”) |
| Audit trail | 1.5 | **Named fields** stored (e.g. timestamp, inputs, action, override reason) |
| Privacy | 1.5 | What must not go into a public model |
| Buy vs build | 1.5 | Honest ownership note with at least one tradeoff |

**Release-gate evidence:** full credit prefers at least one run where a veto / escalate / hold rule **fires** (or an explicit log that zero fires was expected and why).

---

## Section 9 — Live presentation (5 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Time and structure | 1.5 | ~7 minutes; loop → dataset/approaches → scorecard → governance |
| Substance | 2 | Names **dataset**, **approaches**, rules; **explains scorecard results in plain speech**; who releases |
| Team ownership | 1.5 | Any member can answer who releases **and** walk through one scorecard row |

---

## Section 10 — Code / artifact quality (5 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Runs and is readable | 2 | Clear cells; instructions to rerun |
| Honest limits | 1.5 | What was simulated, stubbed, or left for later |
| Iteration / ablation note | 1.5 | Brief before/after or ≥2 settings tried (hard-work evidence) |

---

# Part B — Ranking score (30 points) — comparative across all projects

Every project is compared to every other project. **Dataset tier** and **number of real approaches** feed especially into B2 and B4.

## Ranking criteria (6 points each = 30)

### B1. Idea quality and business importance (6)

| Score | What we see |
| --- | --- |
| 5–6 | Sharp real process, credible firm KPI, convincing ops/investor story |
| 3–4 | Solid topic; some vagueness |
| 1–2 | Thin idea or model-name-as-topic |

### B2. Effort, data richness, and approach depth (6)

| Score | What we see |
| --- | --- |
| 5–6 | Hard work + **T2/T3 data** + **3+ real approaches** (or deep hybrid) + iteration |
| 3–4 | Meets bar; mid data/approaches |
| 1–2 | Toy synthetic + single approach; minimal effort |

### B3. Solution clarity (6)

| Score | What we see |
| --- | --- |
| 5–6 | Stranger can follow loop, rules, who releases, and each approach’s role |
| 3–4 | Mostly clear |
| 1–2 | Hard to tell what runs |

### B4. Evaluation clarity (6)

| Score | What we see |
| --- | --- |
| 5–6 | Fair baseline, full scorecard, **clear own-words story** of results, honest losses, failure/escalation cases |
| 3–4 | Scorecard present but thin, one-sided, or mostly unexplained numbers |
| 1–2 | Claims without numbers, cherry-picking, or evaluation text that does not sound like the team |

### B5. Overall impact and presentation (6)

| Score | What we see |
| --- | --- |
| 5–6 | Professional; talk names dataset + approaches; team owns the story |
| 3–4 | Understandable |
| 1–2 | Confusing or weak ownership |

---

## How ranking points are assigned

1. Instructor (and TAs, when used) score B1–B5 (1–6 each).
2. Projects are ordered by total ranking score.
3. Tiers convert standing into the **30 points**:

| Tier | Rough standing | Points (of 30) |
| --- | --- | --- |
| **Exceptional** | Top ~10% | 28–30 |
| **Excellent** | Top ~25% | 24–27 |
| **Very good** | Top ~50% | 20–23 |
| **Good** | Top ~75% | 15–19 |
| **Satisfactory** | Lower quarter | 10–14 |

**Aim high:** synthetic-only + one-approach projects can pass the checklist but usually will **not** land in the top ranking tiers.

---

## Grading summary sheet

| Section | Max | Score |
| --- | --- | --- |
| 1. Title and team | 2 |  |
| 2. Problem and artifact | 7 |  |
| 3. Agent loop | 10 |  |
| 4. Why this family | 6 |  |
| 5. Dataset and tools | 8 |  |
| 6. Approaches combined | 6 |  |
| 7. Evaluation, results, own-words explanation | 15 |  |
| 8. Governance | 6 |  |
| 9. Live presentation | 5 |  |
| 10. Code / artifact quality | 5 |  |
| **Part A subtotal** | **70** |  |
| B1. Idea quality | 6 |  |
| B2. Effort / data / approaches | 6 |  |
| B3. Solution clarity | 6 |  |
| B4. Evaluation clarity | 6 |  |
| B5. Impact / presentation | 6 |  |
| **Part B ranking** | **30** |  |
| **TOTAL** | **100** |  |

Optional early **project proposal** (`Project-Proposal.md`) is feedback only unless Canvas scores it. State your planned **dataset tier** and **approach count** early.

---

## Late work

**10% per late day**. After **five days**, not accepted.

---

## Academic integrity

You may reuse agent code from an assigned lab. You may **not** turn in an AI-written report or evaluation as if your team wrote it. The results section especially must sound like you. If the assignment ever allows a tool for drafting, you must say how you used it. Submitting AI prose as your own work breaks the syllabus.

---

*DAT 5668 · Agentic AI: Autonomous Decision-Making · Salih Tutun, PhD*
