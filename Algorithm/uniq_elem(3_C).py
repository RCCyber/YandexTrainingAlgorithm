"""
Find unique element in list
"""
elem_list = list(map(int, input().split()))
freq_dict = {}

for i in elem_list:
    if i not in freq_dict:
        freq_dict[i] = 1
    else:
        freq_dict[i] += 1

uniq_list = [i for i in freq_dict if freq_dict[i] == 1]
print(*uniq_list)
