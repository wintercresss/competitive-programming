#include <iostream>
using namespace std;

int main() {
    int n;
    int best = -100000;
    int curr = 0;
    cin >> n;
    for (int i = 0; i < n; i++ ){
        int curr_cost;
        cin >> curr_cost;
        curr += curr_cost;
        if (curr < curr_cost) curr = curr_cost;
        best = max(best, curr);
    }
    cout << best << endl;
}