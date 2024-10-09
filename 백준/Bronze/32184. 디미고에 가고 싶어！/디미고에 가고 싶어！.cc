#include <iostream>
using namespace std;
int main() {
	int N,M;
	int cnt = 0;
	cin >> N >> M;
	if (M % 2 == 0 && N % 2 != 0) {
		cout << (M-N+1)/2 << endl;
	}
	else {
		cout << (M-N+1)/2 + 1 << endl;
	}
	return 0;
}