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

ans = SieveOfEratosthenes(n)
print(len(ans))
print(' '.join(map(str, ans)))