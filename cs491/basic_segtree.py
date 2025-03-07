import sys

data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
q = int(next(it))

# Since the initial array is all zeros:
tree = [0] * (2 * n)
arr = [0] * n

def update(i, value):
    # Set value at position i and update the tree
    i += n
    tree[i] = value
    while i > 1:
        i //= 2
        tree[i] = max(tree[2 * i], tree[2 * i + 1])

def query(l, r):
    # Query maximum in interval [l, r]
    res = float('-inf')
    l += n
    r += n + 1  # make r inclusive
    while l < r:
        if l & 1:
            res = max(res, tree[l])
            l += 1
        if r & 1:
            r -= 1
            res = max(res, tree[r])
        l //= 2
        r //= 2
    return res

# No need to build the tree explicitly as arr is all zeros.

output = []
for _ in range(q):
    op = next(it)
    if op == "Add":
        x = int(next(it)) - 1
        v = int(next(it))
        arr[x] += v
        update(x, arr[x])
    elif op == "Set":
        x = int(next(it)) - 1
        v = int(next(it))
        arr[x] = v
        update(x, v)
    elif op == "Max":
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        output.append(str(query(l, r)))

sys.stdout.write("\n".join(output))
