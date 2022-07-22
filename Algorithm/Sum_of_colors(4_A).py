"""
Print the sum of similar color values
"""
n = int(input())
numb_pair = []
sum_dict = {}
for i in range(n):
    temp = list(map(int, input().split()))
    numb_pair.append(temp)
for i in numb_pair:
    if i[0] not in sum_dict:
        sum_dict[i[0]] = i[1]
    else:
        sum_dict[i[0]] += i[1]
for key in sorted(sum_dict):
    print("%s %s" % (key, sum_dict[key]))
