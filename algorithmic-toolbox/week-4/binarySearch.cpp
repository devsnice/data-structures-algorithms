#include <vector>

using namespace std;

#include <vector>
#include <math.h>

using std::vector;

int main(const vector<long int> &array, long int key, long int low, long int high) {

    if(high < low) {
        return -1;
    }

    long int mid = low + ceil((high - low) / 2);

    if(array[mid] == key) {
        return mid;
    }

    if(array[mid] < key) {
        return binary_search(array, key, mid + 1, high);
    }
    else {
        return binary_search(array, key, low, mid - 1);
    }

}