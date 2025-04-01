from functools import cache

n = int(input())

arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
else:
    ops = input().split()

    #dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]

    @cache
    def solve(i, j):
        if i >= len(arr) or j >= len(arr):
            return 0
        if i > j:
            return 0
        if i == j:
            return arr[i]

        #if dp[i][j] != -1:
        #    return dp[i][j]
        
        res = float('-inf')
        for k in range(i, j):
            if ops[k] == '+':
                curr1 = solve(i, k) + solve(k+1, j)
                res = max(res, curr1)
            else:
                curr2 = solve(i, k) * solve(k+1, j)
                mincurr2 = dpmin(i, k) * dpmin(k+1, j)
                res = max(res, curr2, mincurr2)
        
        #dp[i][j] = res
        
        return res

    @cache
    def dpmin(i, j):
        if i >= len(arr) or j >= len(arr):
            return 0
        if i > j:
            return 0
        if i == j:
            return arr[i]

        #if dp[i][j] != -1:
        #    return dp[i][j]
        
        res = float('-inf')
        for k in range(i, j):
            if ops[k] == '+':
                curr1 = dpmin(i, k) + dpmin(k+1, j)
                res = min(res, curr1)
            else:
                curr2 = dpmin(i, k) * dpmin(k+1, j)
                res = min(res, curr2)
        
        #dp[i][j] = res
        
        return res
    

    ans = solve(0, len(arr)-1)
    print(ans)