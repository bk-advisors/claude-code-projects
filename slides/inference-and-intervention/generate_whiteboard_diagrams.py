"""
Generate whiteboard summary diagrams for each chapter of
"Inference and Intervention" — one PNG per chapter.

Output: whiteboard-diagrams/ch01-whiteboard.png … ch10-whiteboard.png
Style: hand-drawn (xkcd), BKA brand colours, no axes/grids.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# ── Shared constants ──────────────────────────────────────────────────────────

OUT_DIR = os.path.join(os.path.dirname(__file__), "whiteboard-diagrams")
DPI = 150
FIG_W, FIG_H = 10, 7

# BKA brand colours
BLUE    = "#005CB9"
LBLUE   = "#00A1DF"
GREEN   = "#83BD00"
TEAL    = "#3E9B6E"
RED     = "#E24A3F"
ORANGE  = "#FA7650"
AMBER   = "#F8A623"
YELLOW  = "#FED141"
DARK    = "#333333"
GRAY    = "#888888"
LGRAY   = "#CCCCCC"

FONT = {"family": "sans-serif", "weight": "bold"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def new_fig(title=""):
    """Create a clean figure with no axes."""
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.text(5, 6.6, title, ha="center", va="top",
                fontsize=18, fontweight="bold", color=BLUE, fontfamily="sans-serif")
    return fig, ax


def circled_num(ax, x, y, n, color=BLUE, r=0.22, fontsize=13):
    """Draw a circled number at (x, y)."""
    c = Circle((x, y), r, fill=False, edgecolor=color, linewidth=2)
    ax.add_patch(c)
    ax.text(x, y, str(n), ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=color, fontfamily="sans-serif")


def rounded_box(ax, x, y, w, h, text, fc="white", ec=BLUE, lw=2, fontsize=11, textcolor=DARK):
    """Draw a rounded rectangle with centred text."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.1", facecolor=fc, edgecolor=ec, linewidth=lw)
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=textcolor, fontfamily="sans-serif",
            wrap=True)


def arrow(ax, x1, y1, x2, y2, color=DARK, lw=2, style="->"):
    """Draw an arrow between two points."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw))


def dag_node(ax, x, y, label, color=BLUE, r=0.35, fontsize=10):
    """Draw a circular DAG node."""
    c = Circle((x, y), r, fill=True, facecolor="white", edgecolor=color, linewidth=2.5)
    ax.add_patch(c)
    ax.text(x, y, label, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=DARK, fontfamily="sans-serif")


def save(fig, name):
    fig.savefig(os.path.join(OUT_DIR, name), dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — Causal Model as Foundation
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch01():
    fig, ax = new_fig("Ch 1 — Causal Model as Foundation")

    # Foundation bar
    bar = FancyBboxPatch((1.5, 0.6), 7, 0.9,
                         boxstyle="round,pad=0.15", facecolor=BLUE, edgecolor=BLUE, linewidth=2)
    ax.add_patch(bar)
    t = ax.text(5, 1.05, "CAUSAL  MODEL", ha="center", va="center",
                fontsize=16, fontweight="bold", color="white", fontfamily="sans-serif")
    t.set_path_effects([])

    # Two zones
    rounded_box(ax, 3, 5.0, 3.2, 1.6, "Situational\nAssessment", fc="#E8F0FE", ec=BLUE)
    ax.text(3, 4.0, "What is happening?", ha="center", va="center",
            fontsize=9, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    rounded_box(ax, 7, 5.0, 3.2, 1.6, "Managerial\nIntervention", fc="#E8F8E8", ec=GREEN)
    ax.text(7, 4.0, "What should we do?", ha="center", va="center",
            fontsize=9, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Upward arrows from foundation to zones
    arrow(ax, 3, 1.6, 3, 3.9, color=BLUE, lw=2.5, style="-|>")
    arrow(ax, 7, 1.6, 7, 3.9, color=GREEN, lw=2.5, style="-|>")

    # Three traps in red
    traps = [("Confounding", 2.3), ("Reverse\nCausation", 5.0), ("Selection\nBias", 7.7)]
    for i, (label, xpos) in enumerate(traps):
        circled_num(ax, xpos, 2.7, i + 1, color=RED)
        ax.text(xpos, 2.2, label, ha="center", va="center",
                fontsize=9, fontweight="bold", color=RED, fontfamily="sans-serif")

    ax.text(5, 3.25, "Traps you fall into without the foundation",
            ha="center", va="center", fontsize=8, fontstyle="italic", color=GRAY,
            fontfamily="sans-serif")

    save(fig, "ch01-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — Three Triplet Structures
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch02():
    fig, ax = new_fig("Ch 2 — Three Triplet Structures")

    structures = [
        {"name": "CHAIN (Serial)", "nodes": ["A", "B", "C"],
         "arrows": [(0, 1), (1, 2)], "rule": "Condition on B: BLOCKS", "x_off": 1.5, "color": BLUE},
        {"name": "FORK (Diverging)", "nodes": ["A", "B", "C"],
         "arrows": [(1, 0), (1, 2)], "rule": "Condition on B: BLOCKS", "x_off": 5.0, "color": TEAL},
        {"name": "COLLIDER (Converging)", "nodes": ["A", "B", "C"],
         "arrows": [(0, 1), (2, 1)], "rule": "Condition on B: OPENS!", "x_off": 8.5, "color": RED},
    ]

    for s in structures:
        xc = s["x_off"]
        y_top = 4.8
        r = 0.3
        positions = [(xc - 1.1, y_top), (xc, y_top - 1.4), (xc + 1.1, y_top)]

        # Title
        ax.text(xc, 5.8, s["name"], ha="center", va="center",
                fontsize=11, fontweight="bold", color=s["color"], fontfamily="sans-serif")

        # Nodes
        for i, (nx, ny) in enumerate(positions):
            fc = AMBER if i == 1 else "white"
            ec = s["color"]
            c = Circle((nx, ny), r, fill=True, facecolor=fc, edgecolor=ec, linewidth=2.5)
            ax.add_patch(c)
            ax.text(nx, ny, s["nodes"][i], ha="center", va="center",
                    fontsize=12, fontweight="bold", color=DARK, fontfamily="sans-serif")

        # Arrows
        for (frm, to) in s["arrows"]:
            x1, y1 = positions[frm]
            x2, y2 = positions[to]
            dx = x2 - x1
            dy = y2 - y1
            dist = np.sqrt(dx**2 + dy**2)
            # shorten by node radius
            x1s = x1 + (r + 0.05) * dx / dist
            y1s = y1 + (r + 0.05) * dy / dist
            x2s = x2 - (r + 0.05) * dx / dist
            y2s = y2 - (r + 0.05) * dy / dist
            arrow(ax, x1s, y1s, x2s, y2s, color=s["color"], lw=2)

        # Rule text
        rule_color = RED if "OPENS" in s["rule"] else TEAL
        ax.text(xc, 2.4, s["rule"], ha="center", va="center",
                fontsize=9, fontweight="bold", color=rule_color, fontfamily="sans-serif",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9E6" if "OPENS" in s["rule"] else "#F0F8F0",
                          edgecolor=rule_color, linewidth=1.5))

    # Bottom summary
    ax.text(5, 1.2, "These three structures govern ALL information flow",
            ha="center", va="center", fontsize=12, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=2))

    # Node type legend
    ax.text(0.3, 0.5, "Node types:", fontsize=8, fontweight="bold", color=GRAY,
            fontfamily="sans-serif")
    legend_items = [("Oval = Probabilistic", BLUE), ("Rect = Decision", ORANGE),
                    ("Hex = Objective", TEAL), ("Chev = Function", GRAY)]
    for i, (label, col) in enumerate(legend_items):
        ax.text(0.3 + i * 2.5, 0.15, label, fontsize=7, color=col,
                fontfamily="sans-serif")

    save(fig, "ch02-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Iterative Model Building
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch03():
    fig, ax = new_fig("Ch 3 — Iterative Model Building")

    cx, cy = 5, 3.5

    # Three concentric rings
    rings = [
        (1.0, BLUE, "Round 1", "4 nodes", "MOH Director\nSupply side"),
        (1.9, TEAL, "Round 2", "8 nodes", "Facility Directors\nTransmission failures"),
        (2.8, GREEN, "Round 3", "12+ nodes", "Community Health Workers\nDemand side"),
    ]

    for r, color, rlabel, nlabel, desc in rings:
        ring = Circle((cx, cy), r, fill=False, edgecolor=color, linewidth=2.5, linestyle="--")
        ax.add_patch(ring)

    # Ring labels (right side)
    for i, (r, color, rlabel, nlabel, desc) in enumerate(rings):
        circled_num(ax, cx + r + 0.35, cy + 0.4, i + 1, color=color, r=0.2, fontsize=11)
        ax.text(cx + r + 0.35, cy - 0.05, rlabel, ha="center", va="top",
                fontsize=9, fontweight="bold", color=color, fontfamily="sans-serif")

    # Ring descriptions (left side for 1 & 2, bottom for 3)
    descs = [
        (cx - 1.6, cy + 1.4, rings[0][4], rings[0][1]),
        (cx - 2.8, cy - 0.5, rings[1][4], rings[1][1]),
        (cx - 0.2, cy - 3.3, rings[2][4], rings[2][1]),
    ]
    for dx, dy, txt, col in descs:
        ax.text(dx, dy, txt, ha="center", va="center",
                fontsize=9, fontstyle="italic", color=col, fontfamily="sans-serif")

    # Central "Core DAG" node
    core = Circle((cx, cy), 0.4, fill=True, facecolor=BLUE, edgecolor=BLUE, linewidth=2)
    ax.add_patch(core)
    t = ax.text(cx, cy, "Core\nDAG", ha="center", va="center",
                fontsize=8, fontweight="bold", color="white", fontfamily="sans-serif")
    t.set_path_effects([])

    # Curved arrows between rings
    for i in range(2):
        r1 = rings[i][0]
        r2 = rings[i + 1][0]
        mid_r = (r1 + r2) / 2
        # arc on top
        theta = np.radians(60)
        x1 = cx + r1 * np.cos(theta)
        y1 = cy + r1 * np.sin(theta)
        x2 = cx + r2 * np.cos(theta)
        y2 = cy + r2 * np.sin(theta)
        arrow(ax, x1, y1, x2, y2, color=AMBER, lw=2, style="-|>")
        ax.text(cx + mid_r * np.cos(theta) - 0.1, cy + mid_r * np.sin(theta) + 0.25,
                "What's\nmissing?", ha="center", va="center",
                fontsize=7, fontstyle="italic", color=AMBER, fontfamily="sans-serif")

    # Bottom annotation
    ax.text(5, 0.3, "Each round reveals what the previous one missed",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=1.5))

    save(fig, "ch03-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — From Beliefs to Numbers
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch04():
    fig, ax = new_fig("Ch 4 — From Beliefs to Numbers")

    steps = [
        ("Probability\nP(X)", BLUE),
        ("Conditional\nProbability\nP(X|Y)", LBLUE),
        ("CPTs", TEAL),
        ("Bayes'\nRule", GREEN),
        ("Bayesian\nNetwork", AMBER),
    ]

    x_start = 0.8
    x_gap = 1.9
    y_base = 1.5
    step_h = 0.8  # height increment per step

    for i, (label, color) in enumerate(steps):
        x = x_start + i * x_gap
        y = y_base + i * step_h
        w = 1.5
        h = 1.1

        # Step box
        rounded_box(ax, x, y, w, h, "", fc="white", ec=color, lw=2.5)

        # Circled number
        circled_num(ax, x - w/2 + 0.25, y + h/2 - 0.15, i + 1, color=color, r=0.18, fontsize=10)

        # Label
        ax.text(x, y - 0.1, label, ha="center", va="center",
                fontsize=9, fontweight="bold", color=DARK, fontfamily="sans-serif")

        # Arrow to next step
        if i < len(steps) - 1:
            x2 = x_start + (i + 1) * x_gap
            y2 = y_base + (i + 1) * step_h
            arrow(ax, x + w/2 + 0.05, y + 0.2, x2 - w/2 - 0.05, y2 - 0.2,
                  color=DARK, lw=2, style="-|>")

    # Bridge between steps 4 and 5
    bx1 = x_start + 3 * x_gap + 0.75
    bx2 = x_start + 4 * x_gap - 0.75
    by = y_base + 3.5 * step_h + 0.8
    ax.plot([bx1, bx2], [by, by], color=RED, lw=3, linestyle="-")
    ax.text((bx1 + bx2) / 2, by + 0.25, "Causal Markov\nCondition", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=RED, fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#FEECEB", edgecolor=RED, linewidth=1.5))

    # Braces / labels
    ax.text(4.2, 0.6, "Mathematics", ha="center", va="center",
            fontsize=10, fontweight="bold", color=GRAY, fontfamily="sans-serif")
    ax.plot([0.8, 7.4], [0.85, 0.85], color=GRAY, lw=1.5)

    ax.text(8.4, 0.6, "Model +\nNumbers", ha="center", va="center",
            fontsize=10, fontweight="bold", color=AMBER, fontfamily="sans-serif")
    ax.plot([7.8, 9.2], [0.85, 0.85], color=AMBER, lw=1.5)

    save(fig, "ch04-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Forward & Backward Reasoning
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch05():
    fig, ax = new_fig("Ch 5 — Forward & Backward Reasoning")

    # Central DAG nodes
    cx = 5
    nodes = [
        (cx - 1.2, 4.8, "Staffing", BLUE),
        (cx + 1.2, 4.8, "Equipment", BLUE),
        (cx, 3.2, "Quality", TEAL),
        (cx, 1.6, "NMR", RED),
    ]

    for nx, ny, label, color in nodes:
        dag_node(ax, nx, ny, label, color=color, r=0.45, fontsize=9)

    # DAG arrows
    dag_arrows = [(0, 2), (1, 2), (2, 3)]
    for frm, to in dag_arrows:
        x1, y1 = nodes[frm][0], nodes[frm][1]
        x2, y2 = nodes[to][0], nodes[to][1]
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        r = 0.5
        arrow(ax, x1 + r * dx/dist, y1 + r * dy/dist,
              x2 - r * dx/dist, y2 - r * dy/dist,
              color=DARK, lw=2.5, style="-|>")

    # Forward arrow (left)
    ax.annotate("", xy=(1.5, 1.5), xytext=(1.5, 5.2),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=3.5))
    ax.text(1.0, 3.3, "FORWARD\nPredict", ha="center", va="center",
            fontsize=11, fontweight="bold", color=BLUE, fontfamily="sans-serif",
            rotation=90)
    ax.text(0.2, 3.3, "Given causes,\nwhat outcomes\ndo we expect?", ha="center", va="center",
            fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Backward arrow (right)
    ax.annotate("", xy=(8.5, 5.2), xytext=(8.5, 1.5),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=3.5))
    ax.text(9.0, 3.3, "BACKWARD\nDiagnose", ha="center", va="center",
            fontsize=11, fontweight="bold", color=ORANGE, fontfamily="sans-serif",
            rotation=270)
    ax.text(9.8, 3.3, "Given outcomes,\nwhat causes\nare most likely?", ha="center", va="center",
            fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Explaining away callout (bottom right)
    ea_box = FancyBboxPatch((6.5, 0.3), 3.2, 1.0,
                            boxstyle="round,pad=0.15", facecolor="#FFF3E6", edgecolor=AMBER, linewidth=2)
    ax.add_patch(ea_box)
    ax.text(8.1, 0.8, "Explaining Away\nConfirming one cause\nreduces belief in the other",
            ha="center", va="center", fontsize=8, fontweight="bold", color=DARK,
            fontfamily="sans-serif")

    save(fig, "ch05-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Simpson's Paradox
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch06():
    fig, ax = new_fig("Ch 6 — Simpson's Paradox")

    # ── LEFT panel: aggregate bar chart (wrong) ──
    ax.text(1.5, 5.5, "AGGREGATED", ha="center", fontsize=11,
            fontweight="bold", color=RED, fontfamily="sans-serif")

    # Simple bar sketch
    bars_x = [0.8, 1.6]
    bars_h = [3.5, 4.5]
    colors = [LBLUE, TEAL]
    labels = ["Ctrl", "Tx"]
    for bx, bh, bc, bl in zip(bars_x, bars_h, colors, labels):
        ax.bar(bx, bh, width=0.55, bottom=1.0, color=bc, edgecolor=DARK, linewidth=1.5, alpha=0.7)
        ax.text(bx, 0.7, bl, ha="center", fontsize=8, color=DARK, fontfamily="sans-serif")

    # Red X
    ax.text(1.5, 4.0, "X", ha="center", va="center",
            fontsize=40, fontweight="bold", color=RED, alpha=0.5, fontfamily="sans-serif")
    ax.text(1.5, 0.3, "Wrong answer!", ha="center", fontsize=8,
            fontweight="bold", color=RED, fontfamily="sans-serif")

    # ── CENTER: two DAGs ──
    ax.text(5, 5.5, "WHY?", ha="center", fontsize=12,
            fontweight="bold", color=DARK, fontfamily="sans-serif")

    # Confounder DAG (top)
    ax.text(5, 4.9, "Confounder (common cause)", ha="center", fontsize=9,
            fontweight="bold", color=TEAL, fontfamily="sans-serif")
    dag_node(ax, 5, 4.3, "C", color=AMBER, r=0.28, fontsize=10)
    dag_node(ax, 4, 3.5, "Tx", color=BLUE, r=0.28, fontsize=9)
    dag_node(ax, 6, 3.5, "Y", color=TEAL, r=0.28, fontsize=10)
    arrow(ax, 4.75, 4.15, 4.25, 3.7, color=AMBER, lw=2)
    arrow(ax, 5.25, 4.15, 5.75, 3.7, color=AMBER, lw=2)
    ax.text(6.7, 4.3, "Adjust!", ha="left", fontsize=10,
            fontweight="bold", color=GREEN, fontfamily="sans-serif")

    # Mediator DAG (bottom)
    ax.text(5, 2.5, "Mediator (on the pathway)", ha="center", fontsize=9,
            fontweight="bold", color=ORANGE, fontfamily="sans-serif")
    dag_node(ax, 3.8, 1.8, "Tx", color=BLUE, r=0.28, fontsize=9)
    dag_node(ax, 5, 1.8, "M", color=ORANGE, r=0.28, fontsize=10)
    dag_node(ax, 6.2, 1.8, "Y", color=TEAL, r=0.28, fontsize=10)
    arrow(ax, 4.1, 1.8, 4.7, 1.8, color=DARK, lw=2)
    arrow(ax, 5.3, 1.8, 5.9, 1.8, color=DARK, lw=2)
    ax.text(6.7, 1.8, "Don't adjust!", ha="left", fontsize=10,
            fontweight="bold", color=RED, fontfamily="sans-serif")

    # ── RIGHT panel: stratified bar charts (correct) ──
    ax.text(8.8, 5.5, "STRATIFIED", ha="center", fontsize=11,
            fontweight="bold", color=GREEN, fontfamily="sans-serif")

    # Stratum 1
    ax.text(8.8, 5.0, "High severity", ha="center", fontsize=7,
            color=GRAY, fontfamily="sans-serif")
    ax.bar(8.3, 2.5, width=0.4, bottom=3.2, color=LBLUE, edgecolor=DARK, linewidth=1, alpha=0.7)
    ax.bar(8.8, 3.2, width=0.4, bottom=3.2, color=TEAL, edgecolor=DARK, linewidth=1, alpha=0.7)

    # Stratum 2
    ax.text(8.8, 2.8, "Low severity", ha="center", fontsize=7,
            color=GRAY, fontfamily="sans-serif")
    ax.bar(8.3, 1.5, width=0.4, bottom=1.0, color=LBLUE, edgecolor=DARK, linewidth=1, alpha=0.7)
    ax.bar(8.8, 2.0, width=0.4, bottom=1.0, color=TEAL, edgecolor=DARK, linewidth=1, alpha=0.7)

    # Green checkmark
    ax.text(9.5, 3.5, u"\u2713", ha="center", va="center",
            fontsize=36, fontweight="bold", color=GREEN, fontfamily="sans-serif")
    ax.text(8.8, 0.3, "Right answer!", ha="center", fontsize=8,
            fontweight="bold", color=GREEN, fontfamily="sans-serif")

    # Bottom rule
    ax.text(5, 0.3, "The DAG tells you which one it is",
            ha="center", fontsize=11, fontweight="bold", color=BLUE, fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=2))

    save(fig, "ch06-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — Observe vs Intervene (Graph Surgery)
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch07():
    fig, ax = new_fig("Ch 7 — Observe vs Intervene")

    # ── TOP panel: Observe ──
    ax.text(5, 5.8, "OBSERVE   P(Y | X = x)", ha="center", fontsize=12,
            fontweight="bold", color=BLUE, fontfamily="sans-serif")

    # Nodes
    top_y = 4.9
    obs_nodes = [
        (2.5, top_y, "Capacity\n(Chance)", BLUE, "o"),
        (5, top_y, "Intervention\n(Decision)", ORANGE, "s"),
        (7.5, top_y, "Lives Saved\n(Objective)", TEAL, "h"),
    ]

    for nx, ny, label, color, shape in obs_nodes:
        if shape == "s":  # rectangle
            rounded_box(ax, nx, ny, 1.6, 0.8, label, fc="white", ec=color, lw=2.5, fontsize=8)
        elif shape == "h":  # hexagon
            hex_patch = mpatches.RegularPolygon((nx, ny), 6, radius=0.55,
                                                facecolor="white", edgecolor=color, linewidth=2.5)
            ax.add_patch(hex_patch)
            ax.text(nx, ny, label, ha="center", va="center",
                    fontsize=7, fontweight="bold", color=DARK, fontfamily="sans-serif")
        else:  # oval
            dag_node(ax, nx, ny, label, color=color, r=0.55, fontsize=7)

    # All arrows intact (observe)
    arrow(ax, 3.1, top_y, 4.15, top_y, color=DARK, lw=2.5)   # Capacity -> Decision
    arrow(ax, 5.85, top_y, 6.9, top_y, color=DARK, lw=2.5)   # Decision -> Lives
    arrow(ax, 3.0, top_y - 0.45, 6.95, top_y - 0.45, color=GRAY, lw=1.5, style="-|>")  # Capacity -> Lives (direct)

    # ── BOTTOM panel: Intervene ──
    ax.text(5, 3.1, "INTERVENE   P(Y | do(X = x))", ha="center", fontsize=12,
            fontweight="bold", color=RED, fontfamily="sans-serif")
    ax.text(5, 2.7, "Graph Surgery: cut arrows INTO the decision node",
            ha="center", fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    bot_y = 1.8
    for nx, ny_orig, label, color, shape in obs_nodes:
        ny = bot_y
        if shape == "s":
            rounded_box(ax, nx, ny, 1.6, 0.8, label, fc="#FFF3E6", ec=ORANGE, lw=2.5, fontsize=8)
        elif shape == "h":
            hex_patch = mpatches.RegularPolygon((nx, ny), 6, radius=0.55,
                                                facecolor="white", edgecolor=color, linewidth=2.5)
            ax.add_patch(hex_patch)
            ax.text(nx, ny, label, ha="center", va="center",
                    fontsize=7, fontweight="bold", color=DARK, fontfamily="sans-serif")
        else:
            dag_node(ax, nx, ny, label, color=color, r=0.55, fontsize=7)

    # Arrow from Decision -> Lives (still intact)
    arrow(ax, 5.85, bot_y, 6.9, bot_y, color=DARK, lw=2.5)
    # Arrow from Capacity -> Lives (still intact)
    arrow(ax, 3.0, bot_y - 0.45, 6.95, bot_y - 0.45, color=GRAY, lw=1.5, style="-|>")

    # CUT arrow: Capacity -> Decision (dashed + red X)
    ax.plot([3.1, 4.15], [bot_y, bot_y], color=RED, lw=2, linestyle="--", alpha=0.5)
    ax.text(3.6, bot_y + 0.2, "X", ha="center", va="center",
            fontsize=18, fontweight="bold", color=RED, fontfamily="sans-serif")

    # EVPI bracket on right
    ax.annotate("", xy=(9.5, top_y + 0.5), xytext=(9.5, bot_y - 0.5),
                arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.5))
    ax.text(9.5, (top_y + bot_y) / 2, "EVPI", ha="center", va="center",
            fontsize=11, fontweight="bold", color=AMBER, fontfamily="sans-serif",
            rotation=270,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=1))

    save(fig, "ch07-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Portfolio Allocation
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch08():
    fig, ax = new_fig("Ch 8 — Portfolio Allocation")

    # Fund circle (left)
    fund = Circle((1.5, 4.5), 0.7, fill=True, facecolor=BLUE, edgecolor=BLUE, linewidth=2)
    ax.add_patch(fund)
    t = ax.text(1.5, 4.5, "Pooled\nFund", ha="center", va="center",
                fontsize=10, fontweight="bold", color="white", fontfamily="sans-serif")
    t.set_path_effects([])

    # Country circles
    countries = [
        (5.5, 5.5, 0.55, "Country A\n(high burden)", BLUE),
        (5.5, 4.0, 0.45, "Country B\n(medium)", TEAL),
        (5.5, 2.5, 0.35, "Country C\n(low burden)", GREEN),
    ]

    for cx, cy, r, label, color in countries:
        c = Circle((cx, cy), r, fill=True, facecolor="white", edgecolor=color, linewidth=2.5)
        ax.add_patch(c)
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=7, fontweight="bold", color=DARK, fontfamily="sans-serif")

        # Arrow from fund to country
        dx = cx - r - 0.1 - (1.5 + 0.75)
        arrow(ax, 2.25, 4.5 + (cy - 4.5) * 0.3, cx - r - 0.1, cy,
              color=color, lw=2.5, style="-|>")

        # Uncertainty range bars
        ax.plot([cx + r + 0.2, cx + r + 0.2], [cy - 0.3, cy + 0.3],
                color=AMBER, lw=2)
        ax.plot([cx + r + 0.1, cx + r + 0.3], [cy - 0.3, cy - 0.3],
                color=AMBER, lw=2)
        ax.plot([cx + r + 0.1, cx + r + 0.3], [cy + 0.3, cy + 0.3],
                color=AMBER, lw=2)

    ax.text(6.5, 4.0, "uncertainty\nranges", ha="left", va="center",
            fontsize=7, fontstyle="italic", color=AMBER, fontfamily="sans-serif")

    # Timeline (bottom)
    tl_y = 1.2
    ax.plot([1, 9], [tl_y, tl_y], color=DARK, lw=2)

    phases = [
        (2.5, "Commit\nseed", BLUE),
        (5.0, "Observe\nresults", TEAL),
        (7.5, "Scale or\nreallocate", GREEN),
    ]

    for i, (px, plabel, pcolor) in enumerate(phases):
        ax.plot([px, px], [tl_y - 0.15, tl_y + 0.15], color=DARK, lw=2)
        circled_num(ax, px, tl_y + 0.45, i + 1, color=pcolor, r=0.18, fontsize=10)
        ax.text(px, tl_y - 0.5, plabel, ha="center", va="top",
                fontsize=9, fontweight="bold", color=pcolor, fontfamily="sans-serif")

    # Dashed lines between phases
    for px in [3.75, 6.25]:
        ax.plot([px, px], [tl_y - 0.7, tl_y + 0.7], color=LGRAY, lw=1, linestyle="--")

    # Crowding labels (bottom right)
    ax.text(8.5, 5.8, "Crowding out (−)", ha="center", fontsize=9,
            fontweight="bold", color=RED, fontfamily="sans-serif")
    ax.text(8.5, 5.4, "Gov't reduces spending", ha="center", fontsize=7,
            fontstyle="italic", color=GRAY, fontfamily="sans-serif")
    ax.text(8.5, 4.8, "Crowding in (+)", ha="center", fontsize=9,
            fontweight="bold", color=GREEN, fontfamily="sans-serif")
    ax.text(8.5, 4.4, "Gov't increases spending", ha="center", fontsize=7,
            fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    save(fig, "ch08-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — The Free-Rider Trap
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch09():
    fig, ax = new_fig("Ch 9 — The Free-Rider Trap")

    # ── 2×2 Payoff Matrix ──
    mx, my = 3.5, 3.2  # top-left of matrix
    cw, ch_m = 2.0, 1.4  # cell width, cell height

    # Headers
    ax.text(mx + cw, my + 0.6, "Government", ha="center", fontsize=12,
            fontweight="bold", color=TEAL, fontfamily="sans-serif")
    ax.text(mx + 0.5 * cw, my + 0.15, "Absorb", ha="center", fontsize=10,
            fontweight="bold", color=TEAL, fontfamily="sans-serif")
    ax.text(mx + 1.5 * cw, my + 0.15, "Free-Ride", ha="center", fontsize=10,
            fontweight="bold", color=RED, fontfamily="sans-serif")

    ax.text(mx - 0.6, my - ch_m, "Donor", ha="center", fontsize=12,
            fontweight="bold", color=BLUE, fontfamily="sans-serif", rotation=90)
    ax.text(mx - 0.15, my - 0.5 * ch_m, "Fund\nHigh", ha="center", fontsize=10,
            fontweight="bold", color=BLUE, fontfamily="sans-serif")
    ax.text(mx - 0.15, my - 1.5 * ch_m, "Fund\nLow", ha="center", fontsize=10,
            fontweight="bold", color=BLUE, fontfamily="sans-serif")

    # Grid lines
    for i in range(3):
        ax.plot([mx, mx + 2 * cw], [my - i * ch_m, my - i * ch_m], color=DARK, lw=1.5)
    for j in range(3):
        ax.plot([mx + j * cw, mx + j * cw], [my, my - 2 * ch_m], color=DARK, lw=1.5)

    # Cell contents
    cells = [
        (0, 0, "Best for all\n(+10, +10)", "#E8F8E8", GREEN),
        (1, 0, "Trap!\n(+3, +8)", "#FEECEB", RED),
        (0, 1, "Donor bears\ncost alone\n(+5, +2)", "#FFF9E6", AMBER),
        (1, 1, "Both lose\n(+1, +1)", "#F0F0F0", GRAY),
    ]

    for col, row, text, fc, tc in cells:
        x = mx + col * cw
        y = my - row * ch_m
        rect = FancyBboxPatch((x + 0.05, y - ch_m + 0.05), cw - 0.1, ch_m - 0.1,
                              boxstyle="round,pad=0.05", facecolor=fc, edgecolor="none")
        ax.add_patch(rect)
        ax.text(x + cw / 2, y - ch_m / 2, text, ha="center", va="center",
                fontsize=8, fontweight="bold", color=tc, fontfamily="sans-serif")

    # Nash equilibrium marker
    ne_x = mx + 1.5 * cw
    ne_y = my - 0.5 * ch_m
    ax.text(ne_x + 0.8, ne_y, "Nash\nEquilibrium", ha="left", fontsize=9,
            fontweight="bold", color=RED, fontfamily="sans-serif")
    arrow(ax, ne_x + 0.75, ne_y, ne_x + cw/2 - 0.1, ne_y, color=RED, lw=2, style="-|>")

    # Curved escape arrow from trap to optimal
    opt_x = mx + 0.5 * cw
    opt_y = my - 0.5 * ch_m
    ax.annotate("", xy=(opt_x, opt_y + 0.3), xytext=(ne_x, ne_y + 0.5),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=3,
                                connectionstyle="arc3,rad=0.3"))

    # Escape routes
    ax.text(5.5, 5.8, "Escape routes:", ha="left", fontsize=10,
            fontweight="bold", color=GREEN, fontfamily="sans-serif")
    escapes = [
        ("Commitment devices", "(milestone payments)"),
        ("Repeated games", "(reputation)"),
        ("Matching grants", "(incentive alignment)"),
    ]
    for i, (main, sub) in enumerate(escapes):
        ey = 5.3 - i * 0.55
        circled_num(ax, 5.5, ey, i + 1, color=GREEN, r=0.17, fontsize=9)
        ax.text(5.85, ey, main, ha="left", fontsize=9,
                fontweight="bold", color=DARK, fontfamily="sans-serif")
        ax.text(8.0, ey, sub, ha="left", fontsize=8,
                fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Bottom summary
    ax.text(5, 0.3, "Change the game, not the players",
            ha="center", fontsize=11, fontweight="bold", color=BLUE, fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=2))

    save(fig, "ch09-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 10 — Expert + Algorithm + Data
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch10():
    fig, ax = new_fig("Ch 10 — Expert + Algorithm + Data")

    # Triangle vertices
    top = (5, 5.5)
    bl = (2.5, 2.0)
    br = (7.5, 2.0)

    # Nodes
    node_r = 0.6
    nodes = [
        (*top, "Expert", BLUE),
        (*bl, "Algorithm", ORANGE),
        (*br, "Data", TEAL),
    ]

    for nx, ny, label, color in nodes:
        c = Circle((nx, ny), node_r, fill=True, facecolor="white", edgecolor=color, linewidth=3)
        ax.add_patch(c)
        ax.text(nx, ny, label, ha="center", va="center",
                fontsize=11, fontweight="bold", color=DARK, fontfamily="sans-serif")

    # Subtitles
    ax.text(top[0] - 1.2, top[1] + 0.2, "Proposes\nstructure", ha="center",
            fontsize=9, fontstyle="italic", color=BLUE, fontfamily="sans-serif")
    ax.text(bl[0] - 0.2, bl[1] - 0.85, "Tests & refines\n(PC / Hill Climbing)", ha="center",
            fontsize=9, fontstyle="italic", color=ORANGE, fontfamily="sans-serif")
    ax.text(br[0] + 0.2, br[1] - 0.85, "Reveals\nindependencies", ha="center",
            fontsize=9, fontstyle="italic", color=TEAL, fontfamily="sans-serif")

    # Cycle arrows (Expert -> Algorithm -> Data -> Expert)
    edges = [(top, bl), (bl, br), (br, top)]
    colors_e = [BLUE, ORANGE, TEAL]
    for (x1, y1), (x2, y2), ec in zip(
            [top, bl, br], [bl, br, top], colors_e):
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        r = node_r + 0.1
        arrow(ax, x1 + r * dx/dist, y1 + r * dy/dist,
              x2 - r * dx/dist, y2 - r * dy/dist,
              color=ec, lw=2.5, style="-|>")

    # Center: CPDAG
    center = (5, 3.2)
    cpdag_box = FancyBboxPatch((center[0] - 0.9, center[1] - 0.45), 1.8, 0.9,
                               boxstyle="round,pad=0.1", facecolor="#FFF9E6",
                               edgecolor=AMBER, linewidth=2)
    ax.add_patch(cpdag_box)
    ax.text(center[0], center[1], "CPDAG", ha="center", va="center",
            fontsize=11, fontweight="bold", color=AMBER, fontfamily="sans-serif")
    ax.text(center[0], center[1] - 0.65, "Some edges remain\nambiguous", ha="center",
            fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Exit arrow: Expert -> Oriented DAG
    exit_x = 8.5
    exit_y = 5.5
    arrow(ax, top[0] + node_r + 0.1, top[1], exit_x - 0.7, exit_y,
          color=GREEN, lw=3, style="-|>")

    rounded_box(ax, exit_x, exit_y, 1.8, 0.8, "Oriented\nDAG", fc="#E8F8E8", ec=GREEN, lw=2.5, fontsize=10)
    ax.text(exit_x, exit_y - 0.6, "Expert resolves\nambiguous edges", ha="center",
            fontsize=8, fontstyle="italic", color=GREEN, fontfamily="sans-serif")

    # Bottom annotation
    ax.text(5, 0.4, "Markov equivalence: data alone cannot distinguish all structures",
            ha="center", fontsize=10, fontweight="bold", color=DARK, fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FEECEB", edgecolor=RED, linewidth=1.5))

    save(fig, "ch10-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# INTRO — The Course Journey
# ══════════════════════════════════════════════════════════════════════════════

def draw_intro():
    fig, ax = new_fig("The Course Journey")

    # ── Four-phase pathway flowing left to right ──
    # Phase boxes
    phases = [
        {"label": "FOUNDATIONS", "sub": "Ch 1–3", "color": BLUE,
         "desc": "Think\nCausally", "y": 4.5, "x": 1.3},
        {"label": "QUANTIFY", "sub": "Ch 4–6", "color": TEAL,
         "desc": "Add Numbers\n& Catch Traps", "y": 4.5, "x": 3.9},
        {"label": "DECIDE", "sub": "Ch 7–9", "color": GREEN,
         "desc": "Intervene,\nAllocate, Negotiate", "y": 4.5, "x": 6.5},
        {"label": "DISCOVER", "sub": "Ch 10", "color": AMBER,
         "desc": "Let Data\nRefine the Model", "y": 4.5, "x": 9.1},
    ]

    for i, p in enumerate(phases):
        # Phase box
        w, h = 2.0, 2.4
        box = FancyBboxPatch((p["x"] - w/2, p["y"] - h/2), w, h,
                             boxstyle="round,pad=0.15", facecolor="white",
                             edgecolor=p["color"], linewidth=3)
        ax.add_patch(box)

        # Phase label
        ax.text(p["x"], p["y"] + 0.7, p["label"], ha="center", va="center",
                fontsize=12, fontweight="bold", color=p["color"], fontfamily="sans-serif")

        # Subtitle (chapter range)
        ax.text(p["x"], p["y"] + 0.25, p["sub"], ha="center", va="center",
                fontsize=10, fontweight="bold", color=GRAY, fontfamily="sans-serif")

        # Description
        ax.text(p["x"], p["y"] - 0.5, p["desc"], ha="center", va="center",
                fontsize=9, color=DARK, fontfamily="sans-serif")

        # Circled phase number
        circled_num(ax, p["x"] - w/2 + 0.3, p["y"] + h/2 - 0.3, i + 1,
                    color=p["color"], r=0.2, fontsize=11)

        # Arrow to next phase
        if i < len(phases) - 1:
            nx = phases[i + 1]["x"]
            arrow(ax, p["x"] + w/2 + 0.05, p["y"], nx - w/2 - 0.05, p["y"],
                  color=DARK, lw=2.5, style="-|>")

    # ── Chapter labels underneath each phase ──
    ch_labels = [
        (1.3, [("1", "Causal\nThinking"), ("2", "Draw\nModels"), ("3", "Interview\n& Build")]),
        (3.9, [("4", "Probability\n& Bayes"), ("5", "Inference"), ("6", "Simpson's\nParadox")]),
        (6.5, [("7", "do(X)\nSurgery"), ("8", "Portfolio\nAllocation"), ("9", "Game\nTheory")]),
        (9.1, [("10", "Algorithms\n+ Experts")]),
    ]

    for phase_x, chapters in ch_labels:
        n = len(chapters)
        offsets = [phase_x + (i - (n - 1) / 2) * 0.7 for i in range(n)]
        for (ch_num, ch_label), ox in zip(chapters, offsets):
            ax.text(ox, 2.55, ch_num, ha="center", va="center",
                    fontsize=9, fontweight="bold", color=BLUE, fontfamily="sans-serif",
                    bbox=dict(boxstyle="circle,pad=0.15", facecolor="#E8F0FE",
                              edgecolor=BLUE, linewidth=1.5))
            ax.text(ox, 2.0, ch_label, ha="center", va="center",
                    fontsize=7, color=DARK, fontfamily="sans-serif")

    # ── Feedback loop arrow from right back to left (bottom) ──
    ax.annotate("", xy=(1.3, 1.3), xytext=(9.1, 1.3),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5,
                                connectionstyle="arc3,rad=0.15", linestyle="--"))
    ax.text(5.2, 0.85, "Iterate: data updates the model, model guides new data collection",
            ha="center", va="center", fontsize=9, fontstyle="italic", color=RED,
            fontfamily="sans-serif")

    # ── Bookend labels ──
    ax.text(1.3, 6.2, "You see a\ncorrelation...", ha="center",
            fontsize=10, fontstyle="italic", color=GRAY, fontfamily="sans-serif")
    ax.text(9.1, 6.2, "...you make a\ncausal decision", ha="center",
            fontsize=10, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # Long arrow across top
    arrow(ax, 2.5, 6.2, 8.0, 6.2, color=LGRAY, lw=2, style="-|>")

    save(fig, "intro-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Generating whiteboard diagrams to {OUT_DIR}")

    with plt.xkcd():
        draw_intro()
        draw_ch01()
        draw_ch02()
        draw_ch03()
        draw_ch04()
        draw_ch05()
        draw_ch06()
        draw_ch07()
        draw_ch08()
        draw_ch09()
        draw_ch10()

    print("Done — 11 diagrams generated.")
