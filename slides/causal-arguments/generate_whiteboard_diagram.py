"""
Generate whiteboard summary diagram for
"Making Causal Arguments That Hold Up" -- one PNG.

Output: whiteboard-diagram.png
Style: hand-drawn (xkcd), BKA brand colours, no axes/grids.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Circle

# -- Shared constants --------------------------------------------------------

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
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


# ============================================================================
# THE DIAGRAM -- Three Alternatives Layout
# ============================================================================

def draw_diagram():
    fig, ax = new_fig("Making Causal Arguments That Hold Up")

    cx, cy = 5, 3.5  # centre of diagram

    # -- Central circle: "X caused Y?" ------------------------------------
    center_r = 0.95
    c = Circle((cx, cy), center_r, fill=True,
               facecolor=BLUE, edgecolor=BLUE, linewidth=2.5)
    ax.add_patch(c)
    t = ax.text(cx, cy, "X caused\nY?", ha="center", va="center",
                fontsize=15, fontweight="bold", color="white", fontfamily="sans-serif",
                linespacing=1.1)
    t.set_path_effects([])

    # -- Three surrounding boxes ------------------------------------------
    box_w, box_h = 2.2, 1.0

    boxes = [
        # (x,   y,    label,                subtitle,                              color, num)
        (cx,   5.5,   "Common\nCause",       "Could a third factor\ncause both?",  RED,   "1"),
        (1.7,  cy,    "Coincidence",          "Could X and Y be\nunrelated?",       ORANGE, "2"),
        (8.3,  cy,    "Reversed\nCausation",  "Could Y actually\ncause X?",         TEAL,  "3"),
    ]

    for bx, by, label, sublabel, color, num in boxes:
        rounded_box(ax, bx, by, box_w, box_h, label,
                    fc="white", ec=color, lw=2.5, fontsize=11)

        # Subtitle below each box
        sub_y = by - box_h / 2 - 0.28
        ax.text(bx, sub_y, sublabel, ha="center", va="center",
                fontsize=7.5, fontstyle="italic", color=GRAY, fontfamily="sans-serif",
                linespacing=1.2)

        # Circled step number at top-left of box
        circled_num(ax, bx - box_w / 2 + 0.28, by + box_h / 2 - 0.18,
                    num, color=color, r=0.22, fontsize=10)

    # -- Arrows from centre outward ----------------------------------------
    pad = 0.08

    # Up: centre -> "Common Cause"
    arrow(ax, cx, cy + center_r + pad,
          cx, 5.5 - box_h / 2 - pad,
          color=DARK, lw=2.5, style="-|>")

    # Left: centre -> "Coincidence"
    arrow(ax, cx - center_r - pad, cy,
          1.7 + box_w / 2 + pad, cy,
          color=DARK, lw=2.5, style="-|>")

    # Right: centre -> "Reversed Causation"
    arrow(ax, cx + center_r + pad, cy,
          8.3 - box_w / 2 - pad, cy,
          color=DARK, lw=2.5, style="-|>")

    # -- Two-part structure below centre -----------------------------------
    # Show the "build" side: correlation + causal story
    build_y = 1.6
    rounded_box(ax, 3.2, build_y, 2.4, 0.75, "Show the\nCorrelation",
                fc="white", ec=GREEN, lw=2, fontsize=10)
    rounded_box(ax, 6.8, build_y, 2.4, 0.75, "Tell the\nCausal Story",
                fc="white", ec=GREEN, lw=2, fontsize=10)

    # Arrow between the two build boxes
    arrow(ax, 3.2 + 2.4 / 2 + pad, build_y,
          6.8 - 2.4 / 2 - pad, build_y,
          color=GREEN, lw=2, style="-|>")

    # Label above the build section
    ax.text(5, build_y + 0.65, "Building Your Argument",
            ha="center", fontsize=10, fontweight="bold", color=GREEN,
            fontfamily="sans-serif")

    # Arrow from centre down to build section
    arrow(ax, cx, cy - center_r - pad,
          cx, build_y + 0.75 / 2 + 0.55,
          color=DARK, lw=2, style="-|>")

    # -- Bottom annotation -------------------------------------------------
    ax.text(5, 0.35,
            "Shows the pattern \u2022 Explains the mechanism \u2022 Rules out the alternatives",
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
