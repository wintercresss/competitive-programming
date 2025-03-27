#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <cmath>
using namespace std;
 
typedef long long ll;
 
struct Edge {
    int u, v;
    ll w;
    bool used;
};
 
struct DSU {
    vector<int> parent, rank;
    DSU(int n) : parent(n+1), rank(n+1, 0) {
        for (int i = 0; i <= n; i++) parent[i] = i;
    }
    int find(int a) {
        return parent[a] == a ? a : parent[a] = find(parent[a]);
    }
    bool unite(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (rank[a] < rank[b]) swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
        return true;
    }
};
 
int LOG;
vector<int> depth;
vector<vector<int>> up;
vector<vector<ll>> maxEdge;
vector<vector<pair<int, ll>>> tree;

void dfs(int v, int p, ll w) {
    up[v][0] = p;
    maxEdge[v][0] = w;
    for (auto &edge : tree[v]) {
        int nv = edge.first;
        ll wght = edge.second;
        if (nv == p) continue;
        depth[nv] = depth[v] + 1;
        dfs(nv, v, wght);
    }
}

ll query(int u, int v) {
    if (depth[u] < depth[v])
        swap(u, v);
    ll res = 0;
    for (int i = LOG; i >= 0; i--) {
        if (depth[u] - (1 << i) >= depth[v]) {
            res = max(res, maxEdge[u][i]);
            u = up[u][i];
        }
    }
    if (u == v)
        return res;
    for (int i = LOG; i >= 0; i--) {
        if (up[u][i] != up[v][i]) {
            res = max(res, maxEdge[u][i]);
            res = max(res, maxEdge[v][i]);
            u = up[u][i];
            v = up[v][i];
        }
    }
    res = max(res, maxEdge[u][0]);
    res = max(res, maxEdge[v][0]);
    return res;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, m;
    cin >> n >> m;
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].used = false;
    }
 
    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.w < b.w;
    });
 
    DSU dsu(n);
    ll mstWeight = 0;
    tree.resize(n + 1);
    for (int i = 0; i < m; i++) {
        if (dsu.unite(edges[i].u, edges[i].v)) {
            edges[i].used = true;
            mstWeight += edges[i].w;
            tree[edges[i].u].push_back({edges[i].v, edges[i].w});
            tree[edges[i].v].push_back({edges[i].u, edges[i].w});
        }
    }
 
    depth.assign(n + 1, 0);
    LOG = ceil(log2(n));
    up.assign(n + 1, vector<int>(LOG + 1, 0));
    maxEdge.assign(n + 1, vector<ll>(LOG + 1, 0));
 
    dfs(1, 0, 0);
 
    for (int j = 1; j <= LOG; j++) {
        for (int i = 1; i <= n; i++) {
            up[i][j] = up[ up[i][j-1] ][j-1];
            maxEdge[i][j] = max(maxEdge[i][j-1], maxEdge[ up[i][j-1] ][j-1]);
        }
    }
 
    ll ans = numeric_limits<ll>::max();
    for (int i = 0; i < m; i++) {
        if (edges[i].used) continue;
        int u = edges[i].u, v = edges[i].v;
        ll w = edges[i].w;
        ll L = query(u, v);
        ll candidate = mstWeight - L + w;
        if (candidate >= mstWeight && candidate < ans)
            ans = candidate;
    }
 
    cout << ans << "\n";
    return 0;
}
