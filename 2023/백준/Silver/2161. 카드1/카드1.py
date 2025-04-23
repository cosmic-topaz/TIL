# 2161 카드1
N = int(input())
x = [i for i in range(1, N+1)]
cnt = 0
i = 0
y = []
while cnt < N:
    y.append(x[i])
    i += 1
    cnt += 1
    if i < len(x):
        x.append(x[i])
        i += 1
    
print(*y)