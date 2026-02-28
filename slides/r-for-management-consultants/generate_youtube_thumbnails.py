"""
Generate YouTube thumbnail images for R for Management Consultants videos.
Output: youtube-thumb-intro.png, youtube-thumb-full-lecture.png
Style: polished (no xkcd), BKA brand colours, 1280x720 (YouTube recommended).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    """Create a 1280x720 figure with coloured background and no axes."""
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
    """Draw a rounded rectangle with centred text."""
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

    # -- Main title: "Excel → R" --
    # "Excel" on the left
    ax.text(3.8, 4.6, "Excel", ha="center", va="center",
            fontsize=64, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # Stylized arrow
    ax.annotate("", xy=(8.0, 4.6), xytext=(5.8, 4.6),
                arrowprops=dict(arrowstyle="-|>", color=GREEN,
                                lw=6, mutation_scale=40))

    # "R" on the right
    ax.text(9.4, 4.6, "R", ha="center", va="center",
            fontsize=72, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif")

    # -- Subtitle --
    ax.text(6.4, 3.1, "Stop Copying.  Start Coding.",
            ha="center", va="center",
            fontsize=28, fontweight="bold", color=WHITE,
            fontfamily="sans-serif", alpha=0.95)

    # -- Thin horizontal divider --
    ax.plot([2.5, 10.3], [2.4, 2.4], color=WHITE, lw=1.2, alpha=0.35)

    # -- Simplified code snippet visual (bottom right) --
    code_x = 9.0
    code_y = 1.4
    code_lines = [
        "library(tidyverse)",
        "data |> filter(region)",
        "  |> summarise(mean)",
    ]
    # Semi-transparent background box for code
    code_bg = FancyBboxPatch((code_x - 2.2, code_y - 0.7), 4.4, 1.6,
                              boxstyle="round,pad=0.15", facecolor=WHITE,
                              edgecolor=WHITE, linewidth=1, alpha=0.12)
    ax.add_patch(code_bg)

    for i, line in enumerate(code_lines):
        ax.text(code_x - 1.9, code_y + 0.45 - i * 0.4, line,
                ha="left", va="center",
                fontsize=12, color=WHITE, alpha=0.8,
                fontfamily="monospace")

    # -- Bottom-left branding --
    ax.text(0.5, 0.35, "BK ADVISORS", ha="left", va="center",
            fontsize=14, fontweight="bold", color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    # -- Bottom-right label --
    ax.text(12.3, 0.35, "Course Intro", ha="right", va="center",
            fontsize=14, color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    save(fig, "youtube-thumb-intro.png")


# ============================================================================
# THUMBNAIL 2 — Full Lecture (Complete Course)
# ============================================================================

def draw_full_lecture_thumb():
    fig, ax = new_fig(BLUE)

    # -- Main title --
    ax.text(6.4, 5.8, "R for Consultants",
            ha="center", va="center",
            fontsize=44, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- "COMPLETE COURSE" badge (top-right) --
    rounded_box(ax, 11.0, 6.65, 2.8, 0.65, "COMPLETE COURSE",
                fc=YELLOW, ec=YELLOW, lw=0, fontsize=16, textcolor=DARK)

    # -- Central "R" --
    cx, cy = 6.4, 3.2
    r_bg = FancyBboxPatch((cx - 0.8, cy - 0.8), 1.6, 1.6,
                           boxstyle="round,pad=0.15", facecolor=WHITE,
                           edgecolor=WHITE, linewidth=2, alpha=0.15)
    ax.add_patch(r_bg)
    ax.text(cx, cy, "R", ha="center", va="center",
            fontsize=52, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- Four coloured boxes representing the four parts --
    box_w, box_h = 2.6, 0.85
    boxes = [
        # (x, y, label, color)
        (2.8, 4.4, "Getting\nStarted", LBLUE),
        (10.0, 4.4, "Data\nWrangling", GREEN),
        (2.8, 2.0, "Visualization", ORANGE),
        (10.0, 2.0, "Communication", TEAL),
    ]

    for bx, by, label, color in boxes:
        rounded_box(ax, bx, by, box_w, box_h, label,
                    fc=color, ec=color, lw=0, fontsize=15, textcolor=WHITE)

    # -- Connecting lines from centre to boxes --
    line_alpha = 0.4
    line_lw = 2.0
    # To top-left box
    ax.plot([cx - 0.9, 2.8 + box_w / 2], [cy + 0.5, 4.4 - box_h / 2],
            color=WHITE, lw=line_lw, alpha=line_alpha)
    # To top-right box
    ax.plot([cx + 0.9, 10.0 - box_w / 2], [cy + 0.5, 4.4 - box_h / 2],
            color=WHITE, lw=line_lw, alpha=line_alpha)
    # To bottom-left box
    ax.plot([cx - 0.9, 2.8 + box_w / 2], [cy - 0.5, 2.0 + box_h / 2],
            color=WHITE, lw=line_lw, alpha=line_alpha)
    # To bottom-right box
    ax.plot([cx + 0.9, 10.0 - box_w / 2], [cy - 0.5, 2.0 + box_h / 2],
            color=WHITE, lw=line_lw, alpha=line_alpha)

    # -- Bottom-left branding --
    ax.text(0.5, 0.35, "BK ADVISORS", ha="left", va="center",
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
    print("Done — 2 thumbnails generated.")
