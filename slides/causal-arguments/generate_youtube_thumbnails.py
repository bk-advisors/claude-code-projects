"""
Generate YouTube thumbnail images for Causal Arguments videos.
Output: youtube-thumb-intro.png, youtube-thumb-full-lecture.png
Style: polished (no xkcd), BKA brand colours, 1280x720 (YouTube recommended).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np

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

    # -- Main title --
    ax.text(6.4, 5.6, "Correlation  ≠  Causation",
            ha="center", va="center",
            fontsize=44, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # -- Divider line --
    ax.plot([6.4, 6.4], [1.2, 4.6], color=WHITE, lw=1.5, alpha=0.4)

    # -- LEFT SIDE: Correlation (trend line) --
    left_cx = 3.4

    # Simple rising trend with scatter
    np.random.seed(42)
    xs = np.linspace(1.2, 5.6, 12)
    ys_base = 1.5 + 1.8 * ((xs - 1.2) / 4.4)
    ys = ys_base + np.random.normal(0, 0.18, len(xs))

    ax.plot(xs, ys, "o", color=LBLUE, markersize=8, alpha=0.85, zorder=3)
    # Trend line
    z = np.polyfit(xs, ys, 1)
    ax.plot([1.2, 5.6], [np.polyval(z, 1.2), np.polyval(z, 5.6)],
            color=WHITE, lw=3, alpha=0.9, zorder=2)

    ax.text(left_cx, 1.0, "Correlation", ha="center", va="center",
            fontsize=22, fontweight="bold", color=LBLUE,
            fontfamily="sans-serif")

    # -- RIGHT SIDE: Causation (chain of arrows) --
    right_cx = 9.4
    chain_labels = ["X", "→", "M", "→", "Y"]
    chain_xs = [7.6, 8.2, 8.8, 9.4, 10.0]
    # Draw as linked circles with arrows
    step_labels = ["X", "M", "Y"]
    step_xs = [7.8, 9.4, 11.0]
    step_y = 3.0

    for i, (sx, label) in enumerate(zip(step_xs, step_labels)):
        c = Circle((sx, step_y), 0.42, facecolor=WHITE, edgecolor=WHITE,
                    linewidth=2, alpha=0.15)
        ax.add_patch(c)
        ax.text(sx, step_y, label, ha="center", va="center",
                fontsize=24, fontweight="bold", color=WHITE,
                fontfamily="sans-serif")

        # Arrow to next
        if i < len(step_xs) - 1:
            ax.annotate("", xy=(step_xs[i + 1] - 0.55, step_y),
                        xytext=(sx + 0.55, step_y),
                        arrowprops=dict(arrowstyle="-|>", color=GREEN,
                                        lw=3.5))

    ax.text(right_cx, 1.0, "Causation", ha="center", va="center",
            fontsize=22, fontweight="bold", color=GREEN,
            fontfamily="sans-serif")

    # -- Bottom branding --
    ax.text(0.5, 0.35, "BK Advisors", ha="left", va="center",
            fontsize=14, fontweight="bold", color=WHITE, alpha=0.7,
            fontfamily="sans-serif")
    ax.text(12.3, 0.35, "Lecture 2 Intro", ha="right", va="center",
            fontsize=14, color=WHITE, alpha=0.7,
            fontfamily="sans-serif")

    save(fig, "youtube-thumb-intro.png")


# ============================================================================
# THUMBNAIL 2 — Full Lecture
# ============================================================================

def draw_full_lecture_thumb():
    fig, ax = new_fig(BLUE)

    # -- Title --
    ax.text(6.4, 6.2, "Making Causal Arguments",
            ha="center", va="center",
            fontsize=36, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")
    ax.text(6.4, 5.5, "That Hold Up",
            ha="center", va="center",
            fontsize=36, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif")

    # -- "FULL LECTURE" badge (top-right) --
    rounded_box(ax, 11.3, 6.65, 2.4, 0.65, "FULL LECTURE",
                fc=GREEN, ec=GREEN, lw=0, fontsize=16, textcolor=WHITE)

    # -- Central circle: "X caused Y?" --
    cx, cy = 6.4, 2.8
    center_r = 0.75
    c = Circle((cx, cy), center_r, facecolor=LBLUE, edgecolor=WHITE,
               linewidth=2.5)
    ax.add_patch(c)
    ax.text(cx, cy, "X caused\nY?", ha="center", va="center",
            fontsize=16, fontweight="bold", color=WHITE,
            fontfamily="sans-serif", linespacing=1.1)

    # -- Three alternative boxes --
    box_w, box_h = 2.6, 0.85
    boxes = [
        # (x, y, label, color)
        (cx, 4.5, "Common Cause", RED),
        (2.8, cy, "Coincidence", ORANGE),
        (10.0, cy, "Reversed\nCausation", TEAL),
    ]

    for bx, by, label, color in boxes:
        rounded_box(ax, bx, by, box_w, box_h, label,
                    fc=color, ec=color, lw=0, fontsize=14, textcolor=WHITE)

    # -- Arrows from centre to boxes --
    arrow_props = dict(arrowstyle="-|>", color=WHITE, lw=2.5)
    pad = 0.1

    # Up
    ax.annotate("", xy=(cx, 4.5 - box_h / 2 - pad),
                xytext=(cx, cy + center_r + pad),
                arrowprops=arrow_props)
    # Left
    ax.annotate("", xy=(2.8 + box_w / 2 + pad, cy),
                xytext=(cx - center_r - pad, cy),
                arrowprops=arrow_props)
    # Right
    ax.annotate("", xy=(10.0 - box_w / 2 - pad, cy),
                xytext=(cx + center_r + pad, cy),
                arrowprops=arrow_props)

    # -- Bottom branding --
    ax.text(0.5, 0.35, "BK Advisors", ha="left", va="center",
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
