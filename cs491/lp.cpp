#include<iostream>
#include<string>
#include<vector>

using namespace std;

bool bellman_ford(vector<vector<pair<int, int>>> graph) {
    int V = graph.size();

    vector<int> dist(graph.size(), INT_MAX);
    dist[0] = 0;

    for (int i = 0; i < V-1; i++) {
        for (int j = 0; j < graph.size(); j++) {
            for (int k = 0; k < graph[j].size(); k++) {
                // u = j, v == graph[j][k][1], weight = graph[j][k][0] 
                int u = j;
                pair<int, int> pr = graph[j][k];
                int weight = pr.first;
                int v = pr.second;
                if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                }
            }
        }
    }

    // check for cycle
    for (int j = 0; j < graph.size(); j++) {
        for (int k = 0; k < graph[j].size(); k++) {
            int u = j;
            pair<int, int> pr = graph[j][k];
            int weight = pr.first;
            int v = pr.second;
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                return true;
            }
        }

    }

    return false;
}



int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    vector<vector<pair<int, int>>> graph(n+1);

    for (int i = 0; i < m; i++) {
        string line;
        getline(cin, line);

        int u, v, weight;
        sscanf(line.c_str(), "x%d - x%d <= %d", &u, &v, &weight);
        graph[v].push_back({weight, u});
    }

    for (int i = 1; i < n+1; i++) {
        graph[0].push_back({0, i});
    }

    bool res = bellman_ford(graph);
    if (res) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
    }

}