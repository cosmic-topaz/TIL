from collections import deque
def f(N, K):
    circle = deque([i for i in range(1, N+1)])
    rst = []
    x = 1
    while circle:
        if x%K:
            circle.append(circle.popleft())
            x += 1
        else:
            rst.append(str(circle.popleft()))
            x += 1
    return '<'+', '.join(rst)+'>'

import sys


input = sys.stdin.readline

T = 1
for _ in range(T):
    N, K = map(int, input().split())
    print(f(N, K))