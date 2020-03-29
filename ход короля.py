a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a - c == 1:
    if b - d == 1:
        print('YES')
    elif b - d == 0:
        print('YES')
    elif b - d == -1:
        print('YES')
    else:
        print('NO')
elif a - c == 0:
    if b - d == 1:
        print('YES')
    elif b - d == 0:
        print('YES')
    elif b - d == -1:
        print('YES')
    else:
        print('NO')
elif a - c == -1:
    if b - d == 1:
        print('YES')
    elif b - d == 0:
        print('YES')
    elif b - d == -1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
