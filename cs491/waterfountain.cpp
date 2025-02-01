#include <bits/stdc++.h>
using namespace std;

vector<long long> solve(vector<long long>& arr) {
    vector<long long> res(arr.size());
    vector<pair<long long, long long>> stack;
    for (int i = 0; i < arr.size(); i++) {
        while (stack.size() > 0 && arr[i] > stack[stack.size()-1].second) {
            pair<long long, long long> last = stack.back();
            stack.pop_back();
            res[last.first] = i + 1;
        }

        stack.push_back({i, arr[i]});
    }
    for (int i=0; i<res.size(); i++) {
        if (res[i] == 0) res[i] = -1;
    }
    return res;
}


int main() {
    long long n;
    cin >> n;
    vector<long long> v;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        v.push_back(a);
    }
    vector<long long> result = solve(v);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << ' ';
    }
}