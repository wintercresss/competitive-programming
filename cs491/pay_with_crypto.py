
def main():
    n, w_str = input().split()
    n = int(n)
    # "9.99" -> 9*100 + 99 = 999
    w = int(w_str.split('.')[0]) * 100 + int(w_str.split('.')[1])
    arr = []
    for s in input().split():
        dollars, cents = s.split('.')
        arr.append(int(dollars) * 100 + int(cents))

    MOD = 998244353

    dp = [0 for _ in range(w+1)]
    dp[w] = 1

    for i in range(len(arr)):
        for j in range(w - arr[i], -1, -1):
            dp[j] += dp[j + arr[i]]
            dp[j] %= MOD

    return dp[0]

print(main())

