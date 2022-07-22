"""
Has the number been encountered before
"""
num_list = list(map(int, input().split()))
freq_dict = {}
for i in num_list:
    if i not in freq_dict.keys():
        freq_dict[i] = 1
        print("NO")
    elif i in freq_dict.keys():
        freq_dict[i] += 1
        print("YES")
