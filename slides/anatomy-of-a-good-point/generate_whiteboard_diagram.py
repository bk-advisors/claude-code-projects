"""
Generate whiteboard summary diagram for
"The Anatomy of a Good Point" — one PNG.

Output: whiteboard-diagram.png
Style: hand-drawn (xkcd), BKA brand colours, no axes/grids.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Circle

# ── Shared constants ──────────────────────────────────────────────────────────

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
# THE DIAGRAM — Compass / Cross Layout
# ══════════════════════════════════════════════════════════════════════════════

def draw_diagram():
    fig, ax = new_fig("Anatomy of a Good Point")

    cx, cy = 5, 3.5  # centre of compass

    # ── Central circle: Step 1 ────────────────────────────────────────────
    # xkcd mode adds a white stroke outline to all text via path_effects,
    # which makes white-on-blue text illegible.  We strip those effects
    # from the text inside this circle.
    center_r = 0.95
    c = Circle((cx, cy), center_r, fill=True,
               facecolor=BLUE, edgecolor=BLUE, linewidth=2.5)
    ax.add_patch(c)
    t = ax.text(cx, cy, "1.\nWhat's\nthe Point?", ha="center", va="center",
                fontsize=13, fontweight="bold", color="white", fontfamily="sans-serif",
                linespacing=1.1)
    t.set_path_effects([])

    # ── Four surrounding boxes ────────────────────────────────────────────
    box_w, box_h = 2.2, 1.0

    boxes = [
        # (x,   y,    label,           subtitle,                      color,  step_num)
        (1.7,  cy,    "Why It's True",  "The Reasoning",              GREEN,  "2"),
        (cx,   5.5,   "Zoom Out",       "Induction / Patterns",       TEAL,   "3b"),
        (cx,   1.5,   "Zoom In",        "Deduction / Specific Example", RED,  "3a"),
        (8.3,  cy,    "Who Cares?",     "The Impact",                 ORANGE, "4"),
    ]

    for bx, by, label, sublabel, color, step_num in boxes:
        rounded_box(ax, bx, by, box_w, box_h, label,
                    fc="white", ec=color, lw=2.5, fontsize=11)

        # Subtitle below each box
        sub_y = by - box_h / 2 - 0.22
        ax.text(bx, sub_y, sublabel, ha="center", va="center",
                fontsize=8, fontstyle="italic", color=GRAY, fontfamily="sans-serif")

        # Circled step number at top-left of box
        circled_num(ax, bx - box_w / 2 + 0.28, by + box_h / 2 - 0.18,
                    step_num, color=color, r=0.22, fontsize=10)

    # ── Arrows from centre outward ────────────────────────────────────────
    pad = 0.08  # gap between arrow tip and box/circle edge

    # Left: centre -> "Why It's True"
    arrow(ax, cx - center_r - pad, cy,
          1.7 + box_w / 2 + pad, cy,
          color=DARK, lw=2.5, style="-|>")

    # Up: centre -> "Zoom Out"
    arrow(ax, cx, cy + center_r + pad,
          cx, 5.5 - box_h / 2 - pad,
          color=DARK, lw=2.5, style="-|>")

    # Down: centre -> "Zoom In"
    arrow(ax, cx, cy - center_r - pad,
          cx, 1.5 + box_h / 2 + pad,
          color=DARK, lw=2.5, style="-|>")

    # Right: centre -> "Who Cares?"
    arrow(ax, cx + center_r + pad, cy,
          8.3 - box_w / 2 - pad, cy,
          color=DARK, lw=2.5, style="-|>")

    # ── Bottom annotation ─────────────────────────────────────────────────
    ax.text(5, 0.35,
            "A good point isn't just correct \u2014 it's complete",
            ha="center", fontsize=11, fontweight="bold", color=DARK,
            fontfamily="sans-serif",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E8F0FE",
                      edgecolor=BLUE, linewidth=2))

    save(fig, "whiteboard-diagram.png")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("Generating whiteboard diagram...")

    with plt.xkcd():
        draw_diagram()

    print("Done \u2014 1 diagram generated.")
