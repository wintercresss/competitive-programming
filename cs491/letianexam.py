import heapq

n, k = map(int, input().split())
x, y = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

p1 = len(l1)-1
p2 = len(l2)-1
total = 0
count = 0

visited = set((p1, p2))
heap = [(-(l1[p1] + l2[p2]), p1, p2)]

while count < k:
    curr, idx1, idx2 = heapq.heappop(heap)
    count += 1
    total += abs(curr)
    if idx1 > 0 and (idx1-1, idx2) not in visited:
        visited.add((idx1-1, idx2))
        heapq.heappush(heap, (-(l1[idx1-1] + l2[idx2]), idx1-1, idx2))
    
    if idx2 > 0 and (idx1, idx2-1) not in visited:
        visited.add((idx1, idx2-1))
        heapq.heappush(heap, (-(l1[idx1] + l2[idx2-1]), idx1, idx2-1))

print(total)