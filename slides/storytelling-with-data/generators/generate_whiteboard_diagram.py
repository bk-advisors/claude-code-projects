"""
Generate whiteboard summary diagram for
"Storytelling with Data" — the four-quadrant model.

Output: whiteboard-diagram.png
Style: hand-drawn (xkcd), BKA brand colours, no axes/grids.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# -- Shared constants --------------------------------------------------------

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "generated")
os.makedirs(OUT_DIR, exist_ok=True)
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


# -- Helpers -----------------------------------------------------------------

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


def rounded_box(ax, x, y, w, h, text, fc="white", ec=BLUE, lw=2,
                fontsize=11, textcolor=DARK):
    """Draw a rounded rectangle with centred text."""
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                         boxstyle="round,pad=0.15", facecolor=fc,
                         edgecolor=ec, linewidth=lw)
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=textcolor,
            fontfamily="sans-serif", linespacing=1.2)


def arrow(ax, x1, y1, x2, y2, color=DARK, lw=2, style="->"):
    """Draw an arrow between two points."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw))


def save(fig, name):
    fig.savefig(os.path.join(OUT_DIR, name), dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


# ============================================================================
# THE DIAGRAM — Four-Quadrant Model
# ============================================================================

def draw_diagram():
    fig, ax = new_fig("The Four Modes of Data Storytelling")

    cx, cy = 5, 3.3  # centre of the quadrant layout
    box_w, box_h = 3.6, 1.6
    gap = 0.3

    # -- Axis labels --
    # Horizontal axis: Time
    ax.annotate("", xy=(9.5, cy), xytext=(0.5, cy),
                arrowprops=dict(arrowstyle="-|>", color=LGRAY, lw=2))
    ax.text(0.7, cy + 0.2, "PAST", ha="left", fontsize=9, color=GRAY,
            fontfamily="sans-serif", fontweight="bold")
    ax.text(9.3, cy + 0.2, "FUTURE", ha="right", fontsize=9, color=GRAY,
            fontfamily="sans-serif", fontweight="bold")

    # Vertical axis: Intent
    ax.annotate("", xy=(cx, 6.0), xytext=(cx, 0.6),
                arrowprops=dict(arrowstyle="-|>", color=LGRAY, lw=2))
    ax.text(cx + 0.15, 5.85, "ACTION", ha="left", fontsize=9, color=GRAY,
            fontfamily="sans-serif", fontweight="bold")
    ax.text(cx + 0.15, 0.75, "UNDERSTANDING", ha="left", fontsize=9,
            color=GRAY, fontfamily="sans-serif", fontweight="bold")

    # -- Quadrant boxes --
    # Top-left: Diagnostic (past + action/understanding overlap — placed upper-left)
    qx_left = cx - box_w / 2 - gap / 2
    qx_right = cx + box_w / 2 + gap / 2
    qy_top = cy + box_h / 2 + gap / 2
    qy_bot = cy - box_h / 2 - gap / 2

    # Top-left: Diagnostic
    rounded_box(ax, qx_left, qy_top, box_w, box_h,
                "DIAGNOSTIC\n\nWhy did this\nhappen?",
                fc="white", ec=ORANGE, lw=3, fontsize=11, textcolor=DARK)
    ax.text(qx_left - box_w / 2 + 0.2, qy_top + box_h / 2 - 0.15,
            "africa-measles", fontsize=7, fontstyle="italic", color=ORANGE,
            fontfamily="sans-serif")

    # Top-right: Predictive
    rounded_box(ax, qx_right, qy_top, box_w, box_h,
                "PREDICTIVE\n\nWhat will\nhappen next?",
                fc="white", ec=TEAL, lw=3, fontsize=11, textcolor=DARK)
    ax.text(qx_right - box_w / 2 + 0.2, qy_top + box_h / 2 - 0.15,
            "hpv-png-story", fontsize=7, fontstyle="italic", color=TEAL,
            fontfamily="sans-serif")

    # Bottom-left: Descriptive
    rounded_box(ax, qx_left, qy_bot, box_w, box_h,
                "DESCRIPTIVE\n\nWhat is\nhappening?",
                fc="white", ec=LBLUE, lw=3, fontsize=11, textcolor=DARK)

    # Bottom-right: Prescriptive
    rounded_box(ax, qx_right, qy_bot, box_w, box_h,
                "PRESCRIPTIVE\n\nWhat should\nwe do?",
                fc="white", ec=GREEN, lw=3, fontsize=11, textcolor=DARK)
    ax.text(qx_right - box_w / 2 + 0.2, qy_bot + box_h / 2 - 0.15,
            "Aman's framework", fontsize=7, fontstyle="italic", color=GREEN,
            fontfamily="sans-serif")

    # -- Bottom annotation --
    ax.text(5, 0.2,
            "Most stories cover 1\u20132 quadrants. The best ones cover all four.",
            ha="center", fontsize=10, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE",
                      edgecolor=BLUE, linewidth=2))

    save(fig, "whiteboard-diagram.png")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("Generating whiteboard diagram...")

    with plt.xkcd():
        draw_diagram()

    print("Done \u2014 1 diagram generated.")
