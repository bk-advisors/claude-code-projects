"""
Generate still-frame title cards for the BK Advisors YouTube channel intro.
Output: frame-01-logo.png through frame-05-cta.png (1920x1080 each).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import FancyBboxPatch, Circle

# -- Constants ---------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
LOGO_PATH = os.path.join(REPO_DIR, "slide-master", "BKA_Enhanced_Logo_Apr2025.png")

DPI = 100  # 1920x1080 at 19.2x10.8 inches
FIG_W, FIG_H = 19.2, 10.8

# BKA brand colours
BLUE = "#005CB9"
LBLUE = "#00A1DF"
GREEN = "#83BD00"
TEAL = "#3E9B6E"
RED = "#E24A3F"
ORANGE = "#FA7650"
AMBER = "#F8A623"
YELLOW = "#FED141"
WHITE = "#FFFFFF"
DARK = "#333333"


# -- Helpers -----------------------------------------------------------------

def new_fig(bg_color=BLUE):
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    path = os.path.join(SCRIPT_DIR, name)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0,
                facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


def add_logo(ax, cx, cy, zoom=0.45):
    """Place the BKA logo image centred at (cx, cy)."""
    logo = mpimg.imread(LOGO_PATH)
    # Logo image is square-ish; scale to fit
    img_h, img_w = logo.shape[:2]
    # Display size in data coords
    disp_w = 4.5 * zoom / 0.45
    disp_h = disp_w * (img_h / img_w)
    extent = [cx - disp_w / 2, cx + disp_w / 2,
              cy - disp_h / 2, cy + disp_h / 2]
    ax.imshow(logo, extent=extent, aspect="auto", zorder=5,
              interpolation="lanczos")


def add_small_logo(ax, x, y, zoom=0.18):
    """Place a small logo at the given position."""
    add_logo(ax, x, y, zoom=zoom)


def thin_line(ax, y, color=WHITE, alpha=0.15):
    """Draw a subtle horizontal rule."""
    ax.plot([3, FIG_W - 3], [y, y], color=color, lw=1, alpha=alpha)


# ============================================================================
# FRAME 1 — Logo Reveal
# ============================================================================

def draw_frame_01():
    fig, ax = new_fig()
    add_logo(ax, FIG_W / 2, FIG_H / 2 + 0.3, zoom=0.65)
    save(fig, "frame-01-logo.png")


# ============================================================================
# FRAME 2 — Tagline
# ============================================================================

def draw_frame_02():
    fig, ax = new_fig()

    # Small logo top-left
    add_small_logo(ax, 2.2, FIG_H - 1.5, zoom=0.16)

    # Tagline centred
    ax.text(FIG_W / 2, FIG_H / 2 + 0.3,
            "Connecting Dots, Delivering Results.",
            ha="center", va="center",
            fontsize=48, fontweight="bold", color=WHITE,
            fontfamily="sans-serif", fontstyle="italic")

    # Subtle underline accent
    thin_line(ax, FIG_H / 2 - 0.8, color=YELLOW, alpha=0.5)

    save(fig, "frame-02-tagline.png")


# ============================================================================
# FRAME 3 — Series Overview
# ============================================================================

def draw_frame_03():
    fig, ax = new_fig()

    # Small logo top-left
    add_small_logo(ax, 2.2, FIG_H - 1.5, zoom=0.16)

    # Header
    ax.text(FIG_W / 2, FIG_H - 2.5,
            "Professional Skills for Global Health Consultants",
            ha="center", va="center",
            fontsize=34, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif")

    thin_line(ax, FIG_H - 3.3, color=WHITE, alpha=0.2)

    # Lecture list
    lectures = [
        ("1", "The Anatomy of a Good Point", GREEN),
        ("2", "Making Causal Arguments That Hold Up", ORANGE),
        ("3", "Inference and Intervention", LBLUE),
    ]

    start_y = 5.5
    spacing = 1.8

    for i, (num, title, accent) in enumerate(lectures):
        y = start_y - i * spacing

        # Accent dot
        dot = Circle((4.5, y), 0.22, facecolor=accent, edgecolor=accent)
        ax.add_patch(dot)
        ax.text(4.5, y, num, ha="center", va="center",
                fontsize=16, fontweight="bold", color=WHITE,
                fontfamily="sans-serif")

        # Title
        ax.text(5.3, y, title, ha="left", va="center",
                fontsize=28, fontweight="bold", color=WHITE,
                fontfamily="sans-serif")

    save(fig, "frame-03-series.png")


# ============================================================================
# FRAME 4 — Speaker Card
# ============================================================================

def draw_frame_04():
    fig, ax = new_fig()

    # Small logo top-left
    add_small_logo(ax, 2.2, FIG_H - 1.5, zoom=0.16)

    # Name
    ax.text(FIG_W / 2, 7.5, "Matthew Kuch",
            ha="center", va="center",
            fontsize=52, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # Company
    ax.text(FIG_W / 2, 6.3, "BK Advisors",
            ha="center", va="center",
            fontsize=30, color=LBLUE, fontweight="bold",
            fontfamily="sans-serif")

    thin_line(ax, 5.5, color=WHITE, alpha=0.2)

    # Credentials
    credentials = [
        "CHAI Uganda",
        "Gavi Geneva",
        "Deloitte USAID / DFID",
    ]

    cred_y = 4.6
    for j, cred in enumerate(credentials):
        y = cred_y - j * 1.0

        # Small accent dash
        ax.plot([7.5, 8.0], [y, y], color=YELLOW, lw=3, solid_capstyle="round")

        ax.text(8.4, y, cred, ha="left", va="center",
                fontsize=24, color=WHITE, fontfamily="sans-serif")

    save(fig, "frame-04-speaker.png")


# ============================================================================
# FRAME 5 — Subscribe CTA
# ============================================================================

def draw_frame_05():
    fig, ax = new_fig()

    # Logo centred, medium size
    add_logo(ax, FIG_W / 2, FIG_H / 2 + 1.2, zoom=0.45)

    # Subscribe text
    ax.text(FIG_W / 2, 2.5,
            "Subscribe  ·  New lectures monthly",
            ha="center", va="center",
            fontsize=30, fontweight="bold", color=WHITE,
            fontfamily="sans-serif")

    # Subtle accent bar under text
    bar = FancyBboxPatch(
        (FIG_W / 2 - 4.5, 1.8), 9.0, 0.12,
        boxstyle="round,pad=0.05", facecolor=YELLOW, edgecolor="none",
        alpha=0.6)
    ax.add_patch(bar)

    save(fig, "frame-05-cta.png")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("Generating channel intro frames...")
    draw_frame_01()
    draw_frame_02()
    draw_frame_03()
    draw_frame_04()
    draw_frame_05()
    print("Done — 5 frames generated.")
