#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int sum = 0;
    string s;
    cin >> s;
    sort(s.begin(), s.end(),greater<int>());

    for (int i = 0; i < s.length(); i++) {
        sum += s[i]-'0';
    }

    if (sum % 3 == 0 && s[s.length()-1] == '0') {
        cout << s << endl;
    }
    else {
        cout << -1 << endl;
    }
}