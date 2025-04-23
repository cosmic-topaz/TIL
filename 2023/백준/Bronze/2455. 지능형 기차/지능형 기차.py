def f():
    Lst = [x[1]-x[0] for x in [list(map(int, input().split())) for _ in range(4)]]
    for i in range(1, len(Lst)):
        Lst[i] += Lst[i-1]
        if Lst[i] >= 10000:
            return 10000

    return max(Lst)
import sys
input = sys.stdin.readline
inputs = sys.stdin.readlines

T = 1
for _ in range(T):
    # s = input()
    rst = f()
    print(rst)