def find(u):
    if parent[u] == u:
        return u
    
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    
    if rank[u] < rank[v]:
        parent[u] = v
        rank[v] += rank[u]
    else:
        parent[v] = u
        rank[u] += rank[v]
    return True

n, m = map(int, input().split())
edges = []
parent = [i for i in range(n)]
rank = [1] * n

for _ in range(m):
    u, v, cost = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((cost, u, v))

edges.sort()
res = []
totalcost = 0

for cost, a, b in edges:
    if union(a, b):
        res.append((a+1, b+1))
        totalcost += cost
    if len(res) == n-1:
        break

print(totalcost)
for a, b in res:
    print(str(a) + " " + str(b))