first = list(map(int, input().split()))
second = list(map(int, input().split()))


def get_blocks(list1, list2):
    blocks = []
    length = list1[0] // 2
    a = [-1] * list1[0]
    for i in list2:
        a[i] = i
    if len(a) % 2 == 1 and a[length] != -1:
        return a[length]
    else:
        left_right = []
        for j in range(length-1, -1,  -1):
            if a[j] != -1:
                left_right.append(a[j])
                break
        for j in range(length, list1[0]):
            if a[j] != -1:
                left_right.append(a[j])
                break
        blocks.append(left_right)
    return blocks[0]


final = get_blocks(first, second)
if isinstance(final, int):
    print(final)
else:
    print(*final)
