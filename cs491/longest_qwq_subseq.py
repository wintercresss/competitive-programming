import bisect

n, k = map(int, input().split())
arr = list(map(int, input().split()))
pl = list(map(int, input().split()))
pr = list(map(int, input().split()))

w = sorted(set(arr))

Ql = []
Qr = []

first = dict()
last = dict()

for idx, i in enumerate(arr):
    last[i] = idx+1
    if i not in first:
        first[i] = idx+1

for i in range(len(pl)):
    Ql.append(first[w[pl[i] - 1]])
    Qr.append(last[w[pr[i] - 1]])

map = dict()
for idx, i in enumerate(Ql):
    map[i] = idx

arr1 = [i for i in range(len(Ql))]
arr2 = []
for i in Qr:
    if i in map:
        arr2.append(map[i])
    else:
        arr2.append(float('-inf'))

#print(arr1)
#print(arr2)

def LIS(nums):
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)
        
        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)

print(LIS(arr2))