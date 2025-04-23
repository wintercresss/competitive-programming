l, r = map(int, input().split())
l -= 1

left = list(map(int, str(l)))
right = list(map(int, str(r)))

def solve(idx, is_tight, digits, has_4, has_9, has_5):
    if idx >= len(digits):
        return has_4 and has_9 and has_5
    
    if (idx, is_tight, has_4, has_9, has_5) in dp:
        return dp[(idx, is_tight, has_4, has_9, has_5)]
    
    limit = digits[idx] if is_tight else 9
    total = 0

    for i in range(limit + 1):
        next_tight = is_tight and i == digits[idx]
        if has_4 and has_9 and has_5:
            total += solve(idx+1, next_tight, digits, has_4, has_9, has_5)

        elif has_4 and has_9:
            if i == 5:
                total += solve(idx+1, next_tight, digits, has_4, has_9, True)
            elif i == 4:
                total += solve(idx+1, next_tight, digits, True, False, False)
            else:
                total += solve(idx+1, next_tight, digits, False, False, False)
        
        elif has_4:
            if i == 9:
                total += solve(idx+1, next_tight, digits, has_4, True, False)
            elif i == 4:
                total += solve(idx+1, next_tight, digits, True, False, False)
            else:
                total += solve(idx+1, next_tight, digits, False, False, False)
        
        else:
            if i == 4:
                total += solve(idx+1, next_tight, digits, True, False, False)
            else:
                total += solve(idx+1, next_tight, digits, False, False, False)

    dp[(idx, is_tight, has_4, has_9, has_5)] = total
    return total

dp = dict()
x = solve(0, True, right, False, False, False)
dp = dict()
y = solve(0, True, left, False, False, False)

print(x - y)