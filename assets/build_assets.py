"""Earlier matplotlib figures. Kept as a fallback.

The published PNGs come from assets/mermaid/*.mmd.
Redraw those with: python assets/render_mermaid.py
This script overwrites those PNGs only when passed --matplotlib.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent

NAVY = "#10243E"
BLUE = "#1F6FEB"
RED = "#C23B3B"
GREEN = "#1F7A4D"
GOLD = "#A6843D"
INK = "#10243E"
MUTED = "#5C6B7A"
PAPER = "#F7F9FC"
CARD = "#FFFFFF"


def new_ax(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=160)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    return fig, ax


def card(ax, x, y, w, h, face, edge=None, radius=0.12):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        facecolor=face,
        edgecolor=edge or face,
        linewidth=1.4,
        mutation_aspect=None,
    )
    ax.add_patch(patch)


def label(ax, x, y, text, size=12, color="white", weight="medium", ha="center", va="center"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontweight=weight, zorder=3)


def arrow(ax, start, end, color=NAVY):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.6,
            color=color,
            shrinkA=2,
            shrinkB=2,
        )
    )


def save(fig, name):
    path = OUT / name
    fig.savefig(path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(path.name)


def agent_loop():
    fig, ax = new_ax(12.2, 3.4)
    label(ax, 6.1, 3.05, "The agent loop", 16, INK, "semibold")
    steps = [
        (0.35, "Observe", "Read the situation", BLUE),
        (3.35, "Decide", "Pick the next action", NAVY),
        (6.35, "Act", "Change the world", RED),
        (9.35, "Feedback", "See what happened", GREEN),
    ]
    for x, title, subtitle, color in steps:
        card(ax, x, 0.85, 2.55, 1.55, color, radius=0.15)
        label(ax, x + 1.28, 1.85, title, 14, "white", "semibold")
        label(ax, x + 1.28, 1.35, subtitle, 10, "#E8EEF6")
    for x in (2.9, 5.9, 8.9):
        arrow(ax, (x, 1.62), (x + 0.45, 1.62))
    # Feedback returns to the next observation.
    arrow(ax, (10.6, 0.85), (1.6, 0.85), GOLD)
    label(ax, 6.1, 0.42, "The next observation uses this feedback", 10, MUTED)
    save(fig, "agent-loop.png")


def two_families():
    fig, ax = new_ax(12.2, 6.2)
    label(ax, 6.1, 5.85, "One loop, two agent families", 16, INK, "semibold")
    card(ax, 1.3, 4.55, 9.6, 0.85, NAVY, radius=0.12)
    label(ax, 6.1, 4.97, "Observe  →  Decide  →  Act  →  Feedback", 13, "white", "semibold")

    card(ax, 0.4, 0.45, 5.4, 3.7, CARD, BLUE, radius=0.14)
    card(ax, 0.4, 3.55, 5.4, 0.6, BLUE, radius=0.1)
    label(ax, 3.1, 3.85, "LLM-based agent", 13, "white", "semibold")
    lines = [
        "Input is language or a document",
        "Decide by calling a tool",
        "Act through search, CRM, or a ticket",
        "Feedback is a citation and a review",
        "Sessions 1 through 3",
    ]
    for i, line in enumerate(lines):
        label(ax, 0.7, 3.15 - i * 0.48, line, 11, INK, ha="left")

    card(ax, 6.4, 0.45, 5.4, 3.7, CARD, RED, radius=0.14)
    card(ax, 6.4, 3.55, 5.4, 0.6, RED, radius=0.1)
    label(ax, 9.1, 3.85, "RL-based agent", 13, "white", "semibold")
    lines = [
        "Input is a repeated numeric state",
        "Decide with a learned policy",
        "Act with an order, price, or trade",
        "Feedback is a reward",
        "Sessions 4 through 10",
    ]
    for i, line in enumerate(lines):
        label(ax, 6.7, 3.15 - i * 0.48, line, 11, INK, ha="left")
    save(fig, "two-families.png")


def llm_tools():
    fig, ax = new_ax(12.2, 4.6)
    label(ax, 6.1, 4.25, "LLM-based agent: tools, then a decision", 16, INK, "semibold")
    boxes = [
        (0.3, 1.7, "Ticket", "Language in", NAVY),
        (2.9, 1.7, "Model", "Choose a tool", BLUE),
        (5.5, 1.7, "Tools", "Policy and amount", "#245B8A"),
        (8.1, 1.7, "Memory", "Store the result", GOLD),
        (10.0, 0.35, "Finish", "Refund, refuse, escalate", RED),
    ]
    # Last box is lower so the loop can return.
    for x, y, title, subtitle, color in boxes[:4]:
        card(ax, x, y, 2.2, 1.35, color, radius=0.12)
        label(ax, x + 1.1, y + 0.82, title, 13, "white", "semibold")
        label(ax, x + 1.1, y + 0.42, subtitle, 9, "#F4F7FB")
    card(ax, 4.5, 0.25, 3.4, 1.05, RED, radius=0.12)
    label(ax, 6.2, 0.9, "Finish", 13, "white", "semibold")
    label(ax, 6.2, 0.5, "Refund, refuse, or escalate", 9, "#F4F7FB")
    arrow(ax, (2.5, 2.35), (2.9, 2.35))
    arrow(ax, (5.1, 2.35), (5.5, 2.35))
    arrow(ax, (7.7, 2.35), (8.1, 2.35))
    # Another tool call goes back to the model. A finished memory drops to the decision.
    arrow(ax, (9.2, 3.45), (4.0, 3.45), GOLD)
    label(ax, 6.6, 3.65, "call another tool", 9, MUTED)
    arrow(ax, (9.2, 1.7), (7.6, 1.3), GREEN)
    label(ax, 8.55, 1.28, "done", 9, GREEN)
    save(fig, "llm-tool-loop.png")


def rag_handoff():
    fig, ax = new_ax(12.2, 4.2)
    label(ax, 6.1, 3.9, "LLM-based handoff: retrieve, then check the citation", 15, INK, "semibold")
    roles = [
        (0.35, "Question", NAVY),
        (2.85, "Chunks", BLUE),
        (5.35, "Researcher", "#245B8A"),
        (7.85, "Analyst", GOLD),
        (10.15, "Reviewer", RED),
    ]
    for x, title, color in roles:
        card(ax, x, 1.7, 2.15, 1.2, color, radius=0.12)
        label(ax, x + 1.07, 2.3, title, 12, "white", "semibold")
    for x in (2.5, 5.0, 7.5, 10.0):
        arrow(ax, (x, 2.3), (x + 0.35, 2.3))
    label(ax, 6.1, 1.15, "The reviewer releases the answer only when the citation is in the corpus.", 11, MUTED)
    label(ax, 6.1, 0.6, "A missing citation stops the handoff.", 11, RED)
    save(fig, "rag-handoff.png")


def bandit():
    fig, ax = new_ax(12.2, 4.4)
    label(ax, 6.1, 4.05, "RL-based agent: a bandit sees one reward", 16, INK, "semibold")
    offers = [("A", "0.20", BLUE), ("B", "0.55", RED), ("C", "0.35", "#245B8A")]
    for i, (name, rate, color) in enumerate(offers):
        x = 0.6 + i * 2.5
        card(ax, x, 1.55, 2.1, 1.7, color, radius=0.12)
        label(ax, x + 1.05, 2.65, f"Offer {name}", 14, "white", "semibold")
        label(ax, x + 1.05, 2.1, f"true rate {rate}", 10, "#F4F7FB")
    card(ax, 8.3, 1.55, 3.4, 1.7, NAVY, radius=0.12)
    label(ax, 10.0, 2.7, "Agent", 14, "white", "semibold")
    label(ax, 10.0, 2.15, "Picks one offer", 11, "#F4F7FB")
    label(ax, 10.0, 1.75, "Others stay hidden", 10, "#F4F7FB")
    arrow(ax, (7.6, 2.4), (8.3, 2.4))
    label(ax, 6.1, 0.7, "Explore to learn the rates. Exploit to collect from the current best.", 11, MUTED)
    save(fig, "bandit.png")


def mdp_inventory():
    fig, ax = new_ax(12.2, 4.3)
    label(ax, 6.1, 3.95, "RL-based agent: inventory as a Markov decision process", 15, INK, "semibold")
    nodes = [
        (0.3, "State", "Stock on hand", BLUE),
        (3.2, "Action", "Order 0, 1, or 2", NAVY),
        (6.1, "Demand", "Random, then sales", GOLD),
        (9.0, "Next state", "Ending stock + reward", RED),
    ]
    for x, title, subtitle, color in nodes:
        card(ax, x, 1.55, 2.7, 1.45, color, radius=0.12)
        label(ax, x + 1.35, 2.45, title, 13, "white", "semibold")
        label(ax, x + 1.35, 1.95, subtitle, 9, "#F4F7FB")
    arrow(ax, (3.0, 2.25), (3.2, 2.25))
    arrow(ax, (5.9, 2.25), (6.1, 2.25))
    arrow(ax, (8.8, 2.25), (9.0, 2.25))
    label(ax, 6.1, 0.75, "Reward = margin on sales − holding cost − stockout penalty", 11, INK)
    save(fig, "mdp-inventory.png")


def bellman():
    fig, ax = new_ax(12.2, 3.8)
    label(ax, 6.1, 3.45, "Value backup when the demand model is known", 15, INK, "semibold")
    card(ax, 0.4, 1.2, 3.3, 1.5, BLUE, radius=0.12)
    label(ax, 2.05, 2.15, "V(stock)", 14, "white", "semibold")
    label(ax, 2.05, 1.65, "Value of this state", 10, "#F4F7FB")
    card(ax, 4.5, 1.2, 3.4, 1.5, NAVY, radius=0.12)
    label(ax, 6.2, 2.2, "Backup", 14, "white", "semibold")
    label(ax, 6.2, 1.65, "Average over demand", 10, "#F4F7FB")
    card(ax, 8.7, 1.2, 3.1, 1.5, GREEN, radius=0.12)
    label(ax, 10.25, 2.15, "Best order", 14, "white", "semibold")
    label(ax, 10.25, 1.65, "Max over actions", 10, "#F4F7FB")
    arrow(ax, (3.7, 1.95), (4.5, 1.95))
    arrow(ax, (7.9, 1.95), (8.7, 1.95))
    label(ax, 6.1, 0.55, "Dynamic programming needs those probabilities. Q-learning does not.", 11, MUTED)
    save(fig, "bellman.png")


def q_update():
    fig, ax = new_ax(12.2, 3.6)
    label(ax, 6.1, 3.25, "Q-learning fills the decide step of an RL-based agent", 15, INK, "semibold")
    card(ax, 0.45, 1.15, 11.3, 1.45, NAVY, radius=0.12)
    label(ax, 6.1, 2.15, "Q(state, action)  moves toward  reward + γ · best Q(next state)", 13, "white", "semibold")
    label(ax, 6.1, 1.55, "ε-greedy sometimes tries a random order so the table keeps learning", 11, "#D5E4F7")
    label(ax, 6.1, 0.5, "This is the same decide box an LLM-based agent fills with a tool call.", 11, MUTED)
    save(fig, "q-update.png")


def dqn():
    fig, ax = new_ax(12.2, 4.5)
    label(ax, 6.1, 4.15, "Deep Q-network: a shared guess instead of a table", 15, INK, "semibold")
    card(ax, 0.35, 1.7, 2.5, 1.5, BLUE, radius=0.12)
    label(ax, 1.6, 2.65, "State", 13, "white", "semibold")
    label(ax, 1.6, 2.15, "Stock and demand", 9, "#F4F7FB")
    card(ax, 3.5, 1.7, 2.7, 1.5, NAVY, radius=0.12)
    label(ax, 4.85, 2.65, "Network", 13, "white", "semibold")
    label(ax, 4.85, 2.15, "Q for each order", 9, "#F4F7FB")
    card(ax, 6.85, 1.7, 2.4, 1.5, RED, radius=0.12)
    label(ax, 8.05, 2.65, "Replay", 13, "white", "semibold")
    label(ax, 8.05, 2.15, "Past days, mixed", 9, "#F4F7FB")
    card(ax, 9.85, 1.7, 2.0, 1.5, GREEN, radius=0.12)
    label(ax, 10.85, 2.65, "Target", 13, "white", "semibold")
    label(ax, 10.85, 2.15, "Held still", 9, "#F4F7FB")
    arrow(ax, (2.85, 2.45), (3.5, 2.45))
    arrow(ax, (6.2, 2.45), (6.85, 2.45))
    arrow(ax, (9.25, 2.45), (9.85, 2.45))
    label(ax, 6.1, 0.85, "Train in a simulator. A live bad order hits real stock.", 12, INK)
    save(fig, "dqn.png")


def hybrid():
    fig, ax = new_ax(12.2, 4.4)
    label(ax, 6.1, 4.05, "Hybrid: each family owns a different step", 16, INK, "semibold")
    card(ax, 0.3, 1.55, 3.4, 1.6, BLUE, radius=0.12)
    label(ax, 2.0, 2.6, "LLM-based agent", 12, "white", "semibold")
    label(ax, 2.0, 2.1, "Reads the exception email", 9, "#F4F7FB")
    label(ax, 2.0, 1.75, "Proposes an override", 9, "#F4F7FB")
    card(ax, 4.4, 1.55, 3.3, 1.6, GOLD, radius=0.12)
    label(ax, 6.05, 2.6, "Controller", 12, "white", "semibold")
    label(ax, 6.05, 2.1, "A person or a hard rule", 9, "#F4F7FB")
    label(ax, 6.05, 1.75, "Can veto", 9, "#F4F7FB")
    card(ax, 8.4, 1.55, 3.45, 1.6, RED, radius=0.12)
    label(ax, 10.1, 2.6, "RL-based agent", 12, "white", "semibold")
    label(ax, 10.1, 2.1, "Releases the daily order", 9, "#F4F7FB")
    label(ax, 10.1, 1.75, "Fast path, no language", 9, "#F4F7FB")
    arrow(ax, (3.7, 2.35), (4.4, 2.35))
    arrow(ax, (7.7, 2.35), (8.4, 2.35))
    label(ax, 6.1, 0.7, "The system that releases the order owns the KPI.", 12, INK)
    save(fig, "hybrid.png")


def scorecard():
    fig, ax = new_ax(12.2, 4.6)
    label(ax, 6.1, 4.25, "One scorecard for both families", 16, INK, "semibold")
    columns = ["Metric", "LLM-based agent", "RL-based agent"]
    rows = [
        ["Task success", "Exceptions handled cleanly", "Days the order was right"],
        ["Cost", "Model and tool calls", "Training and compute"],
        ["Latency", "Seconds, often slow", "A fast policy"],
        ["Safety", "Inside policy", "Inside capacity and vetoes"],
        ["Grounding", "Citation is real", "Not a document task"],
        ["Business KPI", "Same stockout or service number for both", ""],
    ]
    colors = [NAVY, BLUE, RED]
    xs = [0.35, 3.15, 7.55]
    widths = [2.7, 4.3, 4.3]
    for x, w, title, color in zip(xs, widths, columns, colors):
        card(ax, x, 3.35, w, 0.55, color, radius=0.08)
        label(ax, x + w / 2, 3.62, title, 11, "white", "semibold")
    for i, row in enumerate(rows):
        y = 2.75 - i * 0.42
        for x, w, text, col in zip(xs, widths, row, range(3)):
            if not text:
                continue
            face = "#E7EEF8" if i % 2 == 0 else CARD
            span = 8.7 if col == 1 and row[2] == "" else w
            if col == 2 and text == "":
                continue
            card(ax, x, y, span, 0.38, face, "#D5DEE8", radius=0.04)
            label(ax, x + 0.12, y + 0.19, text, 9, INK, ha="left")
    save(fig, "scorecard.png")


def main():
    agent_loop()
    two_families()
    llm_tools()
    rag_handoff()
    bandit()
    mdp_inventory()
    bellman()
    q_update()
    dqn()
    hybrid()
    scorecard()


if __name__ == "__main__":
    if "--matplotlib" not in sys.argv:
        raise SystemExit(
            "Published figures are Mermaid diagrams. "
            "Run python assets/render_mermaid.py. "
            "Pass --matplotlib only to restore the older drawings."
        )
    main()
