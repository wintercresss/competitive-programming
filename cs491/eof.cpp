#include <bits/stdc++.h>
using namespace std;

int main() {
    int Ta, Tb;

    while (cin >> Ta >> Tb) {
        int asum = 0;
        int bsum = 0;

        for (int i = 0; i < Ta; i++) {
            int curra;
            cin >> curra;
            asum += curra;
        }

        for (int i = 0; i < Tb; i++) {
            int currb;
            cin >> currb;
            bsum += currb;
        }
        cout << asum - bsum << endl;
    }
}