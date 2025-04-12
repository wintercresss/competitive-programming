n, t1, t2 = map(int, input().split())
arr = list(map(int, input().split()))

dp = [-1] * (len(arr) + 1)

def solve(idx):
    print(dp)
    if idx >= len(arr):
        return 0
    
    if dp[idx] != -1:
        return dp[idx]

    best = float('-inf')

    for j in range(idx + t1, idx + t2 + 1):
        best = max(best, arr[idx] + solve(j))
    
    dp[idx] = best
    return best


ans = solve(-1)

print(dp)
print(ans)