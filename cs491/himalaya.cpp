#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int count = 1;

void dfs(vector<vector<int>>& graph, int currnode, vector<bool>& visited, vector<int>& res, int K) {
    visited[currnode] = true;
    res[currnode] = count;
    for (int nextnode : graph[currnode]) {
        if (!visited[nextnode]) {
            count++;
            if (count > K) {
                count = count - K;
            }
            dfs(graph, nextnode, visited, res, K);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, K;
    cin >> N >> M >> K;
    
    vector<vector<int>> graph(N+1);
    vector<bool> visited(N+1, false);
    for (int i = 0; i < M; i++){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> res(N+1, -1);

    for (int i = 1; i < N+1; i++) {
        if (!visited[i]) {
            dfs(graph, i, visited, res, K);
        }
    }

    for (int i = 1; i < N+1; i++) {
        int curr = res[i];
        for (int j : graph[i]) {
            if (res[j] == res[i]) {
                cout << -1 << endl;;
                return 0;
            }
        }
    }

    for (int i = 1; i < N+1; i++) {
        cout << res[i] << endl;
    }
    
    return 0;
}
