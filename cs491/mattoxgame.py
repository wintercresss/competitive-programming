m, n = map(int, input().split())

mdirections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
pdirections = [(1, 0), (2, 0), (-1, 0), (-2, 0), (0, 1), (0, 2), (0, -1), (0, -2)]

dp = dict()

def solve(mpos, ppos, turn):
    mi, mj, pi, pj = mpos[0], mpos[1], ppos[0], ppos[1]

    if mi == pi and mj == pj:
        return turn // 2
    
    if turn > 60:
        return float('inf')
    
    if (mi*n + mj, pi*n + pj, turn) in dp:
        return dp[(mi*n + mj, pi*n + pj, turn)]
    
    if turn % 2 == 1:
        best = float('-inf')
        for a, b in mdirections:
            nexti, nextj = mi+a, mj+b
            if nexti < 0 or nextj < 0 or nexti >= m or nextj >= n:
                continue
            if nexti == pi and nextj == pj:
                continue
            best = max(best, solve((nexti, nextj), ppos, turn+1))
        
        if best == float('-inf'):
            return turn // 2

        dp[(mi*n + mj, pi*n + pj, turn)] = best
        return best
    else:
        best = float('inf')
        for a, b in pdirections:
            nexti, nextj = pi+a, pj+b
            if nexti < 0 or nextj < 0 or nexti >= m or nextj >= n:
                continue
            if mi == nexti and mj == nextj:
                dp[(mi*n + mj, pi*n + pj, turn)] = turn // 2
                return turn // 2
            best = min(best, solve(mpos, (nexti, nextj), turn+1))
        dp[(mi*n + mj, pi*n + pj, turn)] = best
        return best

print(solve((0, 0), (m-1, n-1), 1))