n = int(input())
 
best = float('inf')
intervals = []
for i in range(n):
    d, t = map(int, input().split())
    
    # n assignments
    # d time to finish, due at t
    intervals.append([t-d, t])
 
intervals.sort(key = lambda x: x[1])
 
for i in range(len(intervals)-2, -1, -1):
    currstart, currend = intervals[i][0], intervals[i][1]
    nextstart, nextend = intervals[i+1][0], intervals[i+1][1]
 
    if currend > nextstart:
        delta = currend - nextstart
        intervals[i][0] = currstart - delta
        intervals[i][1] = currend - delta
 
if intervals[0][0] < 0:
    print(-1)
else:
    print(intervals[0][0])