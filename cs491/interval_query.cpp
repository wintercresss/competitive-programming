#include <bits/stdc++.h>
using namespace std;



int main() {
    long long n, m;
    cin >> n >> m;
    vector<long long> v(n+1);

    for (long long i = 1; i <= n; i++){
        cin >> v[i];
    }

    vector<pair<long long, long long>> intervals(m);
    for (long long i = 0; i < m; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    deque<long long> D;
    long long currL = 1, currR = 0;

    for (long long i = 0; i < m; i++) {
        long long L = intervals[i].first;
        long long R = intervals[i].second;
        while (currR < R) {
            currR++;
            while (!D.empty() && v[D.back()] <= v[currR]) {
                D.pop_back();
            }
            D.push_back(currR);
        }

        while (currL < L) {
            while (!D.empty() && D.front() == currL) {
                D.pop_front();
            }
            currL++;
        }
        cout << v[D.front()] << "\n";
    }
}