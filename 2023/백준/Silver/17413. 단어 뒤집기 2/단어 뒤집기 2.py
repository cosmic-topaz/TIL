from collections import deque
def f(S):
    deq = deque()
    stack = []
    i = 0
    while i < len(S):
        if S[i] == '<':
            stack.extend(deq)
            deq = deque()
            stack.append(S[i])
            while stack[-1] != '>':
                i += 1
                stack.append(S[i])
            i += 1
            continue
        if S[i] == ' ':
            deq.append(' ')
            stack.extend(deq)
            deq = deque()
        else:
            deq.appendleft(S[i])
        i += 1

    if deq:
        stack.extend(deq)
    return ''.join(stack)

import sys


input = sys.stdin.readline

T = 1
for _ in range(T):
    # N, K = map(int, input().split())
    S = input().strip()
    print(f(S))