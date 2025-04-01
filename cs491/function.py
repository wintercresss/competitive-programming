


k = int(input())
MOD = 998244353

# matrix:
# 5 9 4   f(n)
# 1 0 0   f(n-1)
# 0 1 0   f(n-2)

# multiply this matrix n-3 times

mat = [[5, 9, 4], 
       [1, 0 ,0], 
       [0, 1, 0]]

while k > 0:
    if k & 1:
        pass


    k = k >> 1