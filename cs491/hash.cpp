#include <iostream>
#include<vector>

using namespace std;
typedef long long ll;

long long find(ll u, vector<ll>& parent) {
    if (parent[u] == u) {
        return u;
    }

    parent[u] = find(parent[u], parent);
    return parent[u];
}

void unio(ll u, ll v, vector<ll>& parent) {
    ll x = find(u, parent);
    ll y = find(v, parent);
    parent[x] = parent[y];
}


inline ll hash_x(ll x, ll a, ll b, ll n) {
    return (a * x + b) % n;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, m, k;
    cin >> n >> m >> k;

    ll a, b;
    cin >> a >> b;

    vector<ll> cap(n, 0);
    vector<ll> parent(n);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < k; i++) {
        ll x;
        cin >> x;

        ll hashidx = hash_x(x, a, b, n);

        ll real_hash_idx = find(hashidx, parent);

        
        cap[real_hash_idx]++;
        if (cap[real_hash_idx] == m) {
            ll nextidx = (real_hash_idx + 1) % n;
            ll real_next_idx = find(nextidx, parent);
            unio(real_hash_idx, real_next_idx, parent);
        }

        cout << real_hash_idx << "\n";
    }
}