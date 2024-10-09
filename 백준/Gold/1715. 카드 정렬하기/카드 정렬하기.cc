#include <iostream>
#include <queue>
using namespace std;
int main() {
	int N;
	int cnt = 0;
	int card[100001];
	priority_queue<int, vector<int>,greater<int> > pq;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		pq.push(x);
	}
	if (N == 1) {
		cout << 0 << endl;
		return 0;
	}
	while (1) {
		int temp = 0;
		for (int i = 0; i < 2; i++) {
			temp += pq.top();
			pq.pop();
		}
		cnt += temp;
		if (pq.empty()) {
			cout << cnt << endl;
			return 0;
		}
		else {
			pq.push(temp);
		}
	}
	return 0;
}