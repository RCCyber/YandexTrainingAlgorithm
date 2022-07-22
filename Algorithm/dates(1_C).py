"""
EU(0) - dd:mm:yy, US(1) - mm:dd:yy
"""
a = list(map(int, input().split()))


def date_decision(a):
    if a[0] == a[1]:
        return 1
    elif a[0] == 12:
        if a[1] < 12:
            return 0
        else:
            return 1
    elif a[1] == 12:
        if a[0] < 12:
            return 0
        else:
            return 1
    elif a[1] > a[0]:
        if a[1] > 12:
            return 1
        else:
            return 0
    elif a[0] > a[1]:
        if a[0] > 12:
            return 1
        else:
            return 0
"""
EU(0) - dd:mm:yy, US(1) - mm:dd:yy
12-12, 10-10
12-11, 11-12
10-9, 13-9
9-10, 9-13
"""

print(date_decision(a))
