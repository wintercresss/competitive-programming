from collections import defaultdict


n, m = map(int, input().split())
d = defaultdict(list)
degree = defaultdict(int)

for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1

def find_bridges(graph):
    time = 0
    n = len(graph)
    disc = [-1] * n      # discovery times
    low = [-1] * n       # low values
    parent = [-1] * n    # parent vertices
    bridges = []         # list to store bridges

    def dfs(u):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:  # if v is not visited
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return bridges

print(find_bridges(d))