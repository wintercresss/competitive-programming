#include <iostream>
#include <string>
#include <vector>

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

    vector<int> parent(nodes+1);
    vector<int> rank(nodes+1, 1);

    for (int i = 1; i < nodes+1; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < edges; i++) {
        int v1, v2;
        cin >> v1 >> v2;
        unio(v1, v2, parent, rank);
    }

    for (int i = 0; i < earthquakes; i++) {
        
    }

}