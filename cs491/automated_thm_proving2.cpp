#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> graph;
vector<int> disc, low, scc;
vector<bool> inStack;
stack<int> st;
int timeCounter = 0, sccCount = 0;

void tarjan(int v) {
    disc[v] = low[v] = timeCounter++;
    st.push(v);
    inStack[v] = true;
    
    for (int w : graph[v]) {
        if (disc[w] == -1) {
            tarjan(w);
            low[v] = min(low[v], low[w]);
        } else if (inStack[w]) {
            low[v] = min(low[v], disc[w]);
        }
    }
    
    if (low[v] == disc[v]) {
        while (true) {
            int w = st.top();
            st.pop();
            inStack[w] = false;
            scc[w] = sccCount;
            if (w == v)
                break;
        }
        sccCount++;
    }
}

int literalIndex(int var, const string &val) {
    return 2 * (var - 1) + (val == "true" ? 0 : 1);
}

int complement(int lit) {
    return lit ^ 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    graph.assign(2 * n, vector<int>());
    disc.assign(2 * n, -1);
    low.assign(2 * n, 0);
    scc.assign(2 * n, 0);
    inStack.assign(2 * n, false);
    
    for (int i = 0; i < m; i++) {
        string x1, eq1, v1, arrow, x2, eq2, v2;
        cin >> x1 >> eq1 >> v1 >> arrow >> x2 >> eq2 >> v2;
        
        int p = stoi(x1.substr(1));
        int q = stoi(x2.substr(1));
        
        int u = literalIndex(p, v1);
        int v = literalIndex(q, v2);
        graph[u].push_back(v);
        graph[complement(v)].push_back(complement(u));
    }

    for (int i = 0; i < 2 * n; i++) {
        if (disc[i] == -1) {
            tarjan(i);
        }
    }
    
    bool satisfiable = true;
    for (int i = 0; i < n; i++) {
        if (scc[2 * i] == scc[2 * i + 1]) {
            satisfiable = false;
            break;
        }
    }
    
    cout << (satisfiable ? "YES" : "NO") << "\n";
    
    return 0;
}