#include <iostream>

using namespace std;

long long MOD = 998244353;

struct matrix {
    long long mat[3][3];
    matrix friend operator *(const matrix &a, const matrix &b){
        matrix c;
        for (int i = 0; i < 3; i++) {
          for (int j = 0; j < 3; j++) {
              c.mat[i][j] = 0;
              for (int k = 0; k < 3; k++) {
                  c.mat[i][j] += a.mat[i][k] * b.mat[k][j];
                  c.mat[i][j] = c.mat[i][j] % MOD;
              }
          }
        }
        return c;
    }
};

matrix matpow(matrix base, long long n) {
    matrix ans{ {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
      } };
    while (n) {
        if(n&1)
            ans = ans*base;
        base = base*base;
        n >>= 1;
    }
    return ans;
}

long long solve(int n) {
    matrix base{ {
      {5, 9, 4},
      {1, 0, 0},
      {0, 1, 0}
    } };
    return matpow(base, n).mat[0][0];
}


int main() {
    long long k;
    cin >> k;

    long long res = solve(k);
    cout << res << '\n';

}