"""Recreate the portfolio chart from the report's two mesh summaries.

Run from any directory: python scripts/plot_mesh_comparison.py
This plots reported results; it does not run an ANSYS simulation.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "data/mesh_comparison.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
fig.patch.set_facecolor("#F5F7FA")
metrics = [
    ("max_total_displacement_in", "Maximum total displacement", "in", 7),
    ("max_normal_stress_x_psi", "Maximum normal stress in x", "psi", 0),
]
for ax, (key, title, unit, precision) in zip(axes, metrics):
    values = [float(row[key]) for row in rows]
    signed_change = (values[1] - values[0]) / abs(values[0]) * 100
    bars = ax.bar([row["mesh"] for row in rows], values,
                  color=["#173F5F", "#B87952"], width=0.52, zorder=3)
    ax.set_facecolor("#F5F7FA")
    ax.set_title(title, loc="left", fontsize=14, weight="bold", pad=38,
                 color="#142C40")
    ax.text(0, 1.03, f"{signed_change:+.2f}% vs. initial mesh",
            transform=ax.transAxes, color="#6D4B37", fontsize=11)
    ax.set_ylabel(unit)
    ax.set_ylim(0, max(values) * 1.23)
    ax.grid(axis="y", alpha=0.18, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#CBD4DD")
    ax.tick_params(axis="both", length=0)
    for bar, value in zip(bars, values):
        label = f"{value:,.0f}" if precision == 0 else f"{value:.{precision}f}".rstrip("0")
        ax.text(bar.get_x() + bar.get_width() / 2,
                value + max(values) * 0.035, label,
                ha="center", fontsize=12, color="#142C40", weight="bold")

fig.suptitle("MESH REFINEMENT | RESPONSE SENSITIVITY", x=0.075, y=0.98,
             ha="left", fontsize=17, weight="bold", color="#142C40")
fig.text(0.075, 0.035,
         "Source: final project report, Table 2. Two mesh levels; convergence is not established.",
         fontsize=10, color="#516579")
fig.subplots_adjust(left=0.08, right=0.97, top=0.74, bottom=0.15, wspace=0.30)
destination = ROOT / "assets/mesh-response.png"
fig.savefig(destination, dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)
print(destination)
