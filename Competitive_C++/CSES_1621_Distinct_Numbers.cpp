#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void solve(){
    int n;
    cin >> n;

    vector<int> numbers(n);

    for (int i = 0; i < n; i++){
        cin >> numbers[i];
    }

    sort(numbers.begin(), numbers.end());

    int distinctCount = 0;

    for (int i = 0; i < n; i++){
        if (i == 0 || numbers[i] != numbers[i - 1]){
            distinctCount++;
        }
    }

    cout << distinctCount << '\n';
}

int main(){
    solve();
    return 0;
}