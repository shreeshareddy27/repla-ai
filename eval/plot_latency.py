import json
import matplotlib.pyplot as plt

BRAND_BLUE  = "#6FA8DC"
BRAND_GREEN = "#B7E07A"
DARK_BG     = "#0b0f14"   # deep navy/black
GRID        = "#233042"

with open("results/latency.json") as f:
    data = json.load(f)

latencies = data["all_runs"]

fig, ax = plt.subplots(figsize=(8,5))
fig.patch.set_facecolor(DARK_BG)
ax.set_facecolor(DARK_BG)

ax.hist(latencies, bins=8, color=BRAND_BLUE, edgecolor="#E6EEF8", alpha=0.9)
ax.axvline(data["median_ms"], color=BRAND_GREEN, linestyle="--", linewidth=2, label="Median")

ax.set_title("Repla.ai Local LLM Latency Distribution", fontsize=12, color="#E6EEF8")
ax.set_xlabel("Latency (ms)", color="#E6EEF8")
ax.set_ylabel("Frequency", color="#E6EEF8")

ax.tick_params(colors="#E6EEF8")
for spine in ax.spines.values():
    spine.set_color("#E6EEF8")

ax.grid(True, color=GRID, alpha=0.35, linewidth=0.8)
ax.legend(facecolor=DARK_BG, edgecolor="#E6EEF8", labelcolor="#E6EEF8")

plt.tight_layout()
plt.savefig("docs/figures/latency_distribution.png", dpi=300, facecolor=fig.get_facecolor())
plt.close()

print("Saved branded latency graph -> docs/figures/latency_distribution.png")
