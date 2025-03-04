class SegmentTree:
    def __init__(self, arr):
        """Initialize the segment tree with the given array."""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Segment tree array
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """Recursively build the segment tree."""
        if start == end:
            self.tree[node] = arr[start]  # Leaf node stores the array value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)

            # Store the maximum value in the current segment
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def range_max(self, left, right):
        """Returns the maximum value in the range [left, right]."""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        """Helper function to query the max in range [left, right]."""
        if left > end or right < start:
            return float('-inf')  # Out of range, return negative infinity

        if left <= start and end <= right:
            return self.tree[node]  # Completely within range

        mid = (start + end) // 2
        left_max = self._query(2 * node + 1, start, mid, left, right)
        right_max = self._query(2 * node + 2, mid + 1, end, left, right)

        return max(left_max, right_max)

    def update(self, index, value):
        """Updates the array at index with new value."""
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        """Helper function to update the segment tree."""
        if start == end:
            self.tree[node] = value  # Update the leaf node
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)

            # Recalculate max after update
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])

n, m = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
l, r, s = map(int, input().split())

#print(l, r, "INTERVAL")

tree = SegmentTree(arr)

total = tree.range_max(l, r)

for _ in range(1, m):
    l = ((l + s) % n) + 1
    r = ((r + s) % n) + 1
    l, r = min(l, r), max(l, r)
    #print(l, r, "INTERVAL")
    total += tree.range_max(l, r)

print(total)