
void pet_sum(vector<vector<int>> pumps, vector<int> &psum)
{
    // Calculate poump 0 => i
    int n = pumps.size();
    int sum = 0;
    for(int i=0;i<n;i++) {
        sum += pumps[i][0] - pumps[i][1];
        // from 0 to i+1
        psum.push_back(sum);
    }
}

// Both i, j in [0, n-1]
int pet_sum_from_to(vector<int> psum, int i, int j)
{
    if (i==j) {
        // round trip
        int n = psum.size();
        // [i, n-1] + [n-1, 0] + [0, i]
        return psum[n-1];
    }
    else if (i==0) {
        // [0, j]
        return psum[j-1];
    }
    else if (i<j) {
        // [i, j]
        return psum[j-1] - psum[i-1];
    }
    else {
        int n = psum.size();
        // i>j => [i, n-1] + [n-1, 0] + [0, j]
        return psum[n-1] - psum[i-1] + psum[j-1];
    }
}

int tour_slow(vector<vector<int>> pumps)
{
    vector<int> psum;
    pet_sum(pumps, psum);

    int n = psum.size();
    for (int i=0;i<n;i++) {
        bool pass = true;
        for (int j=i+1; j<=i+n;j++) {
            int jd = j%n;
            if (pet_sum_from_to(psum, i, jd)<0) {
                pass = false;
                break;
            }
        }
        if (pass) return i;
    }
    return -1;
}

int tour_fast(vector<vector<int>> pumps)
{
    int n = pumps.size();

    int start_index = 0;
    int current_petrol = 0;

    for (int i=0;i<n;i++) {
        current_petrol += pumps[i][0] - pumps[i][1];

        if (current_petrol<0) {
            start_index = i+1;
            current_petrol = 0;
        }
    }
    return start_index;
}
