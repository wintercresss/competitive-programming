#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum;
    long long mx;
    long long lazy;
};

static const int MAXN = 500000;

vector<Node> segtree;

void build(int idx, int start, int end) {
    if (start == end) {
        segtree[idx].sum = 0;
        segtree[idx].mx  = 0;
        segtree[idx].lazy= 0;
        return;
    }
    int mid = (start + end) / 2;
    build(idx*2, start, mid);
    build(idx*2+1, mid+1, end);

    segtree[idx].sum = segtree[idx*2].sum + segtree[idx*2+1].sum;
    segtree[idx].mx  = max(segtree[idx*2].mx, segtree[idx*2+1].mx);
    segtree[idx].lazy= 0;
}

void push_down(int idx, int start, int end) {
    long long &val = segtree[idx].lazy;
    if (val != 0) {
        int mid = (start + end) / 2;

        // left child
        segtree[idx*2].sum += val * (mid - start + 1);
        segtree[idx*2].mx  += val;
        segtree[idx*2].lazy += val;

        // right child
        segtree[idx*2+1].sum += val * (end - mid);
        segtree[idx*2+1].mx  += val;
        segtree[idx*2+1].lazy += val;

        // clear lazy value in current node
        val = 0;
    }
}

void update(int idx, int start, int end, int l, int r, long long value) {
    if (r < start || end < l) {
        // No overlap
        return;
    }
    if (l <= start && end <= r) {
        // Fully covered segment
        segtree[idx].sum += value * (end - start + 1);
        segtree[idx].mx  += value;
        segtree[idx].lazy+= value;
        return;
    }
    // partial overlap
    push_down(idx, start, end); // make sure children see any pending updates
    int mid = (start + end) / 2;
    update(idx*2, start, mid, l, r, value);
    update(idx*2+1, mid+1, end, l, r, value);

    // push up
    segtree[idx].sum = segtree[idx*2].sum + segtree[idx*2+1].sum;
    segtree[idx].mx  = max(segtree[idx*2].mx, segtree[idx*2+1].mx);
}

long long querySum(int idx, int start, int end, int l, int r) {
    if (r < start || end < l) {
        return 0;
    }
    if (l <= start && end <= r) {
        return segtree[idx].sum;
    }
    push_down(idx, start, end);
    int mid = (start + end) / 2;
    long long leftSum  = querySum(idx*2, start, mid, l, r);
    long long rightSum = querySum(idx*2+1, mid+1, end, l, r);
    return leftSum + rightSum;
}

long long queryMax(int idx, int start, int end, int l, int r) {
    if (r < start || end < l) {
        return LLONG_MIN;
    }
    if (l <= start && end <= r) {
        return segtree[idx].mx;
    }
    push_down(idx, start, end);
    int mid = (start + end) / 2;
    long long leftMax  = queryMax(idx*2, start, mid, l, r);
    long long rightMax = queryMax(idx*2+1, mid+1, end, l, r);
    return max(leftMax, rightMax);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    segtree.resize(4*n);

    build(1, 1, n);

    while (q--) {
        string op;
        cin >> op;
        if (op == "Add") {
            int l, r;
            long long v;
            cin >> l >> r >> v;
            update(1, 1, n, l, r, v);
        } else if (op == "Max") {
            int l, r;
            cin >> l >> r;
            cout << queryMax(1, 1, n, l, r) << "\n";
        } else if (op == "Sum") {
            int l, r;
            cin >> l >> r;
            cout << querySum(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}
