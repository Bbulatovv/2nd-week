n = int(input())
i = 1
while i <= n:
    if i == n:
        print('YES')
    i = i * 2
    if i != n:
        print('NO')
