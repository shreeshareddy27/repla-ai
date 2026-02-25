import numpy as np
import matplotlib.pyplot as plt

BRAND_BLUE  = "#6FA8DC"
BRAND_GREEN = "#B7E07A"
BRAND_PINK  = "#F4A6A6"
DARK_BG     = "#0b0f14"
TEXT        = "#E6EEF8"
GRID        = "#233042"

labels = [
    "External\nTransmission",
    "3rd Party\nRetention",
    "API\nDependency",
    "Offline\nCapability",
    "Attack\nSurface"
]

# Scores: 1 = low risk (better), 5 = high risk (worse)
repla = [1, 1, 1, 1, 2]
cloud = [5, 4, 5, 5, 4]

N = len(labels)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

repla = repla + repla[:1]
cloud = cloud + cloud[:1]

fig = plt.figure(figsize=(7,7))
fig.patch.set_facecolor(DARK_BG)
ax = plt.subplot(111, polar=True)
ax.set_facecolor(DARK_BG)

# Grid + ticks
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, color=TEXT, fontsize=10)

ax.set_rlabel_position(0)
ax.set_yticks([1,2,3,4,5])
ax.set_yticklabels(["1","2","3","4","5"], color=TEXT, fontsize=9)
ax.grid(color=GRID, alpha=0.35, linewidth=0.8)

# Plot lines
ax.plot(angles, repla, color=BRAND_GREEN, linewidth=2, label="Repla.ai (Local)")
ax.fill(angles, repla, color=BRAND_GREEN, alpha=0.12)

ax.plot(angles, cloud, color=BRAND_PINK, linewidth=2, label="Typical Cloud AI")
ax.fill(angles, cloud, color=BRAND_PINK, alpha=0.10)

ax.set_title("Privacy Surface Comparison (Lower = Better)", color=TEXT, fontsize=13, pad=18)
leg = ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.15), frameon=True)
leg.get_frame().set_facecolor(DARK_BG)
leg.get_frame().set_edgecolor(TEXT)
for t in leg.get_texts():
    t.set_color(TEXT)

plt.tight_layout()
plt.savefig("docs/figures/privacy_radar.png", dpi=300, facecolor=fig.get_facecolor())
plt.close()

print("Saved -> docs/figures/privacy_radar.png")
