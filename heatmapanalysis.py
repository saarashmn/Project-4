import numpy as np
import matplotlib.pyplot as plt

# 
p1result = np.loadtxt("population transfer1.txt")
p2result = np.loadtxt("population transfer2.txt")
p3result = np.loadtxt("population transfer3.txt")

# 
combined_results = np.array([p1result, p2result, p3result])

sums = np.sum(combined_results, axis=0)
means = np.mean(combined_results, axis=0)

uncertainty = np.std(sums)
variations = np.var(means)

# 
alpha_values = np.linspace(0.1, 10, 30)

grid_sums = np.zeros((len(alpha_values), len(sums)))
grid_means = np.zeros((len(alpha_values), len(means)))

for i, alpha in enumerate(alpha_values):
    shifted_sums = sums + alpha
    shifted_means = means + alpha
    grid_sums[i] = shifted_sums
    grid_means[i] = shifted_means

fig, ax = plt.subplots(figsize=(10, 6))
heatmap_sums = ax.imshow(grid_sums, cmap='YlGnBu', aspect='auto')
cbar_sums = fig.colorbar(heatmap_sums, ax=ax)
cbar_sums.set_label("Sum of probabilities")
ax.set_xlabel("transfer rate")
ax.set_ylabel("Alpha")
ax.set_title("Likelihood vs. Alpha")

fig, ax = plt.subplots(figsize=(10, 6))
heatmap_means = ax.imshow(grid_means, cmap='YlGnBu', aspect='auto')
cbar_means = fig.colorbar(heatmap_means, ax=ax)
cbar_means.set_label("Mean of Rolls")
ax.set_xlabel("transfer rate")
ax.set_ylabel("Alpha")
ax.set_title("Heatmap of Means with Different Alpha Values")

plt.show()
