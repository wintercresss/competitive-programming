from collections import defaultdict
import heapq

m = int(input())
inp = input().split()
src, tgt, k = inp[0], inp[1], int(inp[2]) # k = max flight tickets

d = defaultdict(list)

for _ in range(m):
    typ, company, start, end = map(str, input().split())
    d[start].append((end, typ, company))
    d[end].append((start, typ, company))

# if same company, can keep going with same ticket (FLIGHT)
# if prev = ferry, cannot go to ferry
# can only buy k flight tickets

heap = [(0, src, None, None, 0)]

best = float('inf')

dp = defaultdict(lambda: float('inf'))

while heap:
    total, currnode, currtype, curr_company, curr_k = heapq.heappop(heap)

    if total >= dp[(curr_k, currnode, currtype, curr_company)]:
        continue
    dp[(curr_k, currnode, currtype, curr_company)] = total

    if currnode == tgt:
        best = min(best, total)
        continue

    for nextnode, nexttype, next_company in d[currnode]:
        if currtype == "F" and nexttype == "F":
            continue
        if curr_company == next_company:
            if nexttype == "P" and curr_k < k:
                heapq.heappush(heap, (total, nextnode, nexttype, next_company, curr_k+1))
            elif nexttype != "P":
                heapq.heappush(heap, (total, nextnode, nexttype, next_company, curr_k))
        elif nexttype != "P":
            heapq.heappush(heap, (total+1, nextnode, nexttype, next_company, curr_k))
        else: # nexttype = P
            if curr_k < k:
                heapq.heappush(heap, (total+1, nextnode, nexttype, next_company, curr_k+1))

print(best)