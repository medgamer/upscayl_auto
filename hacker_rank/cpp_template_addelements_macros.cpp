
// Make iostream faster with a lot of I/O
#define cin ios_base::sync_with_stdio(false);cin.tie(NULL); cin

#define toStr(a) #a

#define foreach(v,i) for(int i=0;i<v.size();i++)

#define io(v) cin >> v

#define FUNCTION(name, operator) \
    void name(int &current, int candidate) { \
        if (candidate operator current) { \
            current = candidate; \
        } \
    }
    
