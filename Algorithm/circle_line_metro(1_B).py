"""
Find the shortest route from start station to finish station on circle subway line
Example:
    Input: 100 5 6  Output: 0
"""
a = list(map(int, input().split()))


def find_route(parameters):
    circle_line = [i for i in range(1, a[0]+1)]
    counter = 0
    left_right = []
    if parameters[1] > parameters[2]:
        parameters[1], parameters[2] = parameters[2], parameters[1]
    for i in range(parameters[1], parameters[2]):
        if circle_line[i] == parameters[2]:
            break
        counter += 1
    left_right.append(counter)
    counter = 0
    for i in range(parameters[1]-1, (parameters[2]-parameters[0]), -1):
        if circle_line[i] == parameters[2]:
            break
        counter += 1
    left_right.append(counter)
    return min(left_right)


print(find_route(a))
