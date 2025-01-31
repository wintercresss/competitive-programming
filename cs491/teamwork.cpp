#include <bits/stdc++.h>
using namespace std;

bool has_subset_sum(vector<int>& nums, int idx, int curr, bool has_taken) {
    if (idx >= nums.size()) {
        return curr == 0 && has_taken;
    }
    bool takepositive = has_subset_sum(nums, idx+1, curr + nums.at(idx), true);
    bool takenegative = has_subset_sum(nums, idx+1, curr - nums.at(idx), true);
    bool skip = has_subset_sum(nums, idx+1, curr, has_taken);
    return takepositive || takenegative || skip;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> vector;
        for (int i = 0; i < n; i++) {
            int curr_num;
            cin >> curr_num;
            vector.push_back(curr_num);
        }
        bool found = has_subset_sum(vector, 0, 0, false);
        if (found) {cout << "YES" << endl;};
        if (!found) {cout << "NO" << endl;}
    }
}