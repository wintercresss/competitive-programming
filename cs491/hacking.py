
n, t = map(int, input().split())
nums = list(map(int, input().split()))
vals = list(map(int, input().split()))

# goal, maximize v without exceeding t?

dp = [0 for _ in range(t+1)]

for i in range(n):
    for j in range(t, nums[i]-1, -1):
        dp[j] = max(dp[j], vals[i] + dp[j - nums[i]])

print(dp[t])





# def solve(idx, remain):
#     if idx >= n or remain <= 0:
#         return 0
    
#     if dp[idx][remain] != -1:
#         return dp[idx][remain]
    
#     skip = solve(idx+1, remain)
#     take = float('-inf')
#     if remain - nums[idx] >= 0:
#         take = vals[idx] + solve(idx+1, remain - nums[idx])
    
#     dp[idx][remain] = max(take, skip)
#     return max(take, skip)

#print(solve(0, t))