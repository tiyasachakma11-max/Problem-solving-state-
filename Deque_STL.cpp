#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, K;
        cin >> N >> K;

        vector<int> arr(N);

        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        deque<int> dq;

        for (int i = 0; i < N; i++) {

            // Remove elements outside the current window
            while (!dq.empty() && dq.front() <= i - K) {
                dq.pop_front();
            }

            // Remove smaller elements from the back
            while (!dq.empty() && arr[dq.back()] <= arr[i]) {
                dq.pop_back();
            }

            dq.push_back(i);

            // Print maximum when window size reaches K
            if (i >= K - 1) {
                cout << arr[dq.front()] << " ";
            }
        }

        cout << endl;
    }

    return 0;
}
