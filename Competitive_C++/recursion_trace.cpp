#include <iostream>

void dfs(int depth) {
    if (depth == 3) {
        return;
    }

    std::cout << depth << '\n';
    dfs(depth + 1);
}

int main() {
    dfs(0);
    return 0;
}