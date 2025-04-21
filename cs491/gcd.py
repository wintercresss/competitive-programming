import sys
input = sys.stdin.readline

q = int(input())
res = []
for _ in range(q):
    a, b = map(int, input().split())
    while b != 0:
        a, b = b, a % b
    res.append(str(a))

print('\n'.join(res))