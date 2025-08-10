
int cookies(int k, vector<int> A)
{
    std::priority_queue<int, std::vector<int>, std::greater<int>> ms;

    for (auto a : A) ms.push(a);

    int n=0;

    while (ms.top()<k) {
        if(ms.size()==1) return -1;

        int a = ms.top(); ms.pop();
        int b = ms.top(); ms.pop();

        ms.push(a + b+ b);

        n++;
    }

    return n;
}
