#include <bits/stdc++.h>
using namespace std;

long long kadane(vector<long long>& nums) {
    long long curr = nums[0];
    long long best = nums[0];
    for (long long i = 1; i < nums.size(); i++) {
        curr = max(nums[i], curr + nums[i]);
        best = max(best, curr);
    }
    return max(0LL, best);
}

int main() {
    long long n;
    cin >> n;
    vector<long long> v;
    for (long long i = 0; i < n; i++ ){
        long long curr_cost;
        cin >> curr_cost;
        v.push_back(curr_cost);
    }
    long long ans = kadane(v);
    cout << ans << endl;
}