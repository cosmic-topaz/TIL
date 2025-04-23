import sys
N = int(input())
input_ = sys.stdin
point = {}
for _ in range(N):
    x, y = map(int, input_.readline().split())
    point[y] = point.get(y, [])
    point[y].append(x)
for y in sorted(point.keys()):
    for x in sorted(point[y]):
        print(x, y)