#include <iostream>
#include <cmath>
using namespace std;
int a = 10001;
int arr[10001];

void Eratos(int N) {
    int s1,s2;
    int diff = 100001;
    for (int i = 2; i <= a; i++) {
        arr[i] = i;
    }
    
    for (int i = 2; i <= sqrt(a); i++) {
        if (arr[i] == 0)
            continue;
        for (int j = i*i; j <= a; j+= i) {
            arr[j] = 0;
        }
    }

    for (int i = 2; i <= N; i++) {
        if (arr[i] != 0 && arr[N-i] != 0) {
            if (abs(arr[i]-arr[N-i]) < diff) {
                s1 = arr[i];
                s2 = arr[N-i];
                diff = abs(arr[i]-arr[N-i]);
            }
        }
    }
    cout << s1 << " " << s2 << endl;

}

int main() {
    int T,N;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        Eratos(N);
    }
    return 0;
}