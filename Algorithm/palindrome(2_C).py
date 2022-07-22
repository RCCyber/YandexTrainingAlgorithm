"""
You have to make palindrome and estimate a cost

Examples:
    Input: a, Output: 0
    Input: ab, Output: 1
    Input: abc, Output: 1
"""
a = list(input())
counter = 1
if len(a) == 1:  # 1 char == zero cost
    print(0)
else:
    rev = a[::-1]
    if a == rev:
        print(0)  # zero cost(similar with word in reverse)
    elif len(a) <= 10000:
        for i in range(len(a) // 2):
            if a[i] != a[-1 - i]:
                a[i], a[-1 - i] = a[-1 - i], a[i]
                if a != rev:
                    counter += 1
        print(counter)


