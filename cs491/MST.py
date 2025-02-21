import heapq

n, m = map(int, input().split())
d = [[] for _ in range(n)]

def find_mst(d, startnode, n):
    heap = [(0, startnode, -1)] # -1 = prev
    visited = set()
    res = []
    total = 0

    while len(visited) < n:
        currcost, currnode, prevnode = heapq.heappop(heap)
        if currnode in visited:
            continue
        
        total += currcost
        visited.add(currnode)
        if prevnode != -1:
            res.append((prevnode+1, currnode+1))
        for nextnode, cost in d[currnode]:
            heapq.heappush(heap, (cost, nextnode, currnode))

    return res, total


for _ in range(m):
    u, v, cost = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, cost))
    d[v].append((u, cost))

answer, totalcost = find_mst(d, 0, n)

print(totalcost)
for u, v in answer:
    print(str(u) + " " + str(v))
