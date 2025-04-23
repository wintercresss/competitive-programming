import math
 
n = int(input())
 
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    
    res = []
    for p in range(2, num+1):
        if prime[p]:
            res.append(p)
    return res
 
primes = SieveOfEratosthenes(n)
print(len(primes))
res = []
 
for prime in primes:
    currpow = 1
    curr = 0
    while n // prime ** currpow > 0:
        curr += n // prime ** currpow
        currpow += 1
    res.append(str(prime))
    res.append(str(curr))
 
print('\n'.join(f"{res[i]} {res[i+1]}" for i in range(0, len(res), 2)))