#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int test;
    cin >> test;
    while (test--) {
        int arrlength;
        vector<int> v;
        cin >> arrlength;
        for (int i = 0; i < arrlength; i++) {
            int num;
            cin >> num;
            v.push_back(num);
        }
        sort(v.begin(), v.end());
        int result = 0;
        result = v[arrlength-2] + v[arrlength-1] - v[0] - v[1];
        cout << result << endl;
    }
}