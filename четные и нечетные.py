a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    if b % 2 != 0:
        print('YES')
    elif c % 2 != 0:
        print('YES')
    else:
        print('NO')
elif b % 2 == 0:
    if a % 2 != 0:
        print('YES')
    elif c % 2 != 0:
        print('YES')
    else:
        print('NO')
elif c % 2 == 0:
    if a % 2 != 0:
        print('YES')
    elif b % 2 != 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
