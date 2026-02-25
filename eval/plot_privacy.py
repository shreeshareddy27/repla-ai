import numpy as np
import matplotlib.pyplot as plt

labels = [
    "External Transmission",
    "3rd Party Retention",
    "API Dependency",
    "Offline Capability",
    "Attack Surface"
]

# Scores (1 = low risk, 5 = high risk)
repla = [1, 1, 1, 1, 2]
cloud = [5, 4, 5, 5, 4]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

repla += repla[:1]
cloud += cloud[:1]
angles += angles[:1]

plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

ax.plot(angles, repla)
ax.fill(angles, repla, alpha=0.1)

ax.plot(angles, cloud)
ax.fill(angles, cloud, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_yticklabels([])
plt.title("Privacy Surface Comparison (Lower = Better)")

plt.tight_layout()
plt.savefig("docs/figures/privacy_radar.png")
plt.close()

print("Saved to docs/figures/privacy_radar.png")
