import numpy as np
import matplotlib.pyplot as plt

p1result = np.loadtxt("population transfer1.txt")
p2result = np.loadtxt("population transfer2.txt")
p3result = np.loadtxt("population transfer3.txt")

# Analyze the results
combined_results = np.array([p1result, p2result, p3result])

sums = np.sum(combined_results, axis=0)
means = np.mean(combined_results, axis=0)

uncertainty = np.std(sums)
variations = np.var(means)

plt.figure(figsize=(8, 6))
plt.hist(sums, bins=30, density=True, edgecolor='black', alpha=0.7)
plt.xlabel("Sum of states")
plt.ylabel("Probability")
plt.title("Distribution of Sums")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(means, bins=30, density=True, edgecolor='black', alpha=0.7)
plt.xlabel("Mean of probabilities")
plt.ylabel("Probability")
plt.title("Distribution of Means")
plt.grid(True)
plt.show()

print("Uncertainty in Sums:", uncertainty)
print("Variations in Means:", variations)
