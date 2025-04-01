
n = int(input())
nums = list(map(int, input().split()))

tail = [0] * n
prev = [-1] * n

length = 1

for i in range(1, n):
    if nums[i] > nums[tail[length-1]]:
        prev[i] = tail[length-1]
        tail[length] = i
        length += 1

    else:
        left, right = 0, length-1
        while left <= right:
            mid = (left + right) // 2
            if nums[i] <= nums[tail[mid]]:
                right = mid - 1
            else:
                left = mid + 1
        tail[left] = i
        if left != 0:
            prev[i] = tail[left-1]

lis = []
curr_idx = tail[length-1]
while curr_idx >= 0:
    lis.append(nums[curr_idx])
    curr_idx = prev[curr_idx]
lis.reverse()

print(len(lis))
print(" ".join(map(str, lis)))