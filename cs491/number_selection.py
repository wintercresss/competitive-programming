import sys
input = sys.stdin.readline

MOD = 998244353
T = int(input())
res = []

nums = []

for i in range(T):
    nums.append(tuple(map(int, input().split())))

maxn = max(n+k for n, k in nums)
fact = [0] * maxn
fact[0] = 1
for i in range(1, maxn):
    fact[i] = (fact[i-1] * i) % MOD

inv_fact = [0] * maxn
inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(maxn-1, 0, -1):
    inv_fact[i-1] = inv_fact[i]*i % MOD

for n, k in nums:
    # uniq_perm = math.perm(n, k) % MOD
    # uniq_comb = math.comb(n, k) % MOD
    # repeat_perm = pow(n, k, MOD)
    # repeat_comb = math.comb(n+k-1, k) % MOD

    uniq_perm = fact[n] * inv_fact[n-k] % MOD
    uniq_comb = fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
    repeat_perm = pow(n, k, MOD)
    repeat_comb = fact[n+k-1] * inv_fact[k] % MOD * inv_fact[n-1] % MOD

    res.append(f'{uniq_perm} {uniq_comb} {repeat_perm} {repeat_comb}')

print('\n'.join(res))