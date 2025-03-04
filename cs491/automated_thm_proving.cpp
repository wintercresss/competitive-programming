#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

const int MAXN = 1000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<bitset<MAXN>> canProve(n);
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int x;
            cin >> x;
            if (x)
                canProve[i].set(j);
        }
    }
    
    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++){
            if (canProve[i].test(k)) {
                canProve[i] |= canProve[k];
            }
        }
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << (canProve[i].test(j) ? 1 : 0) << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
