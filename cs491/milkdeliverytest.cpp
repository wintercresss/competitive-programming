#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;
 
typedef long long ll;
const ll INF = 1e18;
 
struct Edge {
    int to;
    int weight;
};
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, K, T;
    cin >> N >> M >> K >> T;
    
    // Mark subway stations.
    vector<bool> hasSubway(N + 1, false);
    for (int i = 0; i < K; i++){
        int city;
        cin >> city;
        hasSubway[city] = true;
    }
    
    // Use nodes 1..N for cities and node V (N+1) as the virtual node.
    int V = N + 1;
    vector<vector<Edge>> graph(N + 2); // nodes 1..N and V.
    
    // Read road edges.
    for (int i = 0; i < M; i++){
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }
    
    // Add subway edges via the virtual node.
    for (int i = 1; i <= N; i++){
        if (hasSubway[i]){
            // From subway city to virtual node (free)
            graph[i].push_back({V, 0});
            // From virtual node to subway city (cost T)
            graph[V].push_back({i, T});
        }
    }
    
    // Dijkstra from City 1.
    vector<ll> dist(N + 2, INF);
    dist[1] = 0;
    priority_queue<pair<ll, int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
    pq.push({0, 1});
    
    while(!pq.empty()){
        auto [d, u] = pq.top();
        pq.pop();
        if (d != dist[u]) continue;
        for (auto &edge : graph[u]){
            int v = edge.to;
            ll nd = d + edge.weight;
            if (nd < dist[v]){
                dist[v] = nd;
                pq.push({nd, v});
            }
        }
    }
    
    // If city N is unreachable, output -1.
    cout << (dist[N] == INF ? -1 : dist[N]) << "\n";
    
    return 0;
}
