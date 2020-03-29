import math
A = int(input())
B = int(input())
C = int(input())
if A + B <= C or A + C <= B or B + C <= A or A + B + C <= 0:
    print('impossible')
else:
    if B < C:
        N = B
        B = C
        C = N
    if A < B:
        N = A
        A = B
        B = N
    if B < C:
        N = B
        B = C
        C = N
    if A < B:
        N = A
        A = B
        B = N
    if A ** 2 == B ** 2 + C ** 2:
        print('rectangular')
    else:
        alpha = math.acos((B * B + C * C - A * A) / (2 * B * C))
        if alpha < math.pi / 2:
            print('acute')
        else:
            print('obtuse')
