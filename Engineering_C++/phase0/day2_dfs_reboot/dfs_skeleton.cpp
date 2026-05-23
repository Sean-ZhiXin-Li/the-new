#include <iostream>
#include <vector>

void dfs (int depth, int maxDepth, std::string& path) {
    if (depth == maxDepth) {
        std::cout << path << '\n';
        return;
    }

    path.push_back('A' + depth);
    dfs(depth + 1, maxDepth, path);
    path.pop_back();
}

int main() {
    std::string path;

    dfs(0, 3, path);

    return 0;
}