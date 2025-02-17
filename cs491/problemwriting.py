import math

def find(x, square, one, const, root, log):
    if x == 0 and log == 0:
        logx = 0
    elif x == 0:
        logx = float('-inf')
    else:
        logx = log * math.log(x)

    ans = square * x*x + one * x + const + root * math.sqrt(x) + logx
    return ans

n = int(input())

square, one, const, root, log = 0, 0, 0, 0, 0

for i in range(n):
    info = input().split()
    functype, nums = info[0], list(map(int, info[1:]))
    if functype == "1":
        one += nums[0]
        const += nums[1]
    elif functype == "2":
        square += nums[0]
        one += nums[1]
        const += nums[2]
    elif functype == "sqrt":
        root += math.sqrt(nums[0])
        const += nums[1]
    elif functype == "log":
        log += nums[0]
        const += nums[1]


best = float('-inf')
for i in range(0, 43201):
    best = max(best, find(i, square, one, const, root, log))

print(best)

# point = ternary_search(10**-7, square, one, const, root, log)
# left = find(math.floor(point), square, one, const, root, log)
# right = find(math.ceil(point), square, one, const, root, log)
# print(max(left, right))
