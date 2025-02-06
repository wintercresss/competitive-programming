#include <iostream>
#include <vector>
#include <set>
using namespace std;


bool check(vector<vector<int>>& visited, int i, int j, int n, int m) {
    vector<pair<int, int>> directions;
    directions.push_back(make_pair(0, 0));
    directions.push_back(make_pair(1, 0));
    directions.push_back(make_pair(-1, 0));
    directions.push_back(make_pair(0, 1));
    directions.push_back(make_pair(0, -1));
    directions.push_back(make_pair(1, 1));
    directions.push_back(make_pair(1, -1));
    directions.push_back(make_pair(-1, -1));
    directions.push_back(make_pair(-1, 1));

    bool can_place = true;

    for (int x = 0; x < directions.size(); x++) {
        int a = directions[x].first;
        int b = directions[x].second;
        int nexti = a + i;
        int nextj = b + j;

        if (nexti < 0 || nextj < 0 || nexti >= n || nextj >= m) {
            continue;
        }
        if (visited[nexti][nextj] == 1) {
            can_place = false;
            break;
        }
    }

    return can_place;
}


int solve(int n, int m, int k, int curr, vector<vector<int>>& visited, set<vector<vector<int>>>& old) {
    if (curr == k) {
        if (old.find(visited) != old.end()) {
            return 0;
        }
        old.insert(visited);
        return 1;
    }

    int result = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool can_place = check(visited, i, j, n, m);
            if (can_place) {
                visited[i][j] = 1;
                result += solve(n, m, k, curr+1, visited, old);
                visited[i][j] = 0;
            }
        }
    }
    return result;
}




int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> vec(n, vector<int>(m, 0));
    set<vector<vector<int>>> old;
    int res = solve(n, m, k, 0, vec, old);
    cout << res << endl;

}