prev = -1
curRepLen = 0
MaxRepLen = 0
x = int(input())
while x != 0:
    if prev == x:
        curRepLen += 1
    else:
        prev = x
        MaxRepLen = max(MaxRepLen, curRepLen)
        curRepLen = 1
    x = int(input())
MaxRepLen = max(MaxRepLen, curRepLen)
print(MaxRepLen)
