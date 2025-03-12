def matrix_mult(A, B):
    return [
            [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
           ]

def matrix_exponentiation(M, exp):
    result = [[1, 0], 
              [0, 1]]  # Identity matrix
    base = M
    
    while exp:
        if exp % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2
    
    return result

def fibonacci(n):
    if n == 0:
        return 0
    
    F = [[1, 1], [1, 0]]  # Transformation matrix
    result = matrix_exponentiation(F, n - 1)
    
    return result[0][0]  # F(n) is stored at position (0,0)


MOD = 1000000007
n = int(input())
ans = fibonacci(n) % MOD
print(ans)
