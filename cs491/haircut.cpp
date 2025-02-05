#include<vector>
#include<iostream>
using namespace std;

typedef long long ll;

//comapre with neighbors and join if they are all bigger than l
// one counter for how many disjoint sets greater than l
// in disjoint set, either all greater than l or none greater than l

ll find(vector<ll>& parent, ll u) {
    if (parent[u] == u) return u;
    parent[u] = find(parent, parent[u]);
    return parent[u];
}

bool union_(vector<ll>& parent, ll u, ll v) {
    ll paru = parent[u];
    ll parv = parent[v];
    if (paru == parv) return false;

    parent[u] = parent[v];
    return true;
}


int main() {
    int n, q, l;
    cin >> n >> q >> l;
    vector<ll> vec;

    for (int i = 0; i < n; i++) {
        ll strand;
        cin >> strand;
        vec.push_back(strand);
    }

    //vector<ll> parent;
    //for (int i = 0; i < vec.size(); i++) {
    //    parent[i] = i;
    //}

    ll cnt = 0;

    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 0) {
            cout << cnt << endl;
        } else { // type = 1
            ll idx;
            ll amount;
            cin >> idx >> amount;
            vec[idx] += amount;

            if (vec[idx] > l) {
                bool toinc = true;
                if (idx-1 >= 0 && vec[idx-1] > l) {
                    toinc = false;
                }
                if (idx+1 < vec.size() && vec[idx+1] > l) {
                    toinc = false;
                }
                if (toinc) cnt++;

            }

        }
    }


}