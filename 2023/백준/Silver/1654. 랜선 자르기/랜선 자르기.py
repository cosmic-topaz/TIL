import sys
from collections import deque
K, N = map(int, input().split()) # K <= N
a = 1
b = 0
n = deque()
for i in range(K):
    x = int(sys.stdin.readline().rstrip())
    n.append(x)
    b += x
b //= N


while True:
    v = 0
    s = (a+b)//2
    for i in range(len(n)):
        x = n.popleft()
        if x//a == 0:
            pass  
        else:
            n.append(x)
            v += x//s
    if v >= N:
        a = s
    else:
        b = s
    if a - b > -2:
        v = sum(x//b for x in n)
        if v >= N:
            print(b)
            exit()
        else:
            print(a)
            exit()