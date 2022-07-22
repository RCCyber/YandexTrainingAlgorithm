"""
Find number of matches
"""
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(len(list1 + list2) - len(set(list1 + list2)))
