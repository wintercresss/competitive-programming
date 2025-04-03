import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = map(int, data)
    n = next(it)
    m = next(it)
    a = [next(it) for _ in range(n)]
    
    # Compute next power of 2
    size = 1
    while size < n:
        size *= 2
    N = size * 2

    # Initialize four arrays for the segment tree.
    seg_sum = [0] * N
    seg_prefix = [0] * N
    seg_suffix = [0] * N
    seg_best = [0] * N

    # Build leaves: use 0-indexed values
    for i in range(n):
        x = a[i]
        seg_sum[size + i] = x
        seg_prefix[size + i] = x if x > 0 else 0
        seg_suffix[size + i] = x if x > 0 else 0
        seg_best[size + i] = x if x > 0 else 0

    # Leaves beyond n are left as neutral (0,0,0,0)
    # Build internal nodes in a bottom-up manner.
    for i in range(size - 1, 0, -1):
        left = i * 2
        right = left + 1
        s = seg_sum[left] + seg_sum[right]
        seg_sum[i] = s
        seg_prefix[i] = seg_prefix[left] if seg_prefix[left] > seg_sum[left] + seg_prefix[right] else seg_sum[left] + seg_prefix[right]
        seg_suffix[i] = seg_suffix[right] if seg_suffix[right] > seg_sum[right] + seg_suffix[left] else seg_sum[right] + seg_suffix[left]
        # Best is the maximum among left best, right best, or left suffix + right prefix.
        seg_best[i] = seg_best[left]
        if seg_best[right] > seg_best[i]:
            seg_best[i] = seg_best[right]
        tmp = seg_suffix[left] + seg_prefix[right]
        if tmp > seg_best[i]:
            seg_best[i] = tmp

    total_ans = 0
    # Process each query using iterative segment tree query
    for _ in range(m):
        # Convert from 1-indexed [l, r] to 0-indexed, half-open [l-1, r)
        l = next(it) - 1 + size
        r = next(it) + size
        
        # Accumulators for merging segments from left and right.
        L_sum = L_prefix = L_suffix = L_best = 0
        R_sum = R_prefix = R_suffix = R_best = 0
        
        while l < r:
            if l & 1:
                # Merge accumulator L with node l (i.e. combine(L, seg[l]))
                cur_sum = seg_sum[l]
                cur_prefix = seg_prefix[l]
                cur_suffix = seg_suffix[l]
                cur_best = seg_best[l]
                
                new_sum = L_sum + cur_sum
                new_prefix = L_prefix if L_prefix > L_sum + cur_prefix else L_sum + cur_prefix
                new_suffix = cur_suffix if cur_suffix > cur_sum + L_suffix else cur_sum + L_suffix
                new_best = L_best
                if cur_best > new_best:
                    new_best = cur_best
                tmp = L_suffix + cur_prefix
                if tmp > new_best:
                    new_best = tmp
                
                L_sum, L_prefix, L_suffix, L_best = new_sum, new_prefix, new_suffix, new_best
                l += 1
            if r & 1:
                r -= 1
                cur_sum = seg_sum[r]
                cur_prefix = seg_prefix[r]
                cur_suffix = seg_suffix[r]
                cur_best = seg_best[r]
                
                # Merge node r with accumulator R; order matters: combine(cur, R)
                new_sum = cur_sum + R_sum
                new_prefix = cur_prefix if cur_prefix > cur_sum + R_prefix else cur_sum + R_prefix
                new_suffix = R_suffix if R_suffix > R_sum + cur_suffix else R_sum + cur_suffix
                new_best = cur_best
                if R_best > new_best:
                    new_best = R_best
                tmp = cur_suffix + R_prefix
                if tmp > new_best:
                    new_best = tmp
                
                R_sum, R_prefix, R_suffix, R_best = new_sum, new_prefix, new_suffix, new_best
            l //= 2
            r //= 2
        
        # Merge final accumulators L and R to get answer for the query.
        new_sum = L_sum + R_sum
        new_prefix = L_prefix if L_prefix > L_sum + R_prefix else L_sum + R_prefix
        new_suffix = R_suffix if R_suffix > R_sum + L_suffix else R_sum + L_suffix
        new_best = L_best
        if R_best > new_best:
            new_best = R_best
        tmp = L_suffix + R_prefix
        if tmp > new_best:
            new_best = tmp
        
        total_ans += new_best

    sys.stdout.write(str(total_ans))

if __name__ == '__main__':
    main()
