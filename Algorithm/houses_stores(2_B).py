"""
1 - living house, 2 - shop, 0 - office
Task: Find maximum from minimum distance between 1 and 2
Example:
    Input: 1 2 0 0 1 0 2 1 0 2 Output: 2
    Input: 0 1 0 0 1 2 2 1 0 2 Output: 4
    Input: 2 0 1 1 0 1 0 2 1 2 Output: 3
"""
a = list(map(int, input().split()))
counter = 0
count_lst = []
for i in range(len(a)):
    if a[i] == 1 and i+1 != len(a):
        print("Found 1")
        left_right = []
        for j in range(i+1, len(a)):
            counter += 1
            if a[j] == 2:
                print("Found right 2")
                left_right.append(counter)
                break
        counter = 0
        for j in range(i-1, -1, -1):
            counter += 1
            if a[j] == 2:
                print("Found left 2")
                left_right.append(counter)
                break
        count_lst.append(min(left_right))
        counter = 0

print("Final: ", max(count_lst))
