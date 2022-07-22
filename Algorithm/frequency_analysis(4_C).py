"""
Analyze the text and output the words in descending order
"""

freq_count = {}

with open('input.txt') as f:
    for row in f:
        temp = row.split()
        if len(temp) == 1:
            if temp[0] not in freq_count:
                freq_count[temp[0]] = 1
            else:
                freq_count[temp[0]] += 1
        else:
            for j in temp:
                if j not in freq_count:
                    freq_count[j] = 1
                else:
                    freq_count[j] += 1
    f.close()

sort_set = [(j, i) for i, j in sorted(freq_count.items(), reverse=False)]
for row in sorted(sort_set, key=lambda x: x[0], reverse=True):
    print(row[1])
