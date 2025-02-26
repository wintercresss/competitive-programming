import heapq

n, m, k, t = map(int, input().split()) # n = num nodes, m = num edges, k = num subway, t = cost for subway
d = [[] for _ in range(n+2)]

subways = list(map(int, input().split()))

for _ in range(m):
    u, v, w = map(int, input().split())
    d[u].append((v, w))
    d[v].append((u, w))

for sub in subways:
    d[sub].append((n+1, 0))
    d[n+1].append((sub, t))

best = float('inf')

heap = [(0, 1)] # cost, node
visited = set()
found = False

while heap:
    currcost, currnode = heapq.heappop(heap)
    if currnode in visited:
        continue

    visited.add(currnode)
    if currnode == n:
        print(currcost)
        found = True
        break

    for nextnode, nextcost in d[currnode]:
        heapq.heappush(heap, (currcost+nextcost, nextnode))


if not found:
    print(-1)