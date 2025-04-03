import sys
import math

data = sys.stdin.read().split()
n = int(data[0])
m = int(data[1])

a = list(map(int, data[2:2+n]))

queries = []
index = 2 + n
for i in range(m):
    l = int(data[index]) - 1
    r = int(data[index+1]) - 1
    index += 2
    queries.append((l, r, i))

block_size = int(math.sqrt(n))

queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))

answer = [0] * m
freq = [0] * (10**6 + 1)
current_l = 0
current_r = -1
distinct = 0

# mo's algorithm
for l, r, idx in queries:
    while current_r < r:
        current_r += 1
        freq[a[current_r]] += 1
        if freq[a[current_r]] == 1:
            distinct += 1
    
    while current_r > r:
        if freq[a[current_r]] == 1:
            distinct -= 1
        freq[a[current_r]] -= 1
        current_r -= 1

    while current_l < l:
        if freq[a[current_l]] == 1:
            distinct -= 1
        freq[a[current_l]] -= 1
        current_l += 1
    
    while current_l > l:
        current_l -= 1
        freq[a[current_l]] += 1
        if freq[a[current_l]] == 1:
            distinct += 1
    
    answer[idx] = distinct

sys.stdout.write("\n".join(map(str, answer)))

