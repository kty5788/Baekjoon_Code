#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

bool prime[1001];

int Eratosthenes(int n, int k, int cnt) {
    for (int i = 2; i<= 1000; i++) {
        prime[i] = true;
    }

    for (int i = 2; i <= n; i++) {
        if (prime[i] != false) {
            for (int j = i; j <= n; j+=i) {
                if (prime[j] != false) {
                    prime[j] = false;
                    cnt += 1;
                    if (cnt == k) {
                        return j;
                    }
                }
            }
        }
    }
    return 0;
}

int main() {
    int N,K;
    cin >> N >> K;
    cout << Eratosthenes(N,K,0) << endl;
}