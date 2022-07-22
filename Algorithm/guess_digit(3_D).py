"""
guess the digits from 1 to N
"""
n = int(input())
status = ''
while status != 'HELP':
    assumption = set(map(int, input().split()))
    status = input()
    if status == 'YES':
        pass
    elif status == 'NO':
        pass
    elif status == 'HELP':
        pass
