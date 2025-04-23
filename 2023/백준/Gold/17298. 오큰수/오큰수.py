from collections import deque
def f(N):
    A = list(map(int, input().split()))
    stack = []
    NGE = [-1]*N
    for i in range(N):
        if stack:
            while stack and A[i] > stack[-1][-1]:
                NGE[stack[-1][0]] = A[i]
                stack.pop()
        stack.append((i, A[i]))
    return ' '.join([str(x) for x in NGE])

import sys

input = sys.stdin.readline

T = 1
for _ in range(T):
    N = int(input())
    # N, K = map(int, input().split())
    # S = input().strip()
    print(f(N))