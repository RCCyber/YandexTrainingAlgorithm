"""
Find X point location in relation to triangle
If X in the triangle or on the triangle side => 0
Else find the top which is closer to X point
"""
leg = int(input())
median = leg // 2
point = list(map(int, input().split()))
if point[0] >= 0 and point[1] >= 0:
    if point[0] < leg or point[1] < leg:
        print(0)
    elif point[0] >= leg and point[1] >= leg:
        print(2)
elif point[0] <= median and point[1] < 0:
    print(1)
elif point[0] < 0 and point[1] <= median:
    print(1)
elif point[0] > leg and point[1] <= median:
    print(2)
elif point[0] > median and point[1] < 0:
    print(2)
elif point[0] < 0 and point[1] > median:
    print(3)
elif point[0] <= median and point[1] > leg:
    print(3)
