"""
Summarize presidents scores
"""

election_sum = {}

with open('input.txt') as f:
    for row in f:
        temp = row.split()
        if temp[0] not in election_sum:
            election_sum[temp[0]] = int(temp[1])
        else:
            election_sum[temp[0]] += int(temp[1])
    f.close()

for i in sorted(election_sum.keys()):
    print("{} {}".format(i, election_sum[i]))
