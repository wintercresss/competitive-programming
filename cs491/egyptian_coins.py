
n, k = map(int, input().split())

num_bits = 0
curr_pow = 0
results = []

max_k = 0

while n > 0:
    if n & 1:
        num_bits += 1
        results.append(1 << curr_pow)
        max_k += (1 << curr_pow)
    
    curr_pow += 1
    n = n >> 1

if max_k < k or len(results) > k:
    print("NO")
else:
    print("YES")
    remain = 0
    while len(results) + remain < k:
        x = results.pop()
        if x == 1:
            remain += 1
        else:
            results.append(x//2)
            results.append(x//2)
    results += [1 for _ in range(remain)]
    print(' '.join(map(str, results)))
