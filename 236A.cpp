#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    string x;
    set<char> s;
    cin >> x;
    for (int i = 0; i < x.length(); i++) {
        s.insert(x[i]);
    }

    if (s.size() % 2  == 0) {
        cout << "CHAT WITH HER!";
    } else {
        cout << "IGNORE HIM!";
    }
}