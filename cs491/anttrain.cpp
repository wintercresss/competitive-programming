#include <bits/stdc++.h>
using namespace std;

// find num of segments with sum less than value
// continuous segments
// find prefix sum

// to find subarray from i to j, you take prefix[j] - prefix[i]
// [1, 2, 3, 4, ... j] - [1, 2, 3]

// number of inversions, mergesort?

long long merge(vector<int>& arr, int left, int mid, int right, int s) {
    int i = left;
    int j = mid + 1;
    vector<int> temp;
    long long inversions = 0;

    while (i <= mid && j <= right) {
        if (arr[j] - arr[i] < s) { // could be arr[i] - arr[j]
            temp.push_back(arr[i]);
            i++;
        } else {
            inversions += (mid - i + 1);
            temp.push_back(arr[j]);
            j++;
        }
    }

    while (i <= mid) {
        temp.push_back(arr[i]);
        i++;
    }
    
    // Copy any remaining elements of the right subarray
    while (j <= right) {
        temp.push_back(arr[j]);
        j++;
    }
    
    // Copy the merged elements back into the original array
    for (int k = left; k <= right; k++) {
        arr[k] = temp[k - left];
    }
    
    return inversions;
}

long long solve(vector<int>& nums, int left, int right, int s) {
    long long inversions = 0;

    if (left < right) {
        int mid = left + (right - left) / 2;
        inversions += solve(nums, left, mid, s);
        inversions += solve(nums, mid+1, right, s);
        inversions += merge(nums, left, mid, right, s);
    }


    return inversions;
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

    std::vector<int> prefix_sum;
    int curr = 0;
    for (int i = 0; i < vector.size(); i++) {
        curr += vector.at(i);
        prefix_sum.push_back(curr);
    }


    int res = solve(prefix_sum, 0, prefix_sum.size()-1, fav_num);
    cout << res << endl;
}