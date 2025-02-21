from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def tarjan(d, n):
    ids = [-1] * n
    low = [0] * n
    onStack = [False for _ in range(n)]
    stack = []
    index = 0

    scc_count = 0
    scc_ids = [0] * n

    def dfs(currnode):
        nonlocal index, scc_count
        stack.append(currnode)
        onStack[currnode] = True
        ids[currnode] = index
        low[currnode] = index
        index += 1

        for nextnode in d[currnode]:
            if ids[nextnode] == -1:
                dfs(nextnode)
            if onStack[nextnode]:
                low[currnode] = min(low[currnode], low[nextnode])
        
        if (ids[currnode] == low[currnode]):
            while True:
                v = stack.pop()
                onStack[v] = False
                low[v] = ids[currnode]
                scc_ids[v] = scc_count
                if v == currnode:
                    break
            scc_count += 1

        return


    for i in range(n):
        if ids[i] == -1:
            dfs(i)
    
    indegree = [0] * scc_count
    
    for u in range(n):
        for v in d[u]:
            if scc_ids[u] != scc_ids[v]:
                indegree[scc_ids[v]] += 1
    
    total = 0
    for i in indegree:
        if i == 0:
            total += 1
    
    return total



T = int(input())

for z in range(T):
    n, m = map(int, input().split()) # n = nodes, m = edges
    d = defaultdict(list)
    for zz in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
    print(tarjan(d, n))

