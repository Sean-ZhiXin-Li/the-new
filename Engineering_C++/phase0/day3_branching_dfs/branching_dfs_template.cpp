#include <iostream>
#include <string>
#include <vector>

void printIndent(int depth) {
    for (int i = 0; i < depth; i++) {
        std::cout << " ";
    }
}

void dfs(const std::string& choices, std::string path, std::vector<char>& used, int depth) {
    if (path.size() == choices.size()) {
        printIndent(depth);
        std::cout << "leaf: " << path << '\n';
        return;
    }

    for (int i = 0; i < static_cast<int>(choices.size()); i++) {
        if(used[i]) {
            continue;
        }

        printIndent(depth);
        std::cout << "choose: " << choices[i] << '\n';

        used[i] = 1;
        path.push_back(choices[i]);

        dfs(choices, path, used, depth + 1);

        path.pop_back();
        used[i] = 0;

        printIndent(depth - 1);
        std::cout << "undo: " << choices[i] << '\n';
    }
}

int main() {
    std::string choices = "ABC";
    std::string path;
    std::vector<char> used(choices.size(), 0);

    dfs(choices, path, used, 0);

    return 0;
}