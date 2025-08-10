
#include <vector>
#include <iostream>

long long power(long long base, long long exp) {
    long long res = 1;
    base %= 1000000007; // Modulo
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 1000000007;
        base = (base * base) % 1000000007;
        exp /= 2;
    }
    return res;
}

int legoBlocks(int n, int m) {
    long long MOD = 1000000007;

    // Step 1: Calculate ways to build a single row of width i
    std::vector<long long> ways(m + 1, 0);
    ways[0] = 1;
    for (int i = 1; i <= m; ++i) {
        if (i >= 1) ways[i] = (ways[i] + ways[i - 1]) % MOD;
        if (i >= 2) ways[i] = (ways[i] + ways[i - 2]) % MOD;
        if (i >= 3) ways[i] = (ways[i] + ways[i - 3]) % MOD;
        if (i >= 4) ways[i] = (ways[i] + ways[i - 4]) % MOD;
    }

    // Step 2: Calculate total ways to build a wall of height n and width i
    std::vector<long long> total(m + 1);
    for (int i = 0; i <= m; ++i) {
        total[i] = power(ways[i], n);
    }

    // Step 3: Calculate solid walls using inclusion-exclusion
    std::vector<long long> solid(m + 1);
    solid[0] = 1; // Not strictly needed for the final answer, but helps with calculations
    for (int i = 1; i <= m; ++i) {
        solid[i] = total[i];
        for (int j = 1; j < i; ++j) {
            long long term = (solid[j] * total[i - j]) % MOD;
            solid[i] = (solid[i] - term + MOD) % MOD; // Add MOD to handle negative results
        }
    }

    return solid[m];
}
