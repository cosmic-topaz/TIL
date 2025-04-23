N = int(input())
x = []
for i in range(N):
    a, b = map(int, input().split())
    x.append((i, a, b))
y = []
for i in range(N):
    y.append([i, 0])
    for j in range(N):
        if x[j][1] > x[i][1] and x[j][2] > x[i][2]:
            y[i][1] += 1

print(*[y[i][1]+1 for i in range(N)])