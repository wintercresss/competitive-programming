n = int(input())

grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 0:
            row[j] = float('inf')
    grid.append(row)

for i in range(n):
    grid[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

for i in range(n):
    for j in range(n):
        if i != j and grid[i][j] == float('inf'):
            grid[i][j] = -1

for i in range(n):
    print(" ".join(map(str, grid[i])))