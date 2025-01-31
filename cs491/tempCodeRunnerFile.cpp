#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, a, b;
    int x = 0;
    int y = 0;
    cin >> t;
    while (t > 0) {
        --t;
        cin >> a >> b;
        x += a;
        y += b;
    }
    cout << x - y;
}