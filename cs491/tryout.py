from collections import defaultdict, deque, Counter

n, m = map(int, input().split())
d = defaultdict(list)
indegree = [0 for _ in range(n*3)]

for _ in range(m):
    order = list(map(int, input().split()))

    for i in range(1, len(order)-1):
        d[order[i]-1].append(order[i+1]-1)
        indegree[order[i+1]-1] += 1

queue = deque()
for idx, deg in enumerate(indegree):
    if deg == 0:
        queue.append(idx)

top_order = []
while queue:
    currnode = queue.popleft()
    top_order.append(currnode+1)
    for nextnode in d[currnode]:
        indegree[nextnode] -= 1
        if indegree[nextnode] == 0:
            queue.append(nextnode)

if len(top_order) != n*3:
    print("NO")
else:
    print("YES")
    for i in range(0, len(top_order), 3):
        print(top_order[i], top_order[i+1], top_order[i+2])