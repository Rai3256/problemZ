"""
Competitive Programming Python 3 / PyPy 3 Solution Template
Copy this file inside ComProg/solutions/ (e.g. 4A_watermelon.py), fill in solve()
and TEST_CASES, then run:
    python3 ../run_tests.py solutions/4A_watermelon.py
When all TEST_CASES pass, it automatically commits & pushes to Rai3256/problemZ.
"""

import sys


sys.setrecursionlimit(300000)


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        out.append(str(sum(arr)))

    sys.stdout.write("\n".join(out) + "\n")


TEST_CASES = [
    ("2\n3\n1 2 3\n2\n4 5\n", "6\n9\n"),
]


if __name__ == "__main__":
    solve()
