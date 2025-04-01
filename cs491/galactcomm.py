from collections import defaultdict

n = int(input())
dist = [[0 for _ in range(n)] for _ in range(n)]

d = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    costs = list(map(int, input().split()))
    for col in range(len(costs)):
        d[row][col] = costs[col]

k = int(input())
for _ in range(k):
    a, b, c = map(int, input().split())
    

for i in range(1, n):
    print(dist[0][i])