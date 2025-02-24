import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))

heap = [(0, 0)] # COST, NODE
visited = set()
visited.add((0, 0))

best = [-1 for _ in range(n)]

while heap:
    currcost, currnode = heapq.heappop(heap)
    if currnode in visited:
        continue

    best[currnode] = currcost
    visited.add(currnode)
    for nextnode, nextcost in graph[currnode]:
        heapq.heappush(heap, (currcost+nextcost, nextnode))

print(*best)