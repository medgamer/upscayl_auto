#include <iostream>

// Base case for the recursion (when no more digits are left)
template <bool a>
int reversed_binary_value() {
    return a;
}

// Recursive case to process the variadic pack
template <bool a, bool b, bool... d>
int reversed_binary_value() {
    // Shifts the value from the rest of the pack and adds the current digit
    return (reversed_binary_value<b, d...>() << 1) + a;
}

// How to use it.
template <bool...digits>
bool check(int x, int y)
{
    int z = reversed_binary_value<digits...>();
    return (z+64*y==x);
}


int main() {
    // Example: reversed_binary_value<0,0,1>() would be 100 in binary, which is 4
    std::cout << "Reversed binary value of <0,0,1>: " << reversed_binary_value<0, 0, 1>() << std::endl;
    // Example: reversed_binary_value<1,1,0,1>() would be 1011 in binary, which is 11
    std::cout << "Reversed binary value of <1,1,0,1>: " << reversed_binary_value<1, 1, 0, 1>() << std::endl;
    return 0;
}
