
n, k = map(int, input().split())
if n == 0:
    print(k)
else:
    cost = list(map(int, input().split()))
    mult = list(map(int, input().split()))


    third = [cost + k / p for cost, p in zip(cost, mult)]
    #print(third, "THIRD")

    arr = list(zip(cost, mult, third))
    #print(arr)

    arr.sort(key = lambda x: x[2])

    # def solve(i):
    #     if i >= len(arr):
    #         return k

    #     take = float('inf')
    #     if i+1 < len(arr):
    #         take = arr[i][0] + solve(i+1) / arr[i][1]
    #     skip = solve(i + 1)
    #     return min(take, skip)

    # print(solve(0), "ANS")

    dp = [float('inf')] * (len(arr) + 1)
    dp[-1] = k

    for i in range(len(arr)-1, -1, -1):
        dp[i] = min(dp[i+1], arr[i][0] + dp[i+1] / arr[i][1])

    print(dp[0])