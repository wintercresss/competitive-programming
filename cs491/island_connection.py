from collections import deque

m, n = map(int, input().split())
grid = [[-1 for _ in range(n)] for _ in range(m)]

for i in range(m):
    curr = input()
    for j in range(n):
        grid[i][j] = curr[j]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    queue = deque([(i, j)])
    grid[i][j] = 'O'
    while queue:
        r, c = queue.popleft()
        for a, b in dirs:
            nextr, nextc = r+a, c+b
            if nextr < 0 or nextc < 0 or nextr >= m or nextc >= n or grid[nextr][nextc] == 'O':
                continue
            grid[nextr][nextc] = 'O'
            queue.append((nextr, nextc))
    return


num_islands = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'L':
            bfs(i, j)
            num_islands += 1

print(max(0, num_islands-1))