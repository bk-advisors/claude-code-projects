"""
Generate YouTube thumbnail images for Anatomy of a Good Point videos.
Output: youtube-thumb-intro.png, youtube-thumb-full-lecture.png
Style: polished (no xkcd), BKA brand colours, 1280x720 (YouTube recommended).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

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
    ax.text(6.4, 5.8, "The Idea That",
            ha="center", va="center",
            fontsize=42, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(6.4, 4.9, "Won the Room",
            ha="center", va="center",
            fontsize=42, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif")

    # -- Two contrasting figures side by side --
    # Left: data-heavy approach (X mark)
    left_cx = 3.8
    right_cx = 9.0
    fig_y = 2.5

    # Left box — the losing approach
    rounded_box(ax, left_cx, fig_y, 3.2, 2.2, "",
                fc=RED, ec=RED, lw=0, fontsize=14, textcolor=WHITE, alpha=0.25)
    ax.text(left_cx, fig_y + 0.55, "12 minutes", ha="center", va="center",
            fontsize=20, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(left_cx, fig_y - 0.1, "of data", ha="center", va="center",
            fontsize=20, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(left_cx, fig_y - 0.75, "Polite nods.", ha="center", va="center",
            fontsize=14, color=WHITE, fontfamily="sans-serif",
            fontstyle="italic", alpha=0.7)

    # Right box — the winning approach
    rounded_box(ax, right_cx, fig_y, 3.2, 2.2, "",
                fc=GREEN, ec=GREEN, lw=0, fontsize=14, textcolor=WHITE, alpha=0.3)
    ax.text(right_cx, fig_y + 0.55, "90 seconds", ha="center", va="center",
            fontsize=20, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(right_cx, fig_y - 0.1, "of structure", ha="center", va="center",
            fontsize=20, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(right_cx, fig_y - 0.75, "Funded.", ha="center", va="center",
            fontsize=14, color=WHITE, fontfamily="sans-serif",
            fontstyle="italic", alpha=0.7)

    # VS divider
    c = Circle((6.4, fig_y), 0.38, facecolor=WHITE, edgecolor=WHITE,
               linewidth=0, alpha=0.15)
    ax.add_patch(c)
    ax.text(6.4, fig_y, "vs", ha="center", va="center",
            fontsize=16, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- Bottom branding --
    ax.text(0.5, 0.35, "BK Advisors", ha="left", va="center",
            fontsize=14, fontweight="bold", color=WHITE, alpha=0.7,
            fontfamily="sans-serif")
    ax.text(12.3, 0.35, "Lecture 1 Intro", ha="right", va="center",
            fontsize=14, color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    save(fig, "youtube-thumb-intro.png")


# ============================================================================
# THUMBNAIL 2 — Full Lecture
# ============================================================================

def draw_full_lecture_thumb():
    fig, ax = new_fig(BLUE)

    # -- Title --
    ax.text(6.4, 6.3, "The Anatomy of a Good Point",
            ha="center", va="center",
            fontsize=34, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- "FULL LECTURE" badge --
    rounded_box(ax, 11.3, 6.65, 2.4, 0.65, "FULL LECTURE",
                fc=GREEN, ec=GREEN, lw=0, fontsize=16, textcolor=WHITE)

    # -- 4-part compass framework --
    cx, cy = 6.4, 3.1

    # Central circle: "The Point"
    center_r = 0.7
    c = Circle((cx, cy), center_r, facecolor=LBLUE, edgecolor=WHITE,
               linewidth=2.5)
    ax.add_patch(c)
    ax.text(cx, cy + 0.12, "The", ha="center", va="center",
            fontsize=13, color=WHITE, fontfamily="sans-serif")
    ax.text(cx, cy - 0.2, "Point", ha="center", va="center",
            fontsize=15, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # Four surrounding elements
    box_w, box_h = 2.4, 0.8
    elements = [
        # (x, y, label, subtitle, color)
        (cx, 5.0, "Why It's True", "Reasoning", GREEN),
        (2.6, cy, "Zoom In", "Evidence", RED),
        (10.2, cy, "Zoom Out", "Evidence", TEAL),
        (cx, 1.2, "Who Cares?", "Impact", ORANGE),
    ]

    arrow_props = dict(arrowstyle="-|>", color=WHITE, lw=2.5)
    pad = 0.1

    for bx, by, label, subtitle, color in elements:
        rounded_box(ax, bx, by, box_w, box_h, "",
                    fc=color, ec=color, lw=0, fontsize=14, textcolor=WHITE)
        ax.text(bx, by + 0.1, label, ha="center", va="center",
                fontsize=14, fontweight="bold", color=WHITE,
                fontfamily="sans-serif")
        ax.text(bx, by - 0.2, subtitle, ha="center", va="center",
                fontsize=10, color=WHITE, fontfamily="sans-serif",
                alpha=0.8)

    # Arrows from centre to each box
    # Up to "Why It's True"
    ax.annotate("", xy=(cx, 5.0 - box_h / 2 - pad),
                xytext=(cx, cy + center_r + pad),
                arrowprops=arrow_props)
    # Left to "Zoom In"
    ax.annotate("", xy=(2.6 + box_w / 2 + pad, cy),
                xytext=(cx - center_r - pad, cy),
                arrowprops=arrow_props)
    # Right to "Zoom Out"
    ax.annotate("", xy=(10.2 - box_w / 2 - pad, cy),
                xytext=(cx + center_r + pad, cy),
                arrowprops=arrow_props)
    # Down to "Who Cares?"
    ax.annotate("", xy=(cx, 1.2 + box_h / 2 + pad),
                xytext=(cx, cy - center_r - pad),
                arrowprops=arrow_props)

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
    print("Done — 2 thumbnails generated.")
