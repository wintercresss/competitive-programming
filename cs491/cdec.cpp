#include<iostream>
using namespace std;

typedef long long ll;

int main() {
    ll l, r;
    cin >> l >> r;
    ll cnt = 0;
    for (ll i = l; i < r+1; i++) {
        ll temp = i;
        while (temp >= 495) {
            if (temp % 1000 == 495) {
                cnt++;
                break;
            }
            temp = temp / 10;
        }
    }
    cout << cnt << endl;
}