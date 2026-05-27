#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool comparePair(const pair<int, int>& a,
                const pair<int, int>& b)
{
    if (a.first != b.first){
        return a.first < b.first;
    }

    return a.second > b.second;
}

void solve(){
    int n;
    cin >> n;

    vector<pair<int, int>> events;

    for(int i = 0; i < n; i++){
        int time;
        int priority;
        cin >> time >> priority;
        events.push_back({time, priority});
    }

    sort(events.begin(), events.end(), comparePair);

    for (pair<int, int> event: events){
        cout << event.first << " " << event.second << '\n';
    }
}

int main(){
    solve   ();
    return 0;
}