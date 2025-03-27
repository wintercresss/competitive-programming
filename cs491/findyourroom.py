import sys, math

data = sys.stdin.buffer.read().split()
it = iter(data)
N = int(next(it))
Q = int(next(it))

a = [0] + [int(next(it)) for _ in range(N)]

threshold = int(math.sqrt(N)) + 1

pre = {}
for m in range(1, threshold):
    pre[m] = [0] * (m + 1)
    for p in range(1, m + 1):
        pre[m][p] = sum(a[p:N+1:m])

output_lines = []
for _ in range(Q):
    m = int(next(it))
    p = int(next(it))
    if m < threshold:
        output_lines.append(str(pre[m][p]))
    else:
        s = 0
        for i in range(p, N+1, m):
            s += a[i]
        output_lines.append(str(s))

sys.stdout.write("\n".join(output_lines))