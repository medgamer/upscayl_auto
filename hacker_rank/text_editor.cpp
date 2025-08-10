
// 4 kinds of ops
// 1 = append a string
// 2 = delele k chars
// 3 = print kth char
// 4 = undo previous OP 1 or 2.
void text_editor(vector<int> ops, vector<string> paras)
{
    string buffer = "";
    int n = ops.size();

    struct opt {
        int op;
        int k;
        string str;
    };
    stack<opt> mydata;

    for (int i=0;i<n;i++) {
        auto len = buffer.length();
        opt one;
        int op = ops[i], k = 0;
        string lastk = "";
        if (ops[i]==4) {
            one = mydata.top();
            mydata.pop();
            if (one.op==1) {
                // remove == op 2
                buffer = buffer.substr(0, len-one.k);
            }
            else if (one.op==2) {
                // add back == op 1
                buffer += one.str;
            }
            continue;
        }

        switch(op) {
            case 1:
                buffer += paras[i];
                one.op = 1;
                one.k = paras[i].length();
                one.str = paras[i];
                mydata.push(one);
                break;
            case 2:
                k = stoi(paras[i]);
                lastk = buffer.substr(len-k, k);
                buffer = buffer.substr(0, len-k);
                one.op = 2;
                one.k = k;
                one.str = lastk;
                mydata.push(one);
                break;
            case 3:
                // k-th char = buffer[k-1] ;-)
                k = stoi(paras[i]);
                cout << buffer[k-1] << endl;
                break;
            default:;
        }
    }
}
