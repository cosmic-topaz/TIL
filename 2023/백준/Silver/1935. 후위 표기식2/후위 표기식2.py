
def f(N):
    exp = list(input().strip())[::-1]
    x = dict()
    for _ in range(65, 65+N):
        x[chr(_)] = float(input())
    for _ in '-+/*':
        x[_] = _
    stack = []
    rst, b, e = x[exp.pop()], None, None
    while exp or b:
        if b is None:
            b = exp.pop()
            b = x.get(b, b)
        if type(b) is float:
            if e is None:
                e = exp.pop()
                e = x.get(e, e)
            if type(e) is str:
                if e == '+':
                    rst += b
                elif e == '-':
                    rst -= b
                elif e == '/':
                    rst /= b
                else:
                    rst *= b
                b, e = None, None
            else:
                stack.append(rst)
                rst, b, e = b, e, None
        else:
            if e is not None:
                exp.append(e)
            rst, b, e = stack.pop(), rst, b
    return rst

import sys
input = sys.stdin.readline

T = 1
for _ in range(T):
    N = int(input())
    # N, K = map(int, input().split())
    # S = input().strip()
    print(f'{f(N):.2f}')