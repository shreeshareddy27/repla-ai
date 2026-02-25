import matplotlib.pyplot as plt

BRAND_BLUE  = "#6FA8DC"
BRAND_GREEN = "#B7E07A"
BRAND_PINK  = "#F4A6A6"
DARK_BG     = "#0b0f14"
GRID        = "#233042"
TEXT        = "#E6EEF8"

# Adjustable assumptions
tokens_per_request = 500
price_per_million_tokens = 5  # USD

cloud_cost = (tokens_per_request / 1_000_000) * price_per_million_tokens
local_cost = 0

labels = ["Local (Ollama)", "Cloud API"]
costs = [local_cost, cloud_cost]
colors = [BRAND_GREEN, BRAND_PINK]

fig, ax = plt.subplots(figsize=(6,4))
fig.patch.set_facecolor(DARK_BG)
ax.set_facecolor(DARK_BG)

ax.bar(labels, costs, color=colors, edgecolor=TEXT, alpha=0.95)

ax.set_title("Cost per Email Generation", fontsize=12, color=TEXT)
ax.set_ylabel("USD per Request", color=TEXT)

ax.tick_params(colors=TEXT)
for spine in ax.spines.values():
    spine.set_color(TEXT)

ax.grid(True, axis="y", color=GRID, alpha=0.35, linewidth=0.8)

# Annotate cloud bar value for clarity
ax.text(1, cloud_cost, f"${cloud_cost:.4f}", ha="center", va="bottom", color=TEXT, fontsize=10)

plt.tight_layout()
plt.savefig("docs/figures/cost_comparison.png", dpi=300, facecolor=fig.get_facecolor())
plt.close()

print("Saved branded cost graph -> docs/figures/cost_comparison.png")
