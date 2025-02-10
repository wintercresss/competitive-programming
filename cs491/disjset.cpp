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
    int nodes, n;
    cin >> nodes >> n;

    vector<int> parent(nodes+1);
    vector<int> rank(nodes+1, 1);

    for (int i = 1; i < nodes+1; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < n; i++) {
        string type;
        cin >> type;
        if (type == "Union") {
            int u, v;
            cin >> u >> v;
            unio(u, v, parent, rank);
        } else {
            int nodetofind;
            cin >> nodetofind;
            cout << rank[find(nodetofind, parent, rank)] << endl;
        }
    }

}