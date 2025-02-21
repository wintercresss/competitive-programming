#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

vector<vector<int>> graph;
vector<int> ids, low, scc_ids;
vector<bool> onStack;
stack<int> st;
int index_counter, scc_count;

void dfs(int curr) {
    st.push(curr);
    onStack[curr] = true;
    ids[curr] = low[curr] = index_counter++;
    
    // Explore neighbors
    for (int next : graph[curr]) {
        if (ids[next] == -1) {
            dfs(next);
            low[curr] = min(low[curr], low[next]);
        } else if (onStack[next]) {
            low[curr] = min(low[curr], ids[next]);
        }
    }
    
    // Found a strongly connected component (SCC)
    if (ids[curr] == low[curr]) {
        while (true) {
            int node = st.top();
            st.pop();
            onStack[node] = false;
            scc_ids[node] = scc_count;
            // This assignment of low[node] is optional
            low[node] = ids[curr];
            if (node == curr) break;
        }
        scc_count++;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while(T--){
        int n, m;
        cin >> n >> m;
        
        // Initialize graph and related structures
        graph.assign(n, vector<int>());
        ids.assign(n, -1);
        low.assign(n, 0);
        scc_ids.assign(n, 0);
        onStack.assign(n, false);
        while(!st.empty()) st.pop();
        index_counter = 0;
        scc_count = 0;
        
        // Read graph edges (nodes are assumed to be 0-indexed)
        for (int i = 0; i < m; i++){
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
        }
        
        // Run Tarjan's DFS from each unvisited node
        for (int i = 0; i < n; i++){
            if (ids[i] == -1)
                dfs(i);
        }
        
        // Compute indegree for each SCC component
        vector<int> indegree(scc_count, 0);
        for (int u = 0; u < n; u++){
            for (int v : graph[u]){
                if (scc_ids[u] != scc_ids[v])
                    indegree[scc_ids[v]]++;
            }
        }
        
        // Count the number of SCCs with zero indegree
        int total = 0;
        for (int deg : indegree)
            if (deg == 0)
                total++;
        
        cout << total << "\n";
    }
    
    return 0;
}
