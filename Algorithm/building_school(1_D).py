human_count = int(input())
house_coordinate = list(map(int, input().split()))
if len(house_coordinate) % 2 != 0:
    print(house_coordinate[len(house_coordinate) // 2])
else:
    print(house_coordinate[(len(house_coordinate) + 1) // 2])
