#include <iostream>
#include <queue>
using namespace std;
int N,M;
int arr[9];
void a(int depth, int q) {
	if (depth == M) {
		for (int i = 1; i <= M; i++) {
			cout << arr[i] << " ";
		}
		cout << endl;
	}
	else {
		for (int i = 1; i <= N; i++) {
			if (i >= arr[q-1]) {
				arr[q] = i;
				a(depth+1,q+1);
			}
		}
	}
}


int main() {
	cin >> N >> M;
	a(0,1);

	return 0;
}
