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


dp = dict()

def solvefirst(remain, i, cost, val, maxidx):
    print(remain, i, "REMAIN I")
    if remain < 0:
        return float('-inf')

    if i >= maxidx:
        return 0
    
    if (remain, i) in dp:
        return dp[remain][i]
    
    skip = solvefirst(remain, i+1, cost, val, maxidx)
    take = val[i] + solvefirst(remain - cost[i], i+1, cost, val, maxidx)
    dp[(remain, i)] = max(take, skip)
    return max(take, skip)

solvefirst(n, 0, c1, v1, m1)
print(dp)


# def solvesecond(remain, j):
#     if j >= m2:
#         return solvethird(remain, 0)

# def solvethird(remain, k):
#     if j >= m3:
#         return 1