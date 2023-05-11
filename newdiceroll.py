import numpy as np
import matplotlib.pyplot as plt


p1result = np.loadtxt("population transfer1.txt")
p2result = np.loadtxt("population transfer2.txt")
p3result = np.loadtxt("population transfer3.txt")


combined_results = np.array([p1result, p2result, p3result])

sums = np.sum(combined_results, axis=0)
means = np.mean(combined_results, axis=0)

uncertainty = np.std(sums)
variations = np.var(means)

# Plot the data with uncertainty and variations
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(range(len(sums)), sums, label="Sums", color='blue')
ax.fill_between(range(len(sums)), sums - uncertainty, sums + uncertainty,
                color='blue', alpha=0.2)
ax.plot(range(len(means)), means, label="Means", color='green')
ax.fill_between(range(len(means)), means - variations, means + variations,
                color='green', alpha=0.2)

ax.set_xlabel("transfer rate")
ax.set_ylabel("Value")
ax.set_title("population transfer Uncertainty and Variations")
ax.legend()

plt.grid(True)
plt.show()

print("Uncertainty in Sums:", uncertainty)
print("Variations in Means:", variations)
