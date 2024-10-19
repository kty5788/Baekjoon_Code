#include <iostream>
#include <string>
using namespace std;
int main() {
	int T;
	string s;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> s;
		cout << s[0]-'0'+s[2]-'0' << endl;
	}

	return 0;
	
}