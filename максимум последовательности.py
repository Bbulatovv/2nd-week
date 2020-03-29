n = int(input())
maxN = n
while n != 0:
    n = int(input())
    if n == 0:
        break
    if n > maxN:
        maxN = n
print(maxN)
