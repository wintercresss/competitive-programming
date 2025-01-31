#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    int x = 0;
    int y = 0;
    cin >> t;
    while (t > 0) {
        --t;
        int Ta, Tb;
        cin >> Ta >> Tb;
        int sumA = 0;
        int sumB = 0;
        for (int i = 0; i < Ta; i++) {
            int num;
            cin >> num;
            sumA += num;
        }

        for (int i=0; i<Tb; i++) {
            int num;
            cin >> num;
            sumB += num;
        }
        cout << sumA - sumB << endl;
    }
    
}