import sys
input = sys.stdin.readline

def phi(n) :
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # p is a prime factor of n
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


T = int(input())
res = []
for i in range(T):
    n = int(input())
    res.append(phi(n))

print('\n'.join(map(str, res)))