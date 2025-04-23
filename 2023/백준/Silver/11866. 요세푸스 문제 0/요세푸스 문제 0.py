def josephus(N, K):
    x = [i for i in range(1, N+1)]
    cnt = 0
    i = 0
    y = []
    while cnt < N:
        if i%K==K-1:
            y.append(x[i])
            cnt += 1
        else:
            x.append(x[i])
        i += 1

    return y
        
        

N, K = map(int, input().split())
print('<', end='')
print(*josephus(N, K), sep=', ', end='')
print('>')