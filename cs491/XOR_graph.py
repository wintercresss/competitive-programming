from collections import defaultdict, deque

n, m = map(int, input().split())

# red edge = xi xor xj = 1
# blue edge = xi xor xj = 0

# if there is red edge between a connected component, not solvable
# otherwise, solvable

red = defaultdict(list)
blue = defaultdict(list)

for _ in range(m):
    curr = list(input().split())
    u = int(curr[0][1:])
    v = int(curr[2][1:])
    color = int(curr[-1])
    if color == 1:
        red[u].append(v)
        red[v].append(u)
    else:
        blue[u].append(v)
        blue[v].append(u)


totalvisit = set()

def bfs(start):
    currvisit = set()
    currvisit.add(start)
    queue = deque([start])

    while queue:
        currnode = queue.popleft()
        for nextnode in blue[currnode]:
            if nextnode in currvisit:
                continue
            currvisit.add(nextnode)
            queue.append(nextnode)
    
    for node in currvisit:
        for neighbor in red[node]:
            if neighbor in currvisit:
                return False # FOUND
    
    totalvisit.update(currvisit)
    return True


possible = True

for startnode in range(1, n+1):
    if startnode in totalvisit:
        continue
    if not bfs(startnode):
        print("NO")
        possible = False
        break

if possible:
    print("YES")