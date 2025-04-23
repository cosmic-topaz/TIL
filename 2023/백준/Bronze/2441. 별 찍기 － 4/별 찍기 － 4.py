N = int(input())
star = ['*']*N
for _ in range(N):
    print(*star, sep='')
    star[_] = ' ' 
