#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, timer;
vector<vector<int>> adj;
vector<int> disc, low, parent;
vector<bool> visited, isArticulation;

void dfs(int u) {
    visited[u] = true;
    disc[u] = low[u] = ++timer;
    int children = 0;
    for (int v : adj[u]) {
        if (!visited[v]) {
            children++;
            parent[v] = u;
            dfs(v);
            low[u] = min(low[u], low[v]);
            if (parent[u] != -1 && low[v] >= disc[u])
                isArticulation[u] = true;
        } else if (v != parent[u]) {
            low[u] = min(low[u], disc[v]);
        }
    }
    if (parent[u] == -1 && children > 1)
        isArticulation[u] = true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    adj.resize(n + 1);
    disc.assign(n + 1, 0);
    low.assign(n + 1, 0);
    parent.assign(n + 1, -1);
    visited.assign(n + 1, false);
    isArticulation.assign(n + 1, false);

    for (int i = 0; i < m; i++){
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    timer = 0;
    for (int i = 1; i <= n; i++){
        if (!visited[i])
            dfs(i);
    }

    vector<int> result;
    for (int i = 1; i <= n; i++){
        if (isArticulation[i])
            result.push_back(i);
    }
    sort(result.begin(), result.end());

    cout << result.size() << "\n";
    for (int city : result)
        cout << city << " ";
    cout << "\n";

    return 0;
}