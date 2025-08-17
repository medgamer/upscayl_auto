
// Function to find the maximum number of non-overlapping intervals
int maxNonOverlappingIntervals(vector<vector<int>>& intervals) {
    // Sort intervals based on their end times
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });

    int count = 0;
    int end = INT_MIN;

    // Iterate through the sorted intervals
    for (const auto& interval : intervals) {
        // If the start time of the current interval is greater than or equal to the end time of the last selected interval
        if (interval[0] >= end) {
            // Select the current interval
            end = interval[1];
            count++;
        }
    }

    return count;
}
