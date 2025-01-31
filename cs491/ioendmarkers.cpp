#include <bits/stdc++.h>
using namespace std;

int main() {
    while (1) {
        int Ta, Tb;
        cin >> Ta >> Tb;
        if (Ta == 0 && Tb == 0) {
            break;
        }
        
        int totala = 0;
        int totalb = 0;

        for (int i = 0; i < Ta; i++) {
            int curra;
            cin >> curra;
            totala += curra;
        }
        for (int i = 0; i < Tb; i++) {
            int currb;
            cin >> currb;
            totalb += currb;
        }
        cout << totala - totalb << endl;


    }
}