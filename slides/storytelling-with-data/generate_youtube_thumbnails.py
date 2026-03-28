"""
Generate YouTube thumbnail images for Storytelling with Data videos.
Output: youtube-thumb-intro.png, youtube-thumb-full-lecture.png
Style: polished (no xkcd), BKA brand colours, 1280x720 (YouTube recommended).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

# -- Constants ---------------------------------------------------------------

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
DPI = 100  # 1280x720 px at 12.8x7.2 inches
FIG_W, FIG_H = 12.8, 7.2

# BKA brand colours
BLUE = "#005CB9"
LBLUE = "#00A1DF"
GREEN = "#83BD00"
TEAL = "#3E9B6E"
RED = "#E24A3F"
ORANGE = "#FA7650"
AMBER = "#F8A623"
YELLOW = "#FED141"
DARK = "#333333"
WHITE = "#FFFFFF"


# -- Helpers -----------------------------------------------------------------

def new_fig(bg_color=BLUE):
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0, 7.2)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def rounded_box(ax, x, y, w, h, text, fc="white", ec="white", lw=2,
                fontsize=14, textcolor=DARK, alpha=1.0):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                         boxstyle="round,pad=0.12", facecolor=fc,
                         edgecolor=ec, linewidth=lw, alpha=alpha)
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=textcolor,
            fontfamily="sans-serif", linespacing=1.15)


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0,
                facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


# ============================================================================
# THUMBNAIL 1 — Intro Video
# ============================================================================

def draw_intro_thumb():
    fig, ax = new_fig(BLUE)

    # -- Main title --
    ax.text(6.4, 5.8, "The Missing Pieces",
            ha="center", va="center",
            fontsize=44, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(6.4, 4.8, "in Data Storytelling",
            ha="center", va="center",
            fontsize=36, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif")

    # -- Four quadrant preview (two highlighted, two faded) --
    box_w, box_h = 2.8, 1.4
    gap = 0.3
    base_y = 2.2

    # Diagnostic (highlighted)
    rounded_box(ax, 4.5 - gap / 2, base_y + box_h / 2 + gap / 2,
                box_w, box_h, "DIAGNOSTIC\nWhy?",
                fc=ORANGE, ec=ORANGE, lw=0, fontsize=16, textcolor=WHITE)

    # Predictive (highlighted)
    rounded_box(ax, 8.3 + gap / 2, base_y + box_h / 2 + gap / 2,
                box_w, box_h, "PREDICTIVE\nWhat next?",
                fc=TEAL, ec=TEAL, lw=0, fontsize=16, textcolor=WHITE)

    # Descriptive (faded)
    rounded_box(ax, 4.5 - gap / 2, base_y - box_h / 2 - gap / 2,
                box_w, box_h, "Descriptive",
                fc=WHITE, ec=WHITE, lw=0, fontsize=14, textcolor=BLUE,
                alpha=0.2)

    # Prescriptive (faded)
    rounded_box(ax, 8.3 + gap / 2, base_y - box_h / 2 - gap / 2,
                box_w, box_h, "Prescriptive",
                fc=WHITE, ec=WHITE, lw=0, fontsize=14, textcolor=BLUE,
                alpha=0.2)

    # -- Bottom branding --
    ax.text(0.5, 0.35, "BK Advisors", ha="left", va="center",
            fontsize=14, fontweight="bold", color=WHITE, alpha=0.7,
            fontfamily="sans-serif")
    ax.text(12.3, 0.35, "Lecture Intro", ha="right", va="center",
            fontsize=14, color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    save(fig, "youtube-thumb-intro.png")


# ============================================================================
# THUMBNAIL 2 — Full Lecture
# ============================================================================

def draw_full_lecture_thumb():
    fig, ax = new_fig(BLUE)

    # -- Title --
    ax.text(6.4, 6.3, "Storytelling with Data",
            ha="center", va="center",
            fontsize=38, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- "FULL LECTURE" badge --
    rounded_box(ax, 11.3, 6.65, 2.4, 0.65, "FULL LECTURE",
                fc=GREEN, ec=GREEN, lw=0, fontsize=16, textcolor=WHITE)

    # -- Four-quadrant diagram --
    cx, cy = 6.4, 3.0
    box_w, box_h = 3.0, 1.5
    gap = 0.3

    quadrants = [
        # (x_offset, y_offset, label, subtitle, color)
        (-1, 1, "DIAGNOSTIC", "Why did this happen?", ORANGE),
        (1, 1, "PREDICTIVE", "What comes next?", TEAL),
        (-1, -1, "DESCRIPTIVE", "What is happening?", LBLUE),
        (1, -1, "PRESCRIPTIVE", "What should we do?", GREEN),
    ]

    for x_off, y_off, label, subtitle, color in quadrants:
        bx = cx + x_off * (box_w / 2 + gap / 2)
        by = cy + y_off * (box_h / 2 + gap / 2)
        rounded_box(ax, bx, by, box_w, box_h, "",
                    fc=color, ec=color, lw=0, fontsize=14, textcolor=WHITE)
        ax.text(bx, by + 0.2, label, ha="center", va="center",
                fontsize=15, fontweight="bold", color=WHITE,
                fontfamily="sans-serif")
        ax.text(bx, by - 0.25, subtitle, ha="center", va="center",
                fontsize=10, color=WHITE, fontfamily="sans-serif",
                alpha=0.85)

    # -- Subtitle --
    ax.text(6.4, 5.3, "Completing the Scientific Method Loop",
            ha="center", va="center",
            fontsize=18, color=YELLOW, fontfamily="sans-serif",
            fontweight="bold")

    # -- Bottom branding --
    ax.text(0.5, 0.25, "BK Advisors", ha="left", va="center",
            fontsize=14, fontweight="bold", color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    save(fig, "youtube-thumb-full-lecture.png")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("Generating YouTube thumbnails...")
    draw_intro_thumb()
    draw_full_lecture_thumb()
    print("Done \u2014 2 thumbnails generated.")
