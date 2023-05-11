import numpy as np
import matplotlib.pyplot as plt

p1result = np.loadtxt("population transfer1.txt")
p2result = np.loadtxt("population transfer2.txt")
p3result = np.loadtxt("population transfer3.txt")

# Analyze the results
combined_results = np.array([p1result, p2result, p3result])

sums = np.sum(combined_results, axis=0)
means = np.mean(combined_results, axis=0)

alpha_values = np.linspace(0.1, 3, 30)

# Calculate uncertainty and variation for each alpha
uncertainty_values = []
variation_values = []

for alpha in alpha_values:
    shifted_sums = sums + alpha
    uncertainty = np.std(shifted_sums)
    uncertainty_values.append(uncertainty)

    shifted_means = means + alpha
    variation = np.var(shifted_means)
    variation_values.append(variation)

# Create the heatmaps
fig, ax = plt.subplots(figsize=(10, 6))
heatmap_uncertainty = ax.imshow(np.array([uncertainty_values]), cmap='YlGnBu', aspect='auto')
cbar_uncertainty = fig.colorbar(heatmap_uncertainty, ax=ax)
cbar_uncertainty.set_label("Uncertainty")
ax.set_xlabel("Alpha")
ax.set_ylabel("Uncertainty")
ax.set_title("Uncertainty vs Alpha")

fig, ax = plt.subplots(figsize=(10, 6))
heatmap_variation = ax.imshow(np.array([variation_values]), cmap='YlGnBu', aspect='auto')
cbar_variation = fig.colorbar(heatmap_variation, ax=ax)
cbar_variation.set_label("Variation")
ax.set_xlabel("Alpha")
ax.set_ylabel("Variation")
ax.set_title("Variation vs Alpha")

plt.show()
