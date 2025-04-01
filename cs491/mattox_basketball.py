n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[float('-inf'), float('-inf'), float('-inf')] for i in range(len(A) + 1)]

for i in range(3):
    dp[-1][i] = 0

for i in range(len(A)-1, -1, -1): # 0 = TAKE A, 1 = TAKE B, 2 = TAKE NONE
    dp[i][2] = max(dp[i+1][2], A[i] + dp[i+1][0], B[i] + dp[i+1][1])
    dp[i][1] = max(dp[i+1][2], A[i] + dp[i+1][0])
    dp[i][0] = max(dp[i+1][2], B[i] + dp[i+1][1])

print(max(dp[0]))




# def solve(idx, prev):
#     if idx >= len(A):
#         return 0
    
#     skip = solve(idx+1, None)
#     takeA = float('-inf')
#     takeB = float('-inf')

#     if prev == 0: # PREV TOOK A
#         takeB = B[idx] + solve(idx+1, 1)
#     if prev == 1: # PREV TOOK B
#         takeA = A[idx] + solve(idx+1, 0)
#     if prev == None:
#         takeA = A[idx] + solve(idx+1, 0)
#         takeB = B[idx] + solve(idx+1, 1)
    
#     return max(skip, takeA, takeB)

# ans = solve(0, None)