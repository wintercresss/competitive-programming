from functools import cache
n, m, k = map(int, input().split())
N = n*m

directions = [(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1)]

forbidden = []
for idx in range(N):
    i, j = divmod(idx, m)
    mask = 0
    for dx, dy in directions:
        x, y = i+dx, j+dy
        if 0 <= x < n and 0 <= y < m:
            mask |= 1 << (x*m + y)
    forbidden.append(mask)

@cache
def dp(mask, last):
    x = mask.bit_count()
    if x == k:
        return 1

    rem_cells = N - (last + 1)
    if x + rem_cells < k:
        return 0
    
    total = 0
    for idx in range(last+1, N):
        if mask & forbidden[idx]:
            continue
        total += dp(mask | (1 << idx), idx)

    return total

ans = dp(0, -1)
print(ans)