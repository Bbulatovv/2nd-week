a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 <= a2 and b1 <= b2:
    if a1 % 2 == 1 and b1 % 2 == 1:
        if (a2 % 2 == 1 and b2 % 2 == 1) or (a2 % 2 == 0 and b2 % 2 == 0):
            print("Yes")
        else:
            print('No')
    elif a1 % 2 == 0 and b1 % 2 == 0:
        if (a2 % 2 == 1 and b2 % 2 == 1) or (a2 % 2 == 0 and b2 % 2 == 0):
            print("Yes")
        else:
            print('No')
else:
    print('No')
