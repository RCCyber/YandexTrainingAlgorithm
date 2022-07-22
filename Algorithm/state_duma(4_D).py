"""
Distribute 450 seats among the parties that participated in the elections
"""

with open('input.txt') as f:
    votes = [i.split() for i in f]
    digits = [int(i[-1]) for i in votes]
    private = sum(digits) / 450
    distribution = [i / private for i in digits]
    residuals = [(distribution[i], distribution[i] - int(distribution[i])) for i in range(len(distribution))]
    free_places = 450 - round(sum([int(i) for i in distribution]))
    residuals = sorted(residuals, key=lambda x: x[1], reverse=True)
    if sum([int(i) for i in distribution]) < 450:
        for i in range(free_places):
            distribution[distribution.index(residuals[i][0])] += 1
f.close()

for i in range(len(votes)):
    print(*votes[i][:-1], int(distribution[i]))
