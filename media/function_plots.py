import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
OUTPUT_DIR = Path(__file__).parent

def plot_l1_l2_norms(k: float = 1.2) -> None:
    """Plot L1 and L2 norms over the interval [-k, k].

    Args:
        k: Half-width of the x-axis interval.
    """
    x = np.linspace(-k, k, 500)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(x, np.abs(x), color="steelblue")
    axes[0].set_title("L1 Norm  $|x|$")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("$\\|x\\|_1$")
    axes[0].set_xlim(-k, k)

    axes[1].plot(x, x**2, color="darkorange")
    axes[1].set_title("L2 Norm (squared)  $x^2$")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("$\\|x\\|_2^2$")
    axes[1].set_xlim(-k, k)

    for ax in axes:
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
        ax.grid(True, alpha=0.3)

    fig.tight_layout()
    plt.savefig(OUTPUT_DIR / "plots/l1-vs-l2-norms.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    plot_l1_l2_norms()
