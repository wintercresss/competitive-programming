#include<vector>
#include<iostream>
using namespace std;

typedef long long ll;


int main() {
    ll n, q, l;
    cin >> n >> q >> l;
    vector<ll> vec;

    for (ll i = 0; i < n; i++) {
        ll strand;
        cin >> strand;
        vec.push_back(strand);
    }

    ll cnt = 0;
    if (vec[0] > l) {
        cnt++;
    }
    for (ll i = 1; i < vec.size(); i++) {
        if (vec[i] > l && vec[i-1] <= l) {
            cnt++;
        }
    }

    for (ll i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 0) {
            cout << cnt << endl;
        } else { // type = 1
            ll idx;
            ll amount;
            cin >> idx >> amount;
            idx--;
            vec[idx] += amount;
            if (vec.size() == 1 && vec[idx] > l && vec[idx] - amount <= l) cnt++;

            if (vec.size() > 1 && vec[idx] > l && vec[idx] - amount <= l && idx > 0 && idx < vec.size()-1) {
                if (vec[idx-1] > l && vec[idx+1] > l) {
                    cnt--;
                } else if (vec[idx-1] <= l && vec[idx+1] <= l) {
                    cnt++;
                }
            } else if (vec.size() > 1 && vec[idx] > l && vec[idx] - amount <= l && idx == 0) {
                if (vec[idx+1] <= l) {
                    cnt++;
                }
            } else if (vec.size() > 1 && vec[idx] > l && vec[idx] - amount <= l && idx == vec.size()-1) {
                if (vec[idx-1] <= l) {
                    cnt++;
                }
            }

            // for (int i = 0; i < vec.size(); i++) {
            //     std::cout << vec[i] << " ";
            // }
            // std::cout << std::endl;

        }
    }


}