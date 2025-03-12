#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<ll> a(n+1);
    for (int i = 1; i <= n; i++){
        cin >> a[i];
    }
    
    int blockSize = sqrt(n); 

    int numBlocks = (n / blockSize) + 1;
    
    vector<ll> blockSum(numBlocks, 0);

    for (int i = 1; i < blockSize && i <= n; i++){
        blockSum[0] += a[i];
    }

    for (int b = 1; b < numBlocks; b++){
        int start = b * blockSize;
        int end = min(n, (b+1) * blockSize - 1);
        for (int i = start; i <= end; i++){
            blockSum[b] += a[i];
        }
    }

    while(m--){
        int l, r;
        cin >> l >> r;
        int lParity = l & 1;
        
        ll ans = 0;
        int leftBlock = l / blockSize;
        int rightBlock = r / blockSize;
        
        int leftBlockEnd = (leftBlock == 0 ? blockSize - 1 : min(n, (leftBlock+1) * blockSize - 1));
        int endIndex = min(r, leftBlockEnd);
        int sign = ((leftBlock & 1) == lParity) ? 1 : -1;
        for (int i = l; i <= endIndex; i++){
            ans += sign * a[i];
        }

        for (int b = leftBlock + 1; b < rightBlock; b++){
            int blockSign = ((b & 1) == lParity) ? 1 : -1;
            ans += blockSign * blockSum[b];
        }
        
        if(rightBlock != leftBlock){
            int rightBlockStart = rightBlock * blockSize;
            sign = ((rightBlock & 1) == lParity) ? 1 : -1;
            for (int i = rightBlockStart; i <= r; i++){
                ans += sign * a[i];
            }
        }
        
        cout << ans << "\n";
    }
    return 0;
}
