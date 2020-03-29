a = int(input())
x = 0
while a != 0:
    b = int(input())
    if b != 0 and a < b:
        x += 1
    a = b
print(x)
