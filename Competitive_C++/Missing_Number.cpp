# include<iostream>
# include<string>
using std::cout;
using std::cin;

int main() {
    long long n;
    cin >> n;
    long long exceptedSum = n * (n + 1) / 2;
    long long actualSum = 0;

    for (long long i = 0; i < n - 1; i++) {
        long long value;
        cin >> value;
        actualSum += value;
    }

    cout << exceptedSum - actualSum << '\n';
}