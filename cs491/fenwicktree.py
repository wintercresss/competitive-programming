import sys
input_data = sys.stdin.read().strip().split()

n, m = map(int, input_data[:2])
F = [0] * (n + 1)   # 1-based indexing


def fenwicks_update(x, val):
    while x <= n:
        F[x] += val
        x += x & -x

idx = 2
output = []

for _ in range(m):
    x, v = map(int, input_data[idx:idx+2])
    idx += 2

    fenwicks_update(x, v)
    output.append(str(F[x]))

print("\n".join(output))
