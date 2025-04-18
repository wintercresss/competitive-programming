import sys
input = sys.stdin.readline

n, m1, m2, m3 = map(int, input().split())

c1, v1, c2, v2, c3, v3, = [], [], [], [], [], []

for _ in range(m1):
    a, b = map(int, input().split())
    c1.append(a)
    v1.append(b)

for _ in range(m2):
    a, b = map(int, input().split())
    c2.append(a)
    v2.append(b)

for _ in range(m3):
    a, b = map(int, input().split())
    c3.append(a)
    v3.append(b)


def knapsack(W, val, wt): # val = v, wt = c
    dp = [0 for _ in range(W+1)]
    
    for i in range(len(val)):
        for j in range(W+1 - wt[i]):
            dp[j] = max(dp[j], val[i] + dp[j + wt[i]])

    return dp

first = knapsack(n, v1, c1)
second = knapsack(n, v2, c2)
third = knapsack(n, v3, c3)
best = 0

for i in range(1, n+1):
    for j in range(1, n - i):
        k = n - i - j
        test = first[n-i] * second[n-j] * third[n-k]
        best = max(best, test)

print(best)