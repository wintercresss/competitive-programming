import sys
sys.setrecursionlimit(10**5)
d = set()
n, m = map(int, input().split())
for _ in range(m):
    d.add(input())

arr = input().split()
res = []

dp = [-1] * len(arr)

def solve(idx):
    if idx >= len(arr):
        return True
    
    if dp[idx] != -1:
        return dp[idx]

    curr = ""
    for i in range(idx, len(arr)):
        curr += arr[i]
        if curr in d:
            res.append(curr)
            if solve(i+1):
                dp[idx] = True
                return True
            res.pop()
    dp[idx] = False
    return False

ans = solve(0)
if ans == False:
    print(-1)
else:
    print(" ".join(res))