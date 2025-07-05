import math
import sys
input = sys.stdin.readline

T = int(input())

ans = []

for i in range(T):
    a, b = map(int, input().split())
    if math.gcd(a, b) > 1:
        ans.append(-1)
    else:
        ans.append(a * b - a - b)

print('\n'.join(map(str, ans)))