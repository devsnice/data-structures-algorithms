#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> optimal_summands(int n) {
    vector<int> summands;
    int i = 1;
    int sum = 0;

    while(sum < n) {
        int restSumAfterThisSolution = n - sum - i;
        bool nextStepWillRepeatNumber = false;

        auto it = find(summands.begin(), summands.end(), restSumAfterThisSolution);

        nextStepWillRepeatNumber = it != summands.end();

        if (!nextStepWillRepeatNumber && i != restSumAfterThisSolution) {
            summands.push_back(i);
            sum += i;
        }

        i++;
    }

    return summands;
}

int main() {
    int n;
    std::cin >> n;
    vector<int> summands = optimal_summands(n);
    std::cout << summands.size() << '\n';
    for (size_t i = 0; i < summands.size(); ++i) {
        std::cout << summands[i] << ' ';
    }
}
