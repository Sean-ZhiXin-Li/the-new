#include <iostream>
#include <vector>

void printVector(const std::vector<int>& values) {
    for (int value : values) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}

int main() {
    std::vector<int> values = {1, 2, 3, 4, 5};

    printVector(values);

    return 0;
}
