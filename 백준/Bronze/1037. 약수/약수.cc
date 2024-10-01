#include <iostream>
using namespace std;

int main() {
    int N,x;
    cin >> N;
    int min = 1000001;
    int max = -1;
    int arr[N];
    if (N == 1) {
        cin >> x;
        cout << x*x << endl;
    }
    else {
        for (int i = 0; i < N; i++) {
            cin >> x;
            if (x > max)
            max = x;

            if (x < min)
            min = x;
        }
        cout << min*max << endl;
    }

    return 0;
}