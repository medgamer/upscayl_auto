
class Node {
public:
    int data;
    Node *left, *right;

    Node(int d=0) {
        data = d;
        left = NULL;
        right = NULL;
    }
}

void preOrder(Node *root)
{
    std::vector<int> out;

    std::stack<Node*> tree;
    tree.push(root);
    while (!tree.empty()) {
        Node *node = tree.top();
        out.push_back(node->data);
        tree.pop();

        if (node->right) {
            tree.push(node->right);
        }
        if (node->left) {
            tree.push(node->left);
        }
    }

    for (auto d: out) {
        cout << d << " ";
    }
    cout << endl;
}
