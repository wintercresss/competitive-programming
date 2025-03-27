n, k = map(int, input().split())

M = min(n, k)
total = 0
i = 1
while i <= M:
    d = k // i
    j = M if d == 0 else min(M, k // d)
    total += d * (j * (j + 1) - (i - 1) * i) // 2
    i = j + 1

print(k * n - total)