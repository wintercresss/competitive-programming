from collections import defaultdict
import heapq

graph = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

print(graph)

heap = [(0, 1)] # dist, node
visited = set()

while heap:
    currcost, currnode = heapq.heappop(heap)
    if currnode in visited:
        continue
    visited.add(currnode)
    print(visited, currcost)
    if len(visited) == n:
        break

    for nextnode, nextcost in graph[currnode]:
        heapq.heappush(heap, (currcost + nextcost, nextnode))