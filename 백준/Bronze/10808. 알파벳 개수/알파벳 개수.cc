#include <iostream>
using namespace std;
int main() {
	char s[101];
	int alphabet[27] = {0,};
	cin >> s;

	for (int i = 0; s[i]; i++) {
		alphabet[s[i]-'a']++;
	}

	for (int i = 0; i < 26; i++) {
		cout << alphabet[i] << " ";
	}
	cout << endl;

	return 0;
}