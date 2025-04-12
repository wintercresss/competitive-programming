from collections import defaultdict
import bisect

n = int(input())
nums = list(map(int, input().split()))

d = defaultdict(list)

for idx, i in enumerate(nums):
    d[i].append(idx)

dp = [1] * len(nums)
prev = [i for i in range(len(nums))]

for i in range(1, len(nums)):
    if nums[i]-1 in d:
        biggest_index = bisect.bisect_left(d[nums[i]-1], i)-1
        if biggest_index >= 0:
            dp[i] = 1 + dp[d[nums[i]-1][biggest_index]]
            prev[i] = d[nums[i]-1][biggest_index]

#print(dp)
#print(prev)

max_length = float('-inf')
start_idx = float('inf')

for i in range(len(dp)):
    if dp[i] > max_length:
        max_length = dp[i]
        start_idx = i

# print(max_length)
ans = []

curr = start_idx
while prev[curr] != curr:
    ans.append(curr+1)
    curr = prev[curr]

ans.append(prev[curr]+1)
ans = ans[::-1]

print(max_length)
print(" ".join(map(str, ans)))