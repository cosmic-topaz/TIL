def f(N):
    A = list(map(int, input().split()))
    count_A = Counter(A)
    stack = []
    NGF = [-1]*N
    for i in range(N):
        if stack:
            while stack and count_A[A[i]] > count_A[stack[-1][-1]]:
                NGF[stack[-1][0]] = A[i]
                stack.pop()
        stack.append((i, A[i]))
    return ' '.join([str(x) for x in NGF])

import sys
from collections import Counter

input = sys.stdin.readline

T = 1
for _ in range(T):
    N = int(input())
    # N, K = map(int, input().split())
    # S = input().strip()
    print(f(N))