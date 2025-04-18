def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0 
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_count(s, t):
    if not t or not s:
        return 0

    pi = compute_prefix_function(t)
    count = 0
    j = 0

    for i in range(len(s)):
        while j > 0 and s[i] != t[j]:
            j = pi[j - 1]
        if s[i] == t[j]:
            j += 1
        if j == len(t):
            count += 1
            j = pi[j - 1]
    return count


s = input()
t = input()
result = kmp_count(s, t)
print(result)
