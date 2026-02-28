"""
Generate whiteboard summary diagrams for each chapter of
"R for Management Consultants" — one PNG per chapter.

Output: whiteboard-diagrams/ch01-whiteboard.png … ch09-whiteboard.png
Style: hand-drawn (xkcd), BKA brand colours, no axes/grids.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
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


def save(fig, name):
    fig.savefig(os.path.join(OUT_DIR, name), dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — Why R for Management Consultants
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch01():
    fig, ax = new_fig("Ch 1 \u2014 Why R for Management Consultants")

    # Central question
    cx, cy = 5, 3.5
    central = Circle((cx, cy), 0.7, fill=True, facecolor=BLUE, edgecolor=BLUE, linewidth=2.5)
    ax.add_patch(central)
    t = ax.text(cx, cy, "Why R?", ha="center", va="center",
                fontsize=16, fontweight="bold", color="white", fontfamily="sans-serif")
    t.set_path_effects([])

    # Four surrounding boxes
    boxes = [
        (cx, cy + 2.0, "Reproducible", GREEN,  0, -1),   # Top
        (cx + 2.8, cy, "Scalable",     BLUE,  -1,  0),   # Right
        (cx, cy - 2.0, "Free & Open",  TEAL,   0,  1),   # Bottom
        (cx - 2.8, cy, "Auditable",    ORANGE,  1,  0),   # Left
    ]

    for bx, by, label, color, dx, dy in boxes:
        rounded_box(ax, bx, by, 2.0, 0.8, label, fc="white", ec=color, lw=2.5, fontsize=12)
        # Arrow from box toward center
        arrow(ax, bx + dx * 0.7, by + dy * 0.3, cx + (bx - cx) * 0.25, cy + (by - cy) * 0.25,
              color=color, lw=2.5, style="-|>")

    # Bottom annotation
    ax.text(5, 0.5, "R replaces the parts of Excel that waste time and introduce errors",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=1.5))

    save(fig, "ch01-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — R Building Blocks
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch02():
    fig, ax = new_fig("Ch 2 \u2014 R Building Blocks")

    # Horizontal flow with 4 connected boxes
    labels = ["Vectors", "Data Types", "Functions", "Packages"]
    colors = [BLUE, GREEN, TEAL, ORANGE]
    annotations = [
        'c(25, 31, 20)',
        'numeric, character,\nlogical, factor',
        'calc_nmr(deaths,\nbirths)',
        'library(tidyverse)',
    ]

    x_start = 1.2
    x_gap = 2.4
    y_main = 4.0

    for i, (label, color, ann) in enumerate(zip(labels, colors, annotations)):
        x = x_start + i * x_gap
        # Circled number
        circled_num(ax, x - 0.7, y_main + 0.5, i + 1, color=color, r=0.2, fontsize=11)
        # Main box
        rounded_box(ax, x, y_main, 1.8, 0.9, label, fc="white", ec=color, lw=2.5, fontsize=12)
        # Annotation below
        ax.text(x, y_main - 0.85, ann, ha="center", va="center",
                fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

        # Arrow to next box
        if i < len(labels) - 1:
            x_next = x_start + (i + 1) * x_gap
            arrow(ax, x + 0.95, y_main, x_next - 0.95, y_main,
                  color=DARK, lw=2.5, style="-|>")

    # Bottom summary
    ax.text(5, 1.5, "These four building blocks underpin everything in R",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=2))

    save(fig, "ch02-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — Import -> Explore -> Clean
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch03():
    fig, ax = new_fig("Ch 3 \u2014 Import \u2192 Explore \u2192 Clean")

    # Three steps left to right
    steps = [
        ("Import", BLUE, "read_csv()\nread_excel()"),
        ("Explore", GREEN, "glimpse()\nsummary()"),
        ("Handle NAs", RED, "is.na()\nna.rm = TRUE"),
    ]

    x_positions = [1.8, 5.0, 8.2]
    y_main = 3.8

    for i, ((label, color, ann), x) in enumerate(zip(steps, x_positions)):
        # Step number
        circled_num(ax, x - 1.0, y_main + 0.55, i + 1, color=color, r=0.22, fontsize=12)

        # Main box
        rounded_box(ax, x, y_main, 2.2, 1.1, label, fc="white", ec=color, lw=2.5, fontsize=14)

        # Annotation below
        ax.text(x, y_main - 1.0, ann, ha="center", va="center",
                fontsize=10, fontstyle="italic", color=GRAY, fontfamily="sans-serif",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="#F8F8F8",
                          edgecolor=LGRAY, linewidth=1))

        # Arrow to next step
        if i < len(steps) - 1:
            x_next = x_positions[i + 1]
            arrow(ax, x + 1.15, y_main, x_next - 1.15, y_main,
                  color=DARK, lw=2.5, style="-|>")

    # Bottom annotation
    ax.text(5, 1.2, "Every analysis starts with getting data in and understanding its shape",
            ha="center", va="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F8E8", edgecolor=GREEN, linewidth=1.5))

    save(fig, "ch03-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — The 5 dplyr Verbs
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch04():
    fig, ax = new_fig("Ch 4 \u2014 The 5 dplyr Verbs")

    # Central pipe symbol
    cx, cy = 5, 3.3
    pipe_circle = Circle((cx, cy), 0.55, fill=True, facecolor=BLUE, edgecolor=BLUE, linewidth=2.5)
    ax.add_patch(pipe_circle)
    t = ax.text(cx, cy, "|>", ha="center", va="center",
                fontsize=20, fontweight="bold", color="white", fontfamily="monospace")
    t.set_path_effects([])

    # 5 boxes radiating out
    verbs = [
        ("filter()",    "keep rows",     BLUE,   cx,       cy + 2.2),    # Top
        ("select()",    "pick columns",  GREEN,  cx + 2.5, cy + 1.3),    # Top-right
        ("mutate()",    "new columns",   TEAL,   cx + 2.5, cy - 1.3),    # Right (bottom-right)
        ("summarise()", "aggregate",     ORANGE, cx - 2.5, cy - 1.3),    # Bottom-left
        ("group_by()",  "split groups",  RED,    cx - 2.5, cy + 1.3),    # Top-left
    ]

    for verb, desc, color, vx, vy in verbs:
        rounded_box(ax, vx, vy, 2.0, 0.7, verb, fc="white", ec=color, lw=2.5, fontsize=11)
        # Description annotation
        # Place desc on the far side from center
        dx = vx - cx
        dy = vy - cy
        dist = np.sqrt(dx**2 + dy**2)
        desc_x = vx + dx / dist * 0.8
        desc_y = vy + dy / dist * 0.6
        ax.text(desc_x, desc_y, desc, ha="center", va="center",
                fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

        # Arrow from verb box toward center
        arrow(ax, vx - dx / dist * 0.7, vy - dy / dist * 0.25,
              cx + dx / dist * 0.35, cy + dy / dist * 0.35,
              color=color, lw=2, style="-|>")

    # Bottom annotation
    ax.text(5, 0.5, "These five verbs handle 90% of data manipulation tasks",
            ha="center", va="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=1.5))

    save(fig, "ch04-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — Reshape & Join
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch05():
    fig, ax = new_fig("Ch 5 \u2014 Reshape & Join")

    # ── LEFT SIDE: Wide <-> Long ──
    ax.text(2.8, 5.6, "RESHAPE", ha="center", fontsize=13,
            fontweight="bold", color=BLUE, fontfamily="sans-serif")

    # Wide table sketch
    wide_x, wide_y = 1.5, 4.3
    rounded_box(ax, wide_x, wide_y, 1.8, 0.9, "Wide", fc="#E8F0FE", ec=BLUE, lw=2, fontsize=12)

    # Long table sketch
    long_x, long_y = 4.1, 4.3
    rounded_box(ax, long_x, long_y, 1.8, 0.9, "Long", fc="#E8F8E8", ec=GREEN, lw=2, fontsize=12)

    # Double arrows between Wide and Long
    arrow(ax, wide_x + 0.95, wide_y + 0.15, long_x - 0.95, long_y + 0.15,
          color=TEAL, lw=2.5, style="-|>")
    arrow(ax, long_x - 0.95, long_y - 0.15, wide_x + 0.95, wide_y - 0.15,
          color=ORANGE, lw=2.5, style="-|>")

    # Labels on arrows
    ax.text(2.8, wide_y + 0.55, "pivot_longer()", ha="center", va="center",
            fontsize=9, fontweight="bold", color=TEAL, fontfamily="sans-serif")
    ax.text(2.8, wide_y - 0.55, "pivot_wider()", ha="center", va="center",
            fontsize=9, fontweight="bold", color=ORANGE, fontfamily="sans-serif")

    # ── RIGHT SIDE: Join ──
    ax.text(7.5, 5.6, "JOIN", ha="center", fontsize=13,
            fontweight="bold", color=TEAL, fontfamily="sans-serif")

    # Table A
    rounded_box(ax, 6.3, 4.5, 1.2, 0.7, "Table A", fc="#E8F0FE", ec=BLUE, lw=2, fontsize=10)
    # Table B
    rounded_box(ax, 6.3, 3.5, 1.2, 0.7, "Table B", fc="#FFF3E6", ec=ORANGE, lw=2, fontsize=10)
    # Combined
    rounded_box(ax, 8.7, 4.0, 1.5, 1.4, "Combined", fc="#E8F8E8", ec=GREEN, lw=2.5, fontsize=11)

    # Arrows from A and B to Combined
    arrow(ax, 6.95, 4.4, 7.9, 4.15, color=DARK, lw=2, style="-|>")
    arrow(ax, 6.95, 3.6, 7.9, 3.85, color=DARK, lw=2, style="-|>")

    # left_join label
    ax.text(7.5, 4.35, "left_join()", ha="center", va="center",
            fontsize=9, fontweight="bold", color=TEAL, fontfamily="sans-serif",
            rotation=-10)

    # ── Bottom: key takeaway ──
    ax.text(5, 1.5, "Reshape for plotting, join to combine data sources",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=1.5))

    # Dividing line between left and right sections
    ax.plot([5.2, 5.2], [3.0, 5.8], color=LGRAY, lw=1.5, linestyle="--")

    save(fig, "ch05-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — Grammar of Graphics
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch06():
    fig, ax = new_fig("Ch 6 \u2014 Grammar of Graphics")

    # Three stacked layers (bottom to top)
    cx = 5
    layer_w = 5.5
    layer_h = 1.1
    gap = 0.2

    layers = [
        ("Data",       'ggplot(data, ...)',         BLUE,   "#E8F0FE"),
        ("Aesthetics", 'aes(x, y, color)',          GREEN,  "#E8F8E8"),
        ("Geometry",   'geom_point() / geom_col()', ORANGE, "#FFF3E6"),
    ]

    y_base = 1.8

    for i, (label, code, color, fc) in enumerate(layers):
        y = y_base + i * (layer_h + gap + 0.3)

        # Layer box
        box = FancyBboxPatch((cx - layer_w/2, y - layer_h/2), layer_w, layer_h,
                             boxstyle="round,pad=0.12", facecolor=fc, edgecolor=color, linewidth=2.5)
        ax.add_patch(box)

        # Layer label (left side)
        ax.text(cx - layer_w/2 + 0.6, y, label, ha="center", va="center",
                fontsize=13, fontweight="bold", color=color, fontfamily="sans-serif")

        # Code annotation (right side)
        ax.text(cx + 0.8, y, code, ha="center", va="center",
                fontsize=10, fontstyle="italic", color=DARK, fontfamily="sans-serif")

        # "+" sign between layers
        if i < len(layers) - 1:
            plus_y = y + (layer_h + gap + 0.3) / 2
            ax.text(cx - layer_w/2 - 0.4, plus_y, "+", ha="center", va="center",
                    fontsize=22, fontweight="bold", color=DARK, fontfamily="sans-serif")

        # Upward arrow between layers
        if i < len(layers) - 1:
            arrow_y1 = y + layer_h/2 + 0.05
            arrow_y2 = y + layer_h/2 + gap + 0.25
            arrow(ax, cx, arrow_y1, cx, arrow_y2, color=DARK, lw=2, style="-|>")

    # Layer numbers on the left
    for i in range(len(layers)):
        y = y_base + i * (layer_h + gap + 0.3)
        circled_num(ax, cx - layer_w/2 - 0.4, y, i + 1,
                    color=layers[i][2], r=0.2, fontsize=11)

    # Top label
    ax.text(cx, y_base + 2 * (layer_h + gap + 0.3) + 0.9,
            "Layers build on each other", ha="center", va="center",
            fontsize=11, fontweight="bold", color=GRAY, fontfamily="sans-serif")

    # Bottom annotation
    ax.text(5, 0.5, "ggplot2 = Data + Aesthetics + Geometry (+ optional layers)",
            ha="center", va="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE", edgecolor=BLUE, linewidth=1.5))

    save(fig, "ch06-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 — From Default to Publication
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch07():
    fig, ax = new_fig("Ch 7 \u2014 From Default to Publication")

    # ── LEFT: Rough/ugly chart sketch ──
    left_cx, left_cy = 2.2, 3.8
    left_w, left_h = 3.0, 3.0

    # Chart frame
    rough_box = FancyBboxPatch((left_cx - left_w/2, left_cy - left_h/2),
                                left_w, left_h,
                                boxstyle="round,pad=0.08", facecolor="#F8F8F8",
                                edgecolor=GRAY, linewidth=1.5, linestyle="--")
    ax.add_patch(rough_box)

    # Ugly bar chart inside
    bars_x_pos = [1.1, 1.6, 2.1, 2.6, 3.1]
    bars_h_val = [1.5, 2.0, 1.2, 2.5, 1.8]
    for bx, bh in zip(bars_x_pos, bars_h_val):
        ax.bar(bx, bh, width=0.35, bottom=left_cy - left_h/2 + 0.2,
               color=GRAY, edgecolor=DARK, linewidth=1, alpha=0.5)

    ax.text(left_cx, left_cy + left_h/2 + 0.25, "DEFAULT", ha="center",
            fontsize=12, fontweight="bold", color=RED, fontfamily="sans-serif")
    ax.text(left_cx, left_cy - left_h/2 - 0.25, "(gray, no labels, messy)",
            ha="center", fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # ── RIGHT: Polished chart sketch ──
    right_cx, right_cy = 7.8, 3.8
    right_w, right_h = 3.0, 3.0

    polished_box = FancyBboxPatch((right_cx - right_w/2, right_cy - right_h/2),
                                   right_w, right_h,
                                   boxstyle="round,pad=0.08", facecolor="white",
                                   edgecolor=GREEN, linewidth=2.5)
    ax.add_patch(polished_box)

    # Polished bars with BKA colors
    pol_colors = [BLUE, TEAL, GREEN, ORANGE, AMBER]
    for bx_offset, bh, bc in zip([6.7, 7.2, 7.7, 8.2, 8.7], bars_h_val, pol_colors):
        ax.bar(bx_offset, bh, width=0.35, bottom=right_cy - right_h/2 + 0.2,
               color=bc, edgecolor=DARK, linewidth=1, alpha=0.85)

    ax.text(right_cx, right_cy + right_h/2 + 0.25, "PUBLICATION", ha="center",
            fontsize=12, fontweight="bold", color=GREEN, fontfamily="sans-serif")
    ax.text(right_cx, right_cy - right_h/2 - 0.25, "(branded, labeled, clean)",
            ha="center", fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

    # ── Arrow between charts with polish labels ──
    arrow(ax, left_cx + left_w/2 + 0.15, left_cy, right_cx - right_w/2 - 0.15, right_cy,
          color=DARK, lw=3, style="-|>")

    polish_labels = [
        ("theme_bka()", BLUE),
        ("BKA colors", TEAL),
        ("facet_wrap()", GREEN),
        ("patchwork", ORANGE),
        ("ggsave(dpi=300)", RED),
    ]
    label_x = 5.0
    for i, (plabel, pcolor) in enumerate(polish_labels):
        ly = 5.0 - i * 0.45
        ax.text(label_x, ly, plabel, ha="center", va="center",
                fontsize=9, fontweight="bold", color=pcolor, fontfamily="sans-serif")

    # Bottom annotation
    ax.text(5, 0.8, "Five steps from default R charts to client-ready output",
            ha="center", va="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F8E8", edgecolor=GREEN, linewidth=1.5))

    save(fig, "ch07-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 8 — Descriptive Statistics
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch08():
    fig, ax = new_fig("Ch 8 \u2014 Descriptive Statistics")

    # Pyramid / hierarchy (bottom to top, increasing complexity)
    cx = 5.0

    # Bottom row (widest): two boxes side by side
    bottom_labels = [
        ("Proportions\nmean(logical)", ORANGE, 3.0, 1.5),
        ("Central Tendency\nmean() / median()", RED, 7.0, 1.5),
    ]

    # Middle row: two boxes
    middle_labels = [
        ("Correlation\ncor()", GREEN, 3.5, 3.2),
        ("Confidence Intervals\nt.test()", TEAL, 6.5, 3.2),
    ]

    # Top row (narrowest): one box
    top_labels = [
        ("Regression\nlm()", BLUE, 5.0, 4.9),
    ]

    all_levels = [
        (bottom_labels, 2.6, 1.0),
        (middle_labels, 2.2, 1.0),
        (top_labels, 2.4, 1.0),
    ]

    for level_items, bw, bh in all_levels:
        for label, color, bx, by in level_items:
            rounded_box(ax, bx, by, bw, bh, label, fc="white", ec=color, lw=2.5, fontsize=10)

    # Upward arrow on left side: "Increasing complexity"
    arrow(ax, 0.8, 1.0, 0.8, 5.5, color=AMBER, lw=3, style="-|>")
    ax.text(0.5, 3.3, "Increasing\ncomplexity", ha="center", va="center",
            fontsize=10, fontweight="bold", color=AMBER, fontfamily="sans-serif",
            rotation=90)

    # Connecting arrows between levels
    # Bottom-left -> Middle-left
    arrow(ax, 3.2, 2.05, 3.4, 2.65, color=LGRAY, lw=1.5, style="-|>")
    # Bottom-right -> Middle-right
    arrow(ax, 6.8, 2.05, 6.6, 2.65, color=LGRAY, lw=1.5, style="-|>")
    # Middle-left -> Top
    arrow(ax, 3.8, 3.75, 4.6, 4.35, color=LGRAY, lw=1.5, style="-|>")
    # Middle-right -> Top
    arrow(ax, 6.2, 3.75, 5.4, 4.35, color=LGRAY, lw=1.5, style="-|>")

    # Bottom annotation
    ax.text(5, 0.3, "Start simple, build up \u2014 each level adds insight",
            ha="center", va="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=1.5))

    save(fig, "ch08-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 9 — Reproducible Reports
# ══════════════════════════════════════════════════════════════════════════════

def draw_ch09():
    fig, ax = new_fig("Ch 9 \u2014 Reproducible Reports")

    # ── Box 1: .qmd file ──
    qmd_x, qmd_y = 2.0, 4.0
    qmd_w, qmd_h = 2.5, 2.8

    qmd_box = FancyBboxPatch((qmd_x - qmd_w/2, qmd_y - qmd_h/2), qmd_w, qmd_h,
                              boxstyle="round,pad=0.12", facecolor="#E8F0FE",
                              edgecolor=BLUE, linewidth=2.5)
    ax.add_patch(qmd_box)
    ax.text(qmd_x, qmd_y + qmd_h/2 - 0.35, ".qmd file", ha="center", va="center",
            fontsize=13, fontweight="bold", color=BLUE, fontfamily="sans-serif")

    # Three sub-items inside the .qmd box
    sub_items = [
        ("YAML",     AMBER,  qmd_y + 0.25),
        ("Markdown", TEAL,   qmd_y - 0.3),
        ("R code",   GREEN,  qmd_y - 0.85),
    ]
    for slabel, scolor, sy in sub_items:
        sub_box = FancyBboxPatch((qmd_x - 0.8, sy - 0.2), 1.6, 0.4,
                                  boxstyle="round,pad=0.05", facecolor="white",
                                  edgecolor=scolor, linewidth=1.5)
        ax.add_patch(sub_box)
        ax.text(qmd_x, sy, slabel, ha="center", va="center",
                fontsize=9, fontweight="bold", color=scolor, fontfamily="sans-serif")

    # ── Box 2: quarto render ──
    render_x, render_y = 5.0, 4.0
    rounded_box(ax, render_x, render_y, 1.8, 1.0, "quarto\nrender",
                fc="#E8F8E8", ec=TEAL, lw=2.5, fontsize=11)

    # Arrow from .qmd to render
    arrow(ax, qmd_x + qmd_w/2 + 0.05, qmd_y, render_x - 0.95, render_y,
          color=DARK, lw=2.5, style="-|>")

    # ── Three output boxes ──
    outputs = [
        ("HTML", GREEN,  8.0, 5.0),
        ("PDF",  ORANGE, 8.0, 4.0),
        ("DOCX", RED,    8.0, 3.0),
    ]

    for olabel, ocolor, ox, oy in outputs:
        rounded_box(ax, ox, oy, 1.4, 0.7, olabel, fc="white", ec=ocolor, lw=2.5, fontsize=11)
        # Arrow from render to output
        arrow(ax, render_x + 0.95, render_y + (oy - render_y) * 0.3,
              ox - 0.75, oy, color=ocolor, lw=2, style="-|>")

    # ── Bottom: parameterized reports ──
    ax.text(5, 1.5, 'params$country \u2192 5 country briefs from 1 template',
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFF9E6", edgecolor=AMBER, linewidth=2))

    # Small param illustration
    param_countries = ["Kenya", "Ethiopia", "Malawi", "Tanzania", "Uganda"]
    for i, country in enumerate(param_countries):
        px = 2.0 + i * 1.55
        py = 0.5
        ax.text(px, py, country, ha="center", va="center",
                fontsize=7, fontweight="bold", color=BLUE, fontfamily="sans-serif",
                bbox=dict(boxstyle="round,pad=0.15", facecolor="#E8F0FE",
                          edgecolor=BLUE, linewidth=1))

    save(fig, "ch09-whiteboard.png")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Generating whiteboard diagrams to {OUT_DIR}")

    with plt.xkcd():
        draw_ch01()
        draw_ch02()
        draw_ch03()
        draw_ch04()
        draw_ch05()
        draw_ch06()
        draw_ch07()
        draw_ch08()
        draw_ch09()

    print("Done \u2014 9 diagrams generated.")
