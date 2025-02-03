#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

ll mergeSort(vector<ll>& sums, int left, int right, ll s) {
    if (right - left <= 1) return 0;
    int mid = (left + right) / 2;
    ll count = 0;
    
    count += mergeSort(sums, left, mid, s);
    count += mergeSort(sums, mid, right, s);
    
    int j = mid;
    for (int i = left; i < mid; i++) {
        while (j < right && sums[j] < s + sums[i])
            j++;
        count += (j - mid);
    }
    
    vector<ll> temp(right - left);
    int i = left, k = mid, t = 0;
    while (i < mid && k < right) {
        if (sums[i] < sums[k])
            temp[t++] = sums[i++];
        else
            temp[t++] = sums[k++];
    }
    while (i < mid) temp[t++] = sums[i++];
    while (k < right) temp[t++] = sums[k++];
    
    for (int i = left; i < right; i++)
        sums[i] = temp[i - left];
    
    return count;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    ll s;
    cin >> n >> s;
    vector<ll> t(n);
    for (int i = 0; i < n; i++)
        cin >> t[i];
    
    vector<ll> prefix(n + 1, 0);
    for (int i = 0; i < n; i++){
        prefix[i + 1] = prefix[i] + t[i];
    }
    
    ll ans = mergeSort(prefix, 0, prefix.size(), s);
    cout << ans << "\n";
    
    return 0;
}
