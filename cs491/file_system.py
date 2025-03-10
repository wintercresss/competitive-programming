import math
n = int(input())

divisors = [[] for _ in range(n + 1)]
for d in range(1, n + 1):
    for multiple in range(d, n + 1, d):
        divisors[multiple].append(d)

total_cost = 0
for y in range(1, n):
    best_cost = n * y // math.gcd(n, y)
    for g in divisors[y]:
        if y + g <= n:
            cand = y * (y + g) // g
            if cand < best_cost:
                best_cost = cand
    total_cost += best_cost

print(total_cost)