import sys
from collections import defaultdict, deque

data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
m = int(next(it))

grid = []
for _ in range(n):
    row = [int(next(it)) for _ in range(m)]
    grid.append(row)

graph = defaultdict(list)
indegree = [0] * (n * m)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        for a, b in directions:
            nextr, nextc = i + a, j + b
            if nextr < 0 or nextc < 0 or nextr >= n or nextc >= m:
                continue
            if grid[nextr][nextc] > grid[i][j]:
                graph[i * m + j].append(nextr * m + nextc)
                indegree[nextr * m + nextc] += 1

# topsort
top_order = []
queue = deque()
for node in range(n * m):
    if indegree[node] == 0:
        queue.append(node)

while queue:
    currnode = queue.popleft()
    top_order.append(currnode)
    for nextnode in graph[currnode]:
        indegree[nextnode] -= 1
        if indegree[nextnode] == 0:
            queue.append(nextnode)

streak = [1] * (n * m)
for node in reversed(top_order):
    for nextnode in graph[node]:
        streak[node] = max(streak[node], 1 + streak[nextnode])

sys.stdout.write(str(max(streak)))
