#include <iostream>
using namespace std;
int n,m;
int arr[8] = {};
void combination(int depth, int next) {
    if (depth == m) {
        for (int i = 0; i <= m-1; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }
    for (int i = next; i <= n; i++) {
        arr[depth] = i;
        combination(depth+1, i+1);
    }
}


int main() {
    cin >> n >> m;
    combination(0,1);

    return 0;
}