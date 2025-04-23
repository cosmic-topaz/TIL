import sys
from collections import Counter
N, M, B = map(int, input().split())

data = []
for n in range(N):
    data.extend(list(map(int, sys.stdin.readline().split())))

data = dict(Counter(data))

t = [0 for h in range(257)]
result = {}
# t[h] 높이 h로 땅을 고르는데 걸리는 시간
for h in range(257):
    b = B
    for x in data.keys():
        t[h] += data[x]*abs(x-h)
        b += (x-h)*data[x]
        if x > h:
            t[h] +=data[x]*(x-h)
    if b >= 0:
        result[t[h]] = result.get(t[h], [])
        result[t[h]].append(h)
# print(result)
time = min(result.keys())
height = max(result[time])
print(time, height)