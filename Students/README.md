# DAT 5668 — Student files

Agentic AI: Autonomous Decision-Making. Fall 2026.

Use this folder only. It does not contain quiz answers or solution notebooks.

## Each session

The course has 13 sessions. We meet twice a week. Session 1 is the first meeting.

1. Come to the session. The concepts are taught in the room. There are no lecture recordings.
2. Submit the pre-lab quiz in `Quizzes/` at least one hour before the practice session of that module (Sessions 2, 4, 6, 8, 10, and 12). The quiz covers the concept session you just had. A late quiz is not accepted except with an excused absence.
3. Open that session's notebook. Run the worked example, then type the cells marked **Fill this with me** while the instructor is teaching. Guess before you run.
4. On the practice sessions (2, 4, 6, 8, 10, and 12), finish every `TODO` in class. Groups may be 1–3 students.
5. After each practice session, complete that module's file in `Homework/`. Homework is individual unless the instructor says otherwise.

Session 13 is the project meeting. Use `07-Module-7-Project/Session-13.ipynb`.

## What to submit

| Work | Share of the grade | Where it lives |
| --- | --- | --- |
| Lab participation | 5% | In class |
| Quizzes (lowest score dropped) | 30% | `Quizzes/` |
| In-class practice | 15% | Sessions 2, 4, 6, 8, 10, and 12 |
| Homework | 20% | `Homework/` |
| Project | 30% | `07-Module-7-Project/` |

Canvas takes 10% off for each late day on labs, homework, and the project. After five days the work is not accepted. Quizzes due before the practice session are not in that late window.

## How to run the notebooks

Google Colab or local Python with NumPy. Run cells from the top. The examples are simulated course cases, not data from a firm. Do not paste confidential data into a public tool. Session 1 decides with a local stand-in. If the instructor sets `GEMINI_API_KEY` for that session, the same step can ask Gemini which tool to call. Class still runs when the key is absent.

## Use of AI tools

Using the agent code in an assigned lab is allowed. Using Copilot, ChatGPT, or a similar tool to write your quiz, your homework write-up, or your project report is not allowed unless that assignment says you may, and then you must cite how you used it. Submitting an AI-generated write-up as your own work is a violation of the academic integrity policy in the syllabus.

## Two families

Read `Two-Agent-Families.md` before Session 1. Every session is labeled **LLM-based agent**, **RL-based agent**, or **both**. Figures for those sessions are in the course `assets/` folder, one level above `Students/`. Open the notebooks from this project so the pictures resolve.

## Schedule

| Session | Topic | Family | Homework |
| --- | --- | --- | --- |
| 1 | Agent loop | Both | |
| 2 | Tool-using agent | LLM-based | Refund cap |
| 3 | RAG and handoffs | LLM-based | |
| 4 | Bandits | RL-based | A fourth offer |
| 5 | Inventory MDP | RL-based | |
| 6 | Go/no-go memo | Both | Pricing memo |
| 7 | Bellman, DP, MC, TD | RL-based | |
| 8 | Q-learning | RL-based | Reward diagnostic |
| 9 | Deep Q-learning concepts | RL-based | |
| 10 | DQN vs base-stock | RL-based | Exploration diagnostic |
| 11 | Hybrid architecture | Both | |
| 12 | Scorecard and governance | Both | A second pilot |
| 13 | Project presentations | LLM-based, RL-based, or hybrid | Report |
