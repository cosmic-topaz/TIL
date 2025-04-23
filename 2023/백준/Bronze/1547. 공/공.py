import sys
from pprint import pprint
input = sys.stdin.readline
# 1547	공	https://www.acmicpc.net/problem/1547
cup = (1, 2, 3)
status = dict()
i = [0, 0, 1, 2, 0, 0, 3, 0, 0, 0]
for x in cup:
    for y in cup:
        if x != y:
            status[(x, y, 6-x-y)] = []
for s in status.keys():
    p1 = s.index(1)
    p2 = s.index(2)
    p3 = s.index(3)
    for _ in [(1, 2, 3), (2, 1, 3), (3, 2, 1), (1, 3, 2)]:
        x = [0, 0, 0]
        x[p1], x[p2], x[p3] = _
        status[s].append(tuple(x))

M = int(input())
s = (1, 2, 3)
for _ in range(M):
    x, y = map(int, input().split())
    s = status[s][i[x*y]]

print(s[0])