from functools import cache
n, m = map(int, input().split())
# n = nodes, m = edges

cost = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u, v, dist = map(int, input().split())
    u -= 1
    v -= 1
    cost[u][v] = dist
    cost[v][u] = dist


for i in range(n):
    cost[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# goal: visit all nodes
# mask represents nodes that are taken?
@cache
def dp(mask, last):
    if mask == (1 << n) - 1:
        return 0
    
    best = float('inf')
    for j in range(n):
        if mask & (1 << j):
            continue
        best = min(best, cost[last][j] + dp(mask | (1 << j), j))
    return best

ans = min(dp(1 << i, i) for i in range(n))
print(ans)