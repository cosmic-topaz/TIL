from collections import deque
def f(S):
    deq = deque(list(S))
    deq2 = deque()
    N = int(input())
    for _ in range(N):
        cmd = input().strip()
        if cmd[0] == 'L':
            if deq:
                deq2.appendleft(deq.pop())
        if cmd[0] == 'B':
            if deq:
                deq.pop()
        if cmd[0] == 'D':
            if deq2:
                deq.append(deq2.popleft())
        if cmd[0] == 'P':
            deq.append(cmd[2])
    return ''.join(deq+deq2)

import sys

input = sys.stdin.readline
T = 1
for _ in range(T):
    S = input().strip()
    print(f(S))

