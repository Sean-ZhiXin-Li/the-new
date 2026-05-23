#include <algorithm>
#include <cstdlib>
#include <climits>
#include <iostream>
#include <string>
#include <vector>

std::string maskToBinaryString(long long mask, int n) {
    std::string result;

    for (int i = n - 1; i >= 0; i--) {
        if (mask & (1LL << i)) {
            result.push_back('1');
        } else {
            result.push_back('0');
        }
    }

    return result;
}

long long subsetSumFromMask(const std::vector<long long>& values, long long mask) {
    long long sum = 0;

    for (int i = 0; i < static_cast<int>(values.size()); i++) {
        if (mask & (1LL << i)) {
            sum += values[i];
        }
    }

    return sum;
}

long long solveAppleDivision(const std::vector<long long>& apples) {
    int n = static_cast<int>(apples.size());
    long long totalSum = 0;

    for (long long value : apples) {
        totalSum += value;
    }

    long long bestDifference = LLONG_MAX;

    for (long long mask = 0; mask < (1LL << n); mask++) {
        long long groupSum = subsetSumFromMask(apples, mask);
        long long otherSum = totalSum - groupSum;
        long long difference = std::llabs(groupSum - otherSum);

        bestDifference = std::min(bestDifference, difference);
    }

    return bestDifference;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<long long> apples(n);

    for (int i = 0; i < n; i++) {
        std::cin >> apples[i];
    }

    std::cout << solveAppleDivision(apples) << '\n';

    return 0;
}