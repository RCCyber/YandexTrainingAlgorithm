"""
Estimate time, spend on searching diploma
n - folders quantity
a - diplomas quantity in each folder
Example:
    Input: 2       Output: 1
           2 1
    Input:  3
            2 4 5
            1 3 4
"""
n = int(input())
a = list(map(int, input().split()))
print(sum(a) - max(a))
