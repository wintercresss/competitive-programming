import math

MOD = 10**9 + 7
q = int(input())
 
def f(n):
    if n == 0:
        return 0
    x = math.floor(math.log2(n))
    return x * 2 **(x-1) + f(n - 2**x) + (n - 2**x + 1)
 
for _ in range(q):
    l, r = map(int, input().split())
 
    res = (f(r) - f(l-1)) % MOD
    print(int(res))