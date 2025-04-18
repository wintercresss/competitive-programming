def count_pairs(s):
    n = len(s)
    lcp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        si = s[i]
        row_i, row_ip1 = lcp[i], lcp[i+1]
        for j in range(n-1, -1, -1):
            if si == s[j]:
                row_i[j] = 1 + row_ip1[j+1]

    total = 0
    for i in range(n):
        row_i = lcp[i]
        for j in range(i+1, n):
            total += row_i[j]
    return total


s = input()
print(count_pairs(s))

