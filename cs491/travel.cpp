#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
const int MAXN = 100005;
const int LOGN = 18;

int n, m;
vector<pair<int, ll>> adj[MAXN];
int parent[LOGN][MAXN];
int depth[MAXN];
ll distArr[MAXN];

void dfs(int v, int p) {
    parent[0][v] = p;
    for(auto &edge : adj[v]) {
        int u = edge.first;
        ll w = edge.second;
        if(u == p) continue;
        depth[u] = depth[v] + 1;
        distArr[u] = distArr[v] + w;
        dfs(u, v);
    }
}

int lca(int u, int v) {
    if(depth[u] < depth[v])
        swap(u, v);
    int d = depth[u] - depth[v];
    for(int i = 0; i < LOGN; i++){
        if(d & (1 << i))
            u = parent[i][u];
    }
    if(u == v)
        return u;
    for(int i = LOGN - 1; i >= 0; i--){
        if(parent[i][u] != parent[i][v]){
            u = parent[i][u];
            v = parent[i][v];
        }
    }
    return parent[0][u];
}

ll distanceBetween(int u, int v) {
    int ancestor = lca(u, v);
    return distArr[u] + distArr[v] - 2 * distArr[ancestor];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for(int i = 1; i < n; i++){
        int u, v;
        ll w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    
    depth[1] = 0;
    distArr[1] = 0;
    dfs(1, 0);
    
    for(int k = 1; k < LOGN; k++){
        for(int v = 1; v <= n; v++){
            int mid = parent[k-1][v];
            parent[k][v] = (mid == 0 ? 0 : parent[k-1][mid]);
        }
    }
    
    ll totalCost = 0;
    int current = 1;
    for(int i = 0; i < m; i++){
        int next;
        cin >> next;
        totalCost += distanceBetween(current, next);
        current = next;
    }

    totalCost += distanceBetween(current, 1);
    
    cout << totalCost << "\n";
    return 0;
}
