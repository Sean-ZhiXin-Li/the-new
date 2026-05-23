#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;

    map<int, int> frequency;

    for(int i = 0; i < n; i++){
        int value;
        cin >> value;
        frequency[value]++;
    }

    int bestValue = 0;
    int bestCount = -1;

    for (const auto& entry : frequency){
        int value = entry.first;
        int count = entry.second;

        if (count > bestCount){
            bestCount = count;
            bestValue = value;
        }
    }

    cout << bestValue << " " << bestCount << '\n';
    return 0;
}