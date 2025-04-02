import sys
sys.setrecursionlimit(3000)

T = int(input())


def solve(s, d, idx, remaink):
    if idx >= len(s):
        return 0
    
    if dp[idx][remaink] != -1:
        return dp[idx][remaink]
    
    streak = 0
    best = 0
    swaps = 0
    for i in range(idx, len(s)):
        streak += 1
        if s[i] == '0':
            curr = solve(s, d, i+1, remaink)
            best = max(best, curr)
            swaps += 1
        
        if streak == d:
            if remaink - swaps >= 0:
                curr = 1 + solve(s, d, i+1, remaink - swaps)
                best = max(best, curr)
            break
    
    dp[idx][remaink] = best
    return best

answers = []

for _ in range(T):
    k, d, s = input().split()
    k, d = int(k), int(d)
    dp = [[-1 for _ in range(k+1)] for _ in range(len(s)+1)]

    ans = solve(s, d, 0, k)
    answers.append(ans)

for i in answers:
    print(i)




# def solve(s, d, idx, streak, remaink):
#     if idx >= len(s):
#         return 1 if streak == d else 0

#     curr = 1 if streak == d else 0
#     if streak == d:
#         streak = 0

#     take = 0

#     if s[idx] == '0' and remaink > 0:
#         take = solve(s, d, idx+1, streak+1, remaink-1)
    
#     if s[idx] == '0':
#         skip = solve(s, d, idx+1, 0, remaink)
#     else:
#         skip = solve(s, d, idx+1, streak+1, remaink)
    
#     return curr + max(take, skip)