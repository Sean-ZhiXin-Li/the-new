#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> apples(n);
    for (int i = 0; i < n; i++) {
        cin >> apples[i];
    }

    long long totalSum = 0;

    for (long long x : apples) {
        totalSum += x;
    }

    long long bestDiff = INT_MAX;

    for (long long mask = 0; mask < (1ll << n); mask ++) {
        long long groupSum = 0;

        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                groupSum += apples[i];
            }
        }

        long long otherSum = totalSum - groupSum;

        long long diff = llabs(groupSum - otherSum);

        bestDiff = min(bestDiff, diff);
    }

    cout << bestDiff << '\n';

    return 0;
}