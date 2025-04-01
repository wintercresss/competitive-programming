n, t1, t2 = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)

def solve(idx):
    if idx >= len(arr):
        return 0

    best = float('-inf')

    for j in range(idx + t1, idx + t2 + 1):
        best = max(best, arr[idx] + solve(j))
    
    return best


ans = max(solve(i) for i in range(t2))
print(ans)