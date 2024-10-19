#include <iostream>
#include <string>
using namespace std;
int main() {
	string s;
	int alphabet[27] = {0,};
	cin >> s;

	for (int i = 0; i < s.size(); i++) {
		alphabet[int(s[i])-'a'] += 1;
	}

	for (int i = 0; i < 26; i++) {
		cout << alphabet[i] << " ";
	}
	cout << endl;

	return 0;
}