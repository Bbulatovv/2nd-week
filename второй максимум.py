x = - 1
first = 0
second = 0
while x != 0:
    x = int(input())
    if x > first and x != 0:
        second = first
        first = x
    elif x > second and x != 0:
        second = x
print(second)
