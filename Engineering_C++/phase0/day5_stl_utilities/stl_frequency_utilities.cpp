#include <iostream>
#include <map>
#include <vector>

void debugPrintVector(const std::vector<int>& values){
    for (int value : values){
        std::cerr << value << " ";
    }

    std::cerr << '\n';

}

std::map<int, int> buildFrequencyMap(const std::vector<int>& values){
    std:: map<int, int> frequency;

    for (int value : values){
        frequency[value]++;
    }

    return frequency;
}

void debugPrintFrequencyMap(const std::map<int, int>& frequency){
    for(const auto& entry : frequency){
        std::cerr   << entry.first
                    << " ->"
                    << entry.second
                    << '\n';
    }
}

std::pair<int, int> findMostFrequencyValue(const std::map<int, int>& frequency){
    int bestValue = 0;
    int bestCount = -1;

    for(const auto& entry : frequency){
        int value = entry.first;
        int count = entry.second;

        if (count > bestCount){
            bestCount = count;
            bestValue = value;
        }
    }

    return {bestValue, bestCount};
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> values;

    for (int i = 0; i < n; i++) {
        int value;
        std::cin >> value;
        values.push_back(value);
    }

    debugPrintVector(values);

    std::map<int, int> frequency = buildFrequencyMap(values);

    debugPrintFrequencyMap(frequency);

    std::pair<int, int> result = findMostFrequencyValue(frequency);

    std::cout << result.first << " " << result.second << '\n';

    return 0;
}