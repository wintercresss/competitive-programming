from collections import defaultdict, deque
import sys
input = sys.stdin.readline

grid = []

n, m = map(int, input().split())

for _ in range(n):
    grid.append(list(map(int, input().split())))


# create directed edge a->b if grid[a] < grid[b]
# topsort
# find longest path by checking reverse topological order

graph = defaultdict(list)
indegree = [0] * (n * m)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        curr = grid[i][j]
        for a, b in directions:
            nextr, nextc = i+a, j+b
            if nextr < 0 or nextc < 0 or nextr >= n or nextc >= m:
                continue
            if grid[nextr][nextc] > grid[i][j]:
                graph[i * m + j].append(nextr * m + nextc)
                indegree[nextr * m + nextc] += 1

# topsort
top_order = []
queue = deque()
for node in range(len(indegree)):
    if indegree[node] == 0:
        queue.append(node)

while queue:
    currnode = queue.popleft()
    top_order.append(currnode)
    for nextnode in graph[currnode]:
        indegree[nextnode] -= 1
        if indegree[nextnode] == 0:
            queue.append(nextnode)

# check in reverse topological order
streak = [1] * (n * m)

for node in top_order[::-1]:
    for nextnode in graph[node]:
        streak[node] = max(streak[node], 1 + streak[nextnode])

print(max(streak))