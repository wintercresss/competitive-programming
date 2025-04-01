n, k = map(int, input().split())

print(n.bit_length())

dp = [False] * (n.bit_length() + 1)
dp[0] = True


shift_amt = 1
while n > 0:
    if n & 1:
        for i in range(len(dp)-1, -1, -1):
            if dp[i]:
                for j in range(i+1, min(i+shift_amt+1, len(dp))):
                    dp[j] = True
    n = n >> 1
    shift_amt += 1

print(dp)