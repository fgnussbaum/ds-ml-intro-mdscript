"""Generate precision / bias / accuracy visualizations — 1D strip and 2D dartboard."""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

RNG = np.random.default_rng(42)
N = 40
TARGET = 0.0

SCENARIOS = [
    {
        "title": "Unbiased, Imprecise",
        "subtitle": "(high noise, no bias)",
        "mean_2d": (0.0, 0.0),
        "std": 1.1,
    },
    {
        "title": "Biased, Precise",
        "subtitle": "(low noise, systematic bias)",
        "mean_2d": (1.4, 0.9),
        "std": 0.22,
    },
    {
        "title": "Accurate",
        "subtitle": "(low noise, no bias)",
        "mean_2d": (0.0, 0.0),
        "std": 0.22,
    },
]

COLOR_POINTS = "#4878CF"
COLOR_TARGET = "#E84040"
COLOR_MEAN = "#FF8C00"


# ---------------------------------------------------------------------------
# 1-D strip plot
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), sharey=True)
fig.suptitle("Precision, Bias, and Accuracy — 1-D", fontsize=13, fontweight="bold", y=1.01)

for ax, s in zip(axes, SCENARIOS):
    x1d = RNG.normal(s["mean_2d"][0], s["std"], N)
    jitter = RNG.uniform(-0.18, 0.18, N)

    ax.scatter(x1d, jitter, alpha=0.6, s=45, color=COLOR_POINTS, zorder=3)

    ax.axvline(TARGET, color=COLOR_TARGET, linewidth=2, linestyle="--", zorder=4, label="Target")
    ax.axvline(x1d.mean(), color=COLOR_MEAN, linewidth=2, linestyle="-", zorder=4, label=f"Mean = {x1d.mean():.2f}")

    ax.set_xlim(-3.8, 3.8)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel("Measured value")
    ax.set_title(f"{s['title']}\n{s['subtitle']}", fontsize=12)
    ax.legend(fontsize=23, loc="upper right")
    ax.spines[["top", "right", "left"]].set_visible(False)

plt.tight_layout()
out_1d = OUTPUT_DIR / "precision_bias_accuracy_1d.png"
plt.savefig(out_1d, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {out_1d}")


# ---------------------------------------------------------------------------
# 2-D dartboard (Zielscheibe)
# ---------------------------------------------------------------------------

RINGS = [2.5, 2.0, 1.5, 1.0, 0.5]
RING_COLORS = ["#f9f9f9", "#e8e8e8", "#d0d0d0", "#b8b8b8", "#a0a0a0"]

fig, axes = plt.subplots(1, 3, figsize=(13, 5))
# fig.suptitle("Precision, Bias, and Accuracy — 2-D (Dartboard)", fontsize=13, fontweight="bold", y=1.01)

for ax, s in zip(axes, SCENARIOS):
    # Draw rings from outside in
    for r, color in zip(RINGS, RING_COLORS):
        circle = plt.Circle((0, 0), r, color=color, zorder=1)
        ax.add_patch(circle)
        circle_edge = plt.Circle((0, 0), r, fill=False, edgecolor="#999999", linewidth=0.8, zorder=2)
        ax.add_patch(circle_edge)

    # Bullseye
    bullseye = plt.Circle((0, 0), 0.18, color=COLOR_TARGET, zorder=5, label="Real value")
    ax.add_patch(bullseye)

    # Crosshairs
    ax.axhline(0, color="#cccccc", linewidth=0.6, zorder=3)
    ax.axvline(0, color="#cccccc", linewidth=0.6, zorder=3)

    # Measurements
    mx, my = s["mean_2d"]
    x2d = RNG.normal(mx, s["std"], N)
    y2d = RNG.normal(my, s["std"], N)

    ax.scatter(x2d, y2d, alpha=0.7, s=50, color=COLOR_POINTS, zorder=10, label="Shots")

    # Show centroid
    cx, cy = x2d.mean(), y2d.mean()
    ax.plot(cx, cy, marker="x", markersize=12, color=COLOR_MEAN,
            markeredgewidth=2.5, zorder=11, label=f"Mean")

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{s['title']}\n{s['subtitle']}", fontsize=16, y=1.03)
    ax.legend(fontsize=12, loc="upper right")

plt.tight_layout()
out_2d = OUTPUT_DIR / "precision_bias_accuracy_2d.png"
plt.savefig(out_2d, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {out_2d}")
