
// palindrom test

#include <string>

// Check string itself.
bool is_palin(string s)
{
    auto sc = s;
    std::reverse(sc.begin(), sc.end());
    return (sc==s);
}

// Check string  removing its id char.
bool is_palin(string s, int id)
{
    int n = s.length();
    if (id<0 || id>=n) return false;

    // (1, .., n-1) case
    if (id==0) return is_palin(s.substr(1, n-1));
    // (0, .., n-2) case
    else if (id==n-1) return is_palin(s.substr(0, n-1));
    else {
        auto sr = s.substr(0, id) + s.substr(id+1);
        return is_palin(sr);
    }
    return false;
}

int pal_ind(string s)
{
    if (is_palin(s)) return -1;

    auto sr = s;
    std::reverse(sr.begin(), sr.end());

    int n = s.length();
    // Compare s with s.reverse char by char
    for(int i=0;i<n;i++) {
        if (s[i] != sr[i]) {
            // Not equal at i vs n-1-i => check both removing i or n-1-i.
            if (is_palin(s, i)) return i;
            else if (is_palin(s, n-1-i)) return n-1-i;
            // Neitherway is palindrom => must have >=2 differences => -1.
            else return -1;
    }

    // s == sr case.
    return -1;
}
