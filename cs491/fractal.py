n = int(input())
a, b = map(int, input().split())

x = a
found = False

for i in range(n):
    temp = 3 * x
    ipart = temp // b
    rpart = temp % b

    if ipart == 1:
        if rpart != 0:
            print("NO")
            found = True
            break
        else:
            x = 0
            break
    else:
        x = rpart

if not found:
    print("YES")