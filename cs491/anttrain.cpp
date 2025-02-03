#include<vector>
#include <iostream>
using namespace std;

// find num of segments with sum less than value
// continuous segments
// find prefix sum

// to find subarray from i to j, you take prefix[j] - prefix[i]
// [1, 2, 3, 4, ... j] - [1, 2, 3]

// number of inversions, mergesort?

int solve(vector<int>& nums, int s) {
    vector<int> prefix;
    int curr = 0;
    for (int i = 0; i < nums.size(); i++) {
        prefix.push_back(curr);
        curr += nums.at(i);
    }

    prefix.push_back(curr);

    int count = 0;

    for (int start = 0; start < prefix.size(); start++) {
        for (int end = start; end < prefix.size(); end++) {
            int curr = prefix.at(end) - prefix.at(start);
            if (curr < s) count++;
        }
    }
    return count;
}

int main() {
    int n, fav_num;
    cin >> n >> fav_num;
    vector<int> vector;
    for (int i = 0; i < n; i++ ) {
        int curr_num;
        cin >> curr_num;
        vector.push_back(curr_num);
    }

    int res = solve(vector, fav_num);
    cout << res << endl;

}