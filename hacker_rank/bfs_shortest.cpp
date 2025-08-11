
// Create adjacent list from edge pairs
std::vector<std::set<int>> edges_to_adj(int n, vector<vector<int>> edges)
{
    std::vector<std::set<int>> adj(n+1);
    for (auto e : edges) {
        adj[e[0]].insert(e[1]);
        adj[e[1]].insert(e[0]); // Graph is undirected
    }
    return adj;
}

vector<int> bfs_dist(int n, const std::vector<std::set<int>>& adj, int start_node)
{
    std::vector<int> distances(n + 1, -1);
    std::queue<int> q;

    distances[start_node] = 0;
    q.push(start_node);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (distances[v] == -1) { // If neighbor 'v' is unvisited
                distances[v] = distances[u] + 6; // Assuming edge weight of 6
                q.push(v);
            }
        }
    }

    vector<int> out;
    for (int i=1;i<=n;i++) {
        if (i != start_node) out.push_back(distances[i]);
    }

    return out;
}

vector<int> bfs(int n, int m, vector<vector<int>> edges, int s)
{
    auto adj = edges_to_adj(n, edges);

    auto out = bfs_dist(n, adj, s);

    return out;
}
