#include <iostream>
using namespace std;

int main() {

  int tc;
  int cnt = 0;
  int arr[3];
  int sum = 0;

  cin >> tc;

  while (tc > 0) {
    for (int i = 0; i < 3; i++) {
      cin >> arr[i];
      sum += arr[i];
    }
    if (sum >= 2) {
      cnt++;
      sum = 0;
    } else {
      sum = 0;
    }
    tc--;
  }
  cout << cnt << endl;
}