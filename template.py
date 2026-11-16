"""
Competitive Programming Python 3 / PyPy 3 Template
Save files inside ComProg/solutions/ (e.g. 4A_watermelon.py), paste to Codeforces to test,
then run in terminal after AC:
    pz 4A_watermelon.py
(or just `pz` if it's the only modified/new file in ComProg/solutions/)
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


if __name__ == "__main__":
    solve()
