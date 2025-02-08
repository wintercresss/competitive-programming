#include <iostream>
#include<vector>
#include<set>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    set<pair<int,int>> bst;
    bst.insert({a[0], 0});
    vector<int> parentidx(n, -1);

    for (int i = 1; i < n; i++) {
        auto it = bst.lower_bound({a[i], 0});
        int cand1 = -1, cand2 = -1;
    
        if (it != bst.begin()){
            auto pred = prev(it);
            cand1 = pred->second;
        }

        if (it != bst.end()){
            cand2 = it->second;
        }

        int par;
        if (cand1 == -1) {
            par = cand2;
        } else if (cand2 == -1) {
            par = cand1;
        } else {
            par = (cand1 > cand2 ? cand1 : cand2);
        }

        parentidx[i] = par;
        bst.insert({a[i], i});
    }

    for (int i=1; i<n; i++) {
        cout << a[parentidx[i]] << " ";
    }
}