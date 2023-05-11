import random


def populationtransfer(n, num_rolls):
    results = []
    for _ in range(num_rolls):
        roll = random.gauss(1, n)
        results.append(roll)
    return results

num_rolls = 10000

particle1 = 3
pt1 = populationtransfer(particle1, num_rolls)

particle2 = 3
pt2 = populationtransfer(particle2, num_rolls)

particle3 = 3
pt3 = populationtransfer(particle3, num_rolls)

with open("population transfer1.txt", "w") as f:
    f.write("\n".join(map(str, pt1)))

with open("population transfer2.txt", "w") as f:
    f.write("\n".join(map(str, pt2)))

with open("population transfer3.txt", "w") as f:
    f.write("\n".join(map(str, pt3)))
