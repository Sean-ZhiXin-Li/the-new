#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using std::cout;
using std::cin;
using std::string;
using std::vector;
string s;
string path;
bool used[8];
vector<string> results;

void search() {
    if (path.size() == s.size()) {
        results.push_back(path);
        return;
    }

    for (int i = 0; i < (int)s.size(); i++) {
        if (used[i]) {
            continue;
        }

        if (i > 0 && s[i] == s[i - 1] && !used[i - 1]) {
            continue;
        }

        used[i] = true;
        path.push_back(s[i]);

        search();

        path.pop_back();
        used[i] = false;
    }
}

int main() {
    cin >> s;
    sort(s.begin(), s.end());
    search();

    cout << results.size() << '\n';
    for (const string& result : results) {
        cout << result << '\n';
    }

    return 0;
}