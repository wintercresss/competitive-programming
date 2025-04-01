import heapq

n, c = map(int, input().split())
arr = list(map(int, input().split()))

heap = []
for i in arr:
    heapq.heappush(heap, i)

total = 0

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    total += a + b + c
    heapq.heappush(heap, a+b)

print(total)