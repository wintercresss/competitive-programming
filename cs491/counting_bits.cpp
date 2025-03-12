#include <iostream>
using namespace std;

const long long MOD = 1000000007;

long long f(long long n) {
    if (n == 0)
        return 0;
    int x = 63 - __builtin_clzll(n);
    long long power = 1LL << x;
    long long term1 = ( (long long)x * ((power >> 1) % MOD) ) % MOD;
    long long term2 = f(n - power);
    long long term3 = (n - power + 1) % MOD;
    return (term1 + term2 + term3) % MOD;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q;
    cin >> q;
    while(q--){
        long long l, r;
        cin >> l >> r;
        long long res = ( (f(r) - f(l-1)) % MOD + MOD ) % MOD;
        cout << res << "\n";
    }
    return 0;
}
