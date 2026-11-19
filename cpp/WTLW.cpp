#include <iostream>
using namespace std;
 
int main() {
  int tc = 0;
 
  cin >> tc;
  while (tc > 0) {
 
    string s;
    cin >> s;
    int cnt = (int)s.length() - 2;
    char first = s.at(0);
    char last = s.at(s.length() - 1);
 
    if (s.length() <= 10) {
      cout << s << endl;
    } else {
      cout << first << cnt << last << endl;
    }
    cnt = 0;
    tc--;
  }
}