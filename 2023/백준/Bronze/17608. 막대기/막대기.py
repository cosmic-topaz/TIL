def f(N):
    stack = []
    for i in range(1, N+1):
        v = int(input())
        while True:
            if len(stack) == 0:
                stack.append(v)
                break
            if stack[-1] > v:
                stack.append(v)
                break
            else:
                stack.pop()
    return len(stack)

import sys
input = sys.stdin.readline

T = 1
for _ in range(T):
    print(f(int(input())))
