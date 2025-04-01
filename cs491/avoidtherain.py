import heapq
from collections import defaultdict

n, m, k, t = map(int, input().split())

# k = num nodes we need to visit
# t = max total cost
# n = nodes
# m = edges

buildings = list(map(int, input().split()))
total_buildings = set(buildings)

d = defaultdict(list)

for _ in range(m):
    u, v, cost = map(int, input().split())
    d[u].append((v, cost))
    d[v].append((u, cost))

best = float('inf')

for start in buildings:
    visited = set()
    visit_buildings = 0
    heap = [(0, start)]
    while heap:
        currcost, currnode = heapq.heappop(heap)
        if currnode in visited:
            continue
        visited.add(currnode)
        if currnode in total_buildings:
            visit_buildings += 1
        if visit_buildings == len(total_buildings):
            best = min(best, currcost)
            break

        for nextnode, nextcost in d[currnode]:
            if nextnode in visited:
                continue
            heapq.heappush(heap, (currcost + nextcost, nextnode))

if best <= t:
    print("YES")
else:
    print("NO")