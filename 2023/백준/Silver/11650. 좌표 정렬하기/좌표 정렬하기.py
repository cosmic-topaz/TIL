import sys
N = int(input())
input_ = sys.stdin
point = {}
for _ in range(N):
    x, y = map(int, input_.readline().split())
    point[x] = point.get(x, [])
    point[x].append(y)
for x in sorted(point):
    for y in sorted(point[x]):
        print(x, y)