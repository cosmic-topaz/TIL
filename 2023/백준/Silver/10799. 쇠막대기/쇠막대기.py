def f(S):
    data = list(S.split('()'))
    cnt, rst = 0, 0
    for s in data:
        cnt += s.count('(')
        cnt -= s.count(')')
        rst += s.count(')')
        rst += cnt
    return rst

import sys
input = sys.stdin.readline

T = 1
for _ in range(T):
    # N, K = map(int, input().split())
    S = input().strip()
    print(f(S))