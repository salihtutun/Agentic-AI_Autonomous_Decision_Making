# DAT 5668 · Agentic AI: Autonomous Decision-Making

# Final Project Grading Rubric

Salih Tutun, PhD · 100 points · 30% of the course

Use this sheet with the filled `Report-Template.md`, the running notebook artifact, and the Session 13 talk (about 7 minutes). Families allowed: **LLM-based**, **RL-based**, or **hybrid**. A chatbot demo or a prediction-only model from DAT 5565 is not an agent. An ML or deep-learning model may be a **tool** the agent calls.

---

## What full credit looks like (quick view)

| Piece | Full credit |
| --- | --- |
| Loop | Observe, decide, act, and feedback are specific to this business process |
| Family | LLM, RL, or hybrid follows the work; who releases the action is clear |
| Evaluation | Running notebook, at least one baseline, full scorecard |
| Governance | Checkpoint, audit, privacy, buy vs build |
| Presentation | About 7 minutes; any member can answer who releases the action |

---

## Section 1 — Title and team (4 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Title | 2 | Names the business process, not only a model name |
| Team | 2 | All members listed; group of 1–3 |

**Deductions:** generic title (−1); missing member names (−1).

---

## Section 2 — Problem and artifact (12 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Business process | 4 | One real process the firm already runs |
| “Solved” metric | 4 | A number the firm already tracks |
| Reusable artifact | 4 | How someone runs this notebook again on a new day / ticket / feed |

**Deductions:** model-name-as-problem (−2); no KPI (−2); one-off demo with no reuse path (−2).

---

## Section 3 — Agent loop (15 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Observe | 4 | What state or inputs the agent sees |
| Decide | 4 | How the action is chosen (policy, prompt+tools, bandit, Q-table, hybrid handoff) |
| Act | 3 | What changes in the world or system |
| Feedback | 4 | Reward, penalty, correction, or next-state signal used to improve or audit |

Do not paste the Session 1 definition. Name course sessions only if it helps.

**Deductions:** missing any loop step (−2 each); copied textbook wording with no process specifics (−3).

---

## Section 4 — Why this family (12 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Family choice | 4 | LLM, RL, or hybrid stated |
| Work-based reason | 5 | Reason follows the process (documents/exceptions vs repeated numeric decision), not the model brand |
| Who releases the action | 3 | Which system (or person) releases the frequent action; hybrid must say the split |

**Deductions:** chatbot on a pure inventory quantity with no justification (−3); DQN on a contracts-only task with no justification (−3); hybrid with no split (−2).

---

## Section 5 — Data and tools (10 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Source | 4 | Simulated, public data, or free API ([public-apis](https://github.com/public-apis/public-apis)); never confidential employer files |
| Fit to process | 3 | Data/API clearly supports observe or act |
| Tool use (if any) | 3 | Fitted sklearn / XGBoost / DAT 5565 Keras model is a tool inside the loop, not the whole artifact |

**Deductions:** confidential data (−all of Section 5); prediction-only notebook (−4); undeclared API key committed to the file (−2).

---

## Section 6 — Evaluation against a baseline (25 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Running artifact | 6 | Notebook (or script) runs end-to-end |
| Baseline | 5 | Simple rule, fixed offer, chatbot, or heuristic named and run |
| Scorecard | 10 | Task success, cost, latency, safety/grounding, business KPI for agent and baseline |
| Deploy judgment | 4 | Would you deploy? What still fails? Losing to the baseline is acceptable if said clearly |

**Scorecard must appear in the report (and preferably print from the notebook):**

| Metric | Your agent | Baseline |
| --- | --- | --- |
| Task success |  |  |
| Cost |  |  |
| Latency |  |  |
| Safety or grounding |  |  |
| Business KPI |  |  |

**Deductions:** no baseline (−5); missing scorecard rows (−2 each); demo screenshots only, no run (−6).

---

## Section 7 — Governance (10 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Human checkpoint | 3 | When a person must approve or veto |
| Audit trail | 3 | What you store for later review |
| Privacy | 2 | What must not go into a public model |
| Buy vs build | 2 | Honest note on buy, build, or hybrid ownership |

**Deductions:** empty governance (−all of Section 7); privacy ignored when using a public LLM (−2).

---

## Section 8 — Live presentation (8 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Time and structure | 2 | About 7 minutes; loop → family → scorecard → governance |
| Substance | 3 | Problem, artifact, baseline result, and who releases are clear |
| Team ownership | 3 | Any member can answer which system releases the action |

Slides are optional. The notebook table plus one loop diagram is enough if the speaking is clear.

**Deductions:** over time without substance (−1); no member can answer who releases (−3).

---

## Section 9 — Code / artifact quality (4 points)

| Criteria | Points | Description |
| --- | --- | --- |
| Runs and is readable | 2 | Clear cells or modules; instructions to rerun |
| Honest limits | 2 | What was simulated, stubbed, or left for later |

---

## Grading summary

| Section | Max |
| --- | --- |
| 1. Title and team | 4 |
| 2. Problem and artifact | 12 |
| 3. Agent loop | 15 |
| 4. Why this family | 12 |
| 5. Data and tools | 10 |
| 6. Evaluation vs baseline | 25 |
| 7. Governance | 10 |
| 8. Live presentation | 8 |
| 9. Code / artifact quality | 4 |
| **Total** | **100** |

Optional early **project proposal** (see `Project-Proposal.md`) is feedback only unless Canvas lists it as a scored checkpoint. It does not replace the report or the notebook.

---

## Late work

Labs, homework, and the project lose **10% per late day**. After **five days** the work is not accepted.

---

## Academic integrity

Using agent code from an assigned lab is allowed. Using Copilot, ChatGPT, or a similar tool to write the report is not allowed unless the assignment says you may, and then you must cite how you used it. Submitting an AI-generated write-up as your own work violates the syllabus policy.

---

*DAT 5668 · Agentic AI: Autonomous Decision-Making · Salih Tutun, PhD*
