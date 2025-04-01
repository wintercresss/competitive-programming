n = int(input())
arr = list(map(int, input().split()))

dp = [float('-inf')] * len(arr)
dp[0] = arr[0]

for i in range(1, len(dp)):
    dp[i] = arr[i] + max(dp[i-1], dp[i-2])

print(dp[-1])