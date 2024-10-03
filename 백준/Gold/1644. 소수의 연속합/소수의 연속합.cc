#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int max_n = 40000000;
bool prime[40000001];

void Eratos() {
    for (int i = 2; i <= max_n; i++) {
        prime[i] = true;
    }

    for (int i = 2; i <= sqrt(max_n); i++) {
        if (!prime[i])
            continue;
        for (int j = i*2; j <= max_n; j+=i) {
            prime[j] = false;
        }
    }
}


int main() {
    int cnt = 0;
    int n;
    cin >> n;
    Eratos();

    for (int i = 0; i <= n; i++) {
        if (prime[i]) {
            int sum = 0;
            for (int j = i; j <= max_n; j++) {
                if (prime[j]) {
                    sum += j;
                    if (sum == n) {
                        cnt += 1;
                    }
                    else if (sum > n) {
                        break;
                    }
                }
            }
        }
    }
    cout << cnt << endl;
}