
void merge_people(int n, int q, std::vector<int> p, std::vector<int> q)
{
    // Communites in sets.
    std::vector<std::set<int>> comm;
    // People to community set map.
    std::map<int, int> p_to_s;
    for (int i=0;i<n;i++) {
        // id set = -1 means itself only.
        p_to_s[i+1] = -1;
    }

    for (int i=0;i<q;i++) {
        if (q[i]==0) {
            // print
            int id_set = p_to_s[p[i]-1];
            if (id_set>=0)
                cout << comm[id_set].size() << endl;
            else
                cout << 1 << endl;
        }
        else {
            // merge p and q
            int id = p_to_s[p[i]];
            int jd = p_to_s[q[i]];
            if (id>=0 && jd>=0) {
                std::set<int> temp;
                std::set_union(comm[id].begin(), comm[id].end(),
                    comm[jd].begin(), comm[jd].end(),
                    std::inserter(temp, temp.begin())
                    );
                comm[id] = temp;
                // empty
                comm[jd] = std::set<int>{};
                p_to_s[q[i]] = id;
            }
            else if (id>=0) {
                // add q to id
                comm[id].insert(q[i]);
                p_to_s[q[i]] = id;
            }
            else if (jd>=0) {
                // add p to jd
                comm[jd].insert(p[i]);
                p_to_s[p[i]] = jd;
            }
            else {
                // id=jd=-1 => create new set.
                std::set<int> one{p[i], q[i]};
                comm.push_back(one);
                int id = comm.size()-1;
                p_to_s[p[i]] = id;
                p_to_s[q[i]] = id;
            }
        }
    }
}

int find(int i, int parent[]) {
    if (parent[i] == i) {
        return i;
    }
    return parent[i] = find(parent[i], parent); // Path compression
}

void unite(int i, int j, int parent[], int size[]) {
    int root_i = find(i, parent);
    int root_j = find(j, parent);

    if (root_i != root_j) { // Merge only if they are in different communities
        if (size[root_i] < size[root_j]) {
            parent[root_i] = root_j;
            size[root_j] += size[root_i];
        } else {
            parent[root_j] = root_i;
            size[root_i] += size[root_j];
        }
    }
}

void merge_people_fast(int n, int q, std::vector<int> p, std::vector<int> q)
{
    int *parent = new int[n+1];
    int *size = new int[n+1];

    // Init parent and size.
    for (int i=1;i<=n;i++) {
        parent[i] = i;
        size[i] = 1;
    }

    for (int i=0;i<q;i++) {
        if (q[i]==0) {
            // print
            int root = find(p[i], parent);
            cout << size[root] << endl;
        }
        else {
            // merge p and q
            unite(p[i], q[i], parent, size);
        }
    }

    delete []parent;
    delete []size;
}
