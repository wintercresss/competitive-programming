n, m = map(int, input().split()) # n = nodes, m = edges

edges = []
parent = [i for i in range(n)]
rank = [1 for i in range(n)]

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

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((w, u, v))

edges.sort(reverse=True)
remain = n

for weight, u, v in edges:
    if union(u, v):
        remain -= 1
    if remain == 1:
        print(weight)
        break