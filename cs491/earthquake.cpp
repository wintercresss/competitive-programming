#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int find(int u, vector<int>& parent, vector<int>& rank) {
    if (parent[u] == u) return u;
    parent[u] = find(parent[u], parent, rank);
    return parent[u];
}

bool unio(int u, int v, vector<int>& parent, vector<int>& rank) {
    int paru = find(u, parent, rank);
    int parv = find(v, parent, rank);

    if (paru == parv) return false;
    else {
        parent[paru] = parent[parv];
        rank[parv] += rank[paru];
        return true;
    }
}



int main() {
    int nodes, edges, earthquakes;
    cin >> nodes >> edges >> earthquakes;
    int n_connected = nodes;

    vector<int> parent(nodes+1);
    vector<int> rank(nodes+1, 1);

    for (int i = 1; i < nodes+1; i++) {
        parent[i] = i;
    }

    vector<pair<int, int>> all_edges(edges);
    for (int i = 0; i < edges; i++) {
        int u;
        int v;
        cin >> u >> v;
        u--;
        v--;
        if (u > v) swap(u, v);
        all_edges[i] = {u, v};
    }


    unordered_map<long long, int> edgeIndex;
    edgeIndex.reserve(edges*2);

    for (int i = 0; i < edges; i++) {
        int u = all_edges[i].first;
        int v = all_edges[i].second;
        long long key = u * nodes + v;
        edgeIndex[key] = i;
    }

    vector<bool> removed(edges, false);
    vector<int> queryEdgeIndex(earthquakes);

    for (int i = 0; i < earthquakes; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        if (u > v) swap(u, v);
        long long key = u * nodes + v;
        int idx = edgeIndex[key];
        queryEdgeIndex[i] = idx;
        removed[idx] = true;
    }

    for (int i = 0; i < edges; i++) {
        if (!removed[i]) {
            bool did_merge = unio(all_edges[i].first, all_edges[i].second, parent, rank);
            if (did_merge) {
                n_connected--;
            }
        }
    }

    vector<pair<int, int>> res(earthquakes);
    for (int i = earthquakes-1; i>=0; i--) {
        int capital = find(0, parent, rank);
        int reachable = rank[capital];
        res[i] = {reachable, n_connected};
        int idx = queryEdgeIndex[i];
        bool did_merge = unio(all_edges[idx].first, all_edges[idx].second, parent, rank);
        if (did_merge) n_connected--;
    }

    for (int i = 0; i < earthquakes; i++) {
        cout << res[i].first << " " << res[i].second << "\n";
    }

}