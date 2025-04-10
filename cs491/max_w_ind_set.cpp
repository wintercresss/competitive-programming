#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

struct NodeState {
    int u;
    int parent;
    int idx;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<vector<int>> graph(n);
    for (int i = 0; i < n - 1; i++){
        int u, v;
        cin >> u >> v;
        u--; v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    vector<ll> weight(n);
    for (int i = 0; i < n; i++){
        cin >> weight[i];
    }
    
    // dp0[u] = maximum weight if u is not selected.
    // dp1[u] = maximum weight if u is selected.
    vector<ll> dp0(n, 0), dp1(n, 0);
    
    vector<int> parent(n, -1);
    
    vector<NodeState> stack;
    stack.reserve(n);
    vector<int> order;
    order.reserve(n);
    
    stack.push_back({0, -1, 0});
    parent[0] = -1;
    
    while(!stack.empty()){
        NodeState &top = stack.back();
        int u = top.u, par = top.parent;
        if(top.idx < graph[u].size()){
            int v = graph[u][top.idx];
            top.idx++;
            if(v == par) continue;
            parent[v] = u;
            stack.push_back({v, u, 0});
        } else {
            order.push_back(u);
            stack.pop_back();
        }
    }
    
    for (int u : order) {
        dp1[u] = weight[u];
        for (int v : graph[u]) {
            if (v == parent[u]) continue;
            dp1[u] += dp0[v];
            dp0[u] += max(dp0[v], dp1[v]);
        }
    }
    
    ll answer = max(dp0[0], dp1[0]);
    cout << answer << "\n";
    return 0;
}
