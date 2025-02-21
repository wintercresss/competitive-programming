n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

for r in range(n):
    col = list(map(int, input().split()))
    grid[r] = col.copy()

k = int(input())

for _ in range(k):
    u, v, cost = map(int, input().split())
    # edge u to v, with cost c
    u -= 1
    v -= 1

    total = 0
    for i in range(n):
        for j in range(i+1, n):
            grid[i][j] = min(grid[i][j], grid[i][u] + cost + grid[v][j], grid[i][v] + cost + grid[u][j])
            grid[j][i] = grid[i][j]
            total += grid[i][j]
    
    print(total)