#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> find_identical_elements(const std::vector<int>& list1, const std::vector<int>& list2) {
    std::vector<int> common_elements;
    auto it1 = list1.begin();
    auto it2 = list2.begin();

    while (it1 != list1.end() && it2 != list2.end()) {
        if (*it1 == *it2) {
            common_elements.push_back(*it1);
            ++it1;
            ++it2;
        } else if (*it1 < *it2) {
            ++it1;
        } else { // *it1 > *it2
            ++it2;
        }
    }
    return common_elements;
}

int pairs(int k, vector<int> arr)
{
    // sort first
    std::sort(arr.begin(), arr.end());

    // + k
    vector<int> plusk;
    for(auto a : arr) plusk.push_back(a + k);

    // find identical elements

    auto res = find_identical_elements(arr, plusk);

    return res.size();
}
