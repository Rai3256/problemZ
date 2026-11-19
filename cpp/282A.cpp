#include <iostream>
using namespace std;

int main() {

  int statements, res = 0;
  cin >> statements;
  string input;

  while (statements > 0) {
    cin >> input;
    if (input == "++X" || input == "X++") {
      res++;
    } else if (input == "--X" || input == "X--") {
      res--;
    }
    statements--;
  }
  cout << res;
  return 0;
}