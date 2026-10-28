#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);

    int positive = 0, negative = 0, zero = 0;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        if (arr[i] > 0) {
            positive++;
        }
        else if (arr[i] < 0) {
            negative++;
        }
        else {
            zero++;
        }
    }

    cout << fixed << setprecision(6);

    cout << (double)positive / n << endl;
    cout << (double)negative / n << endl;
    cout << (double)zero / n << endl;

    return 0;
}