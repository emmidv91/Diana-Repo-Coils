"""Generate reproducible noisy linear data and fit it using lmfit."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model

OUTPUT = Path(__file__).resolve().parent / "linear_fit.pdf"
RNG_SEED = 42
TRUE_SLOPE = 2.5
TRUE_INTERCEPT = 1.0
NOISE_STD = 2.0


def linear(x, slope, intercept):
    return slope * x + intercept


def main():
    rng = np.random.default_rng(RNG_SEED)
    x = np.linspace(0, 10, 60)
    y = linear(x, TRUE_SLOPE, TRUE_INTERCEPT) + rng.normal(0, NOISE_STD, size=x.size)

    model = Model(linear)
    result = model.fit(y, x=x, slope=1.0, intercept=0.0)
    print(result.fit_report())
    slope = result.params["slope"].value
    intercept = result.params["intercept"].value

    x_smooth = np.linspace(x.min(), x.max(), 300)
    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    ax.scatter(x, y, s=24, alpha=0.7, label="Simulated data")
    ax.plot(x_smooth, linear(x_smooth, slope, intercept), linewidth=2,
            label=f"lmfit: y = {slope:.3f}x + {intercept:.3f}")
    ax.plot(x_smooth, linear(x_smooth, TRUE_SLOPE, TRUE_INTERCEPT), "--",
            linewidth=1, alpha=0.7, label="True model")
    ax.set(xlabel="x", ylabel="y", title="Linear fit of Gaussian-noise data")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.savefig(OUTPUT, format="pdf")
    plt.close(fig)
    print(f"Saved plot to: {OUTPUT}")


if __name__ == "__main__":
    main()
