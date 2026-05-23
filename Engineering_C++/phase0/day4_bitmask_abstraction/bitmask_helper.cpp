#include <iostream>
#include <string>
#include <vector>

std::string maskToBinaryString(long long mask, int n) {
    std::string result;

    for (int i = n - 1; i >= 0; i--) {
        if (mask & (1ll << i)) {
            result.push_back('1');
        }else {
            result.push_back('0');
        }
    }

    return result;
}

long long subsetSumFromMask(const std::vector<long long>& values, long long mask) {
    long long sum = 0;

    for (int i = 0; i < static_cast<int>(values.size()); i++) {
        if (mask & (1ll << i)) {
            sum += values[i];
        }
    }

    return sum;
}

int main() {
    std::vector<long long> values = {3, 5, 7, 8, 1, 6, 2, 9};
    int n = static_cast<int>(values.size());

    for (long long mask = 0; mask < (1ll << n); mask++) {
        std::cout << maskToBinaryString(mask, n)
                  << "->"
                  << subsetSumFromMask(values, mask) << '\n';
    }

    return 0;
}