#include <iostream>
#include <string>
using namespace std;
int main() {
	string s;
	cin >> s;
	
	for (int i = 1; i <= s.size(); i++) {
		cout << s[i-1];
		if (i % 10 == 0)
			cout << '\n';
	}
	cout << endl;
}