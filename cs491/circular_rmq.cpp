#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;
 
typedef long long ll;
 
const ll INF = 1LL << 60;
 
struct SegmentTree {
    int n;
    vector<ll> tree, lazy;
 
    SegmentTree(const vector<ll>& arr) {
        n = arr.size();
        tree.assign(4*n, 0);
        lazy.assign(4*n, 0);
        build(arr, 1, 0, n-1);
    }
 
    void build(const vector<ll>& arr, int idx, int l, int r) {
        if(l == r) {
            tree[idx] = arr[l];
            return;
        }
        int mid = (l + r) / 2;
        build(arr, idx*2, l, mid);
        build(arr, idx*2+1, mid+1, r);
        tree[idx] = min(tree[idx*2], tree[idx*2+1]);
    }
 
    void push(int idx, int l, int r) {
        if(lazy[idx] != 0) {
            tree[idx] += lazy[idx];
            if(l != r) {
                lazy[idx*2] += lazy[idx];
                lazy[idx*2+1] += lazy[idx];
            }
            lazy[idx] = 0;
        }
    }
 
    void update(int idx, int l, int r, int ql, int qr, ll val) {
        push(idx, l, r);
        if(ql > r || qr < l) return;
        if(ql <= l && r <= qr) {
            lazy[idx] += val;
            push(idx, l, r);
            return;
        }
        int mid = (l + r) / 2;
        update(idx*2, l, mid, ql, qr, val);
        update(idx*2+1, mid+1, r, ql, qr, val);
        tree[idx] = min(tree[idx*2], tree[idx*2+1]);
    }
 
    ll query(int idx, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) return INF;
        push(idx, l, r);
        if(ql <= l && r <= qr) return tree[idx];
        int mid = (l + r) / 2;
        return min(query(idx*2, l, mid, ql, qr),
                   query(idx*2+1, mid+1, r, ql, qr));
    }
 
    // Public update function
    void update(int l, int r, ll val) {
        update(1, 0, n-1, l, r, val);
    }
 
    // Public query function
    ll query(int l, int r) {
        return query(1, 0, n-1, l, r);
    }
};
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n;
    cin >> n;
    vector<ll> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    SegmentTree seg(arr);
    
    int m;
    cin >> m;
    cin.ignore(); // consume newline
    
    for (int i = 0; i < m; i++){
        string line;
        getline(cin, line);
        if(line.empty()){
            i--;
            continue;
        }
        istringstream iss(line);
        vector<ll> tokens;
        ll token;
        while(iss >> token)
            tokens.push_back(token);
 
        if(tokens.size() == 2){
            // rmq query
            int lf = tokens[0], rg = tokens[1];
            ll ans;
            if(lf <= rg) {
                ans = seg.query(lf, rg);
            } else {
                // wrap-around: take min in [lf, n-1] and [0, rg]
                ans = min(seg.query(lf, n-1), seg.query(0, rg));
            }
            cout << ans << "\n";
        } else if(tokens.size() == 3){
            // inc operation
            int lf = tokens[0], rg = tokens[1];
            ll v = tokens[2];
            if(lf <= rg) {
                seg.update(lf, rg, v);
            } else {
                seg.update(lf, n-1, v);
                seg.update(0, rg, v);
            }
        }
    }
    return 0;
}
