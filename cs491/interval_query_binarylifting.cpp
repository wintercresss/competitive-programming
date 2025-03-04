#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 100000;
static const int LOGN = 17; // enough for n up to 10^5

int st[LOGN+1][MAXN+1]; // sparse table
int lg[MAXN+1];         // precomputed logs

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    
    vector<long long> a(n+1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    // Precompute logs
    lg[1] = 0;
    for (int i = 2; i <= n; i++) {
        lg[i] = lg[i/2] + 1;
    }

    // Build Sparse Table for RMQ (range max)
    for (int i = 1; i <= n; i++) {
        st[0][i] = (int)a[i];
    }
    for (int k = 1; (1 << k) <= n; k++) {
        for (int i = 1; i + (1 << k) - 1 <= n; i++) {
            st[k][i] = max(st[k-1][i], st[k-1][i + (1 << (k-1))]);
        }
    }

    // RMQ function in O(1) using the Sparse Table
    auto getMax = [&](int L, int R) {
        int length = R - L + 1;
        int k = lg[length];
        int blockSize = (1 << k);
        return max(st[k][L], st[k][R - blockSize + 1]);
    };

    // Read the first query (1-based)
    int l, r, s;
    cin >> l >> r >> s;
    if (l > r) swap(l, r);

    long long sumAns = 0;
    int curL = l, curR = r;

    for (int i = 1; i <= m; i++) {
        // Maximum in [curL..curR]
        long long ans = getMax(curL, curR);
        sumAns += ans;

        // Generate next query using the "subtract 1" fix
        long long nextL = (curL + s) % n + 1;
        long long nextR = (curR + s) % n + 1;
        if (nextL > nextR) swap(nextL, nextR);

        curL = (int)nextL;
        curR = (int)nextR;
    }

    cout << sumAns << "\n";
    return 0;
}
