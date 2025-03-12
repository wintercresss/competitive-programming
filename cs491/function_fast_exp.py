MOD = 998244353

def matrix_mult(A, B):
    res = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
    return res

def matrix_exponentiation(M, exp):
    result = [[1, 0, 0], 
              [0, 1, 0],
              [0, 0, 1]]  # Identity matrix
    base = M
    
    while exp:
        if exp % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2
    
    return result

def solve(n):
    if n == 0:
        return 4
    elif n == 1:
        return 9
    elif n == 2:
        return 5
    
    F = [
        [5, 9, 4],
        [1, 0, 0],
        [0, 1, 0]
    ]
    result = matrix_exponentiation(F, n - 2)
    
    f2, f1, f0 = 5, 9, 4
    f_n = (
        result[0][0] * f2 +
        result[0][1] * f1 +
        result[0][2] * f0
    ) % MOD

    return f_n

n = int(input())
ans = solve(n) % MOD
print(ans)