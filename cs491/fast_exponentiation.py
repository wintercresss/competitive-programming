
t = int(input())
MOD = 10**9 + 7

def solve(x, n):
    res = 1

    while n > 0:
        if n % 2 == 1:
            res = res * x
            res = res % MOD
        x = x * x
        x = x % MOD
        n = n // 2
    
    return res

for _ in range(t):
    x, n = map(int, input().split())
    ans = solve(x, n)

    print(ans)