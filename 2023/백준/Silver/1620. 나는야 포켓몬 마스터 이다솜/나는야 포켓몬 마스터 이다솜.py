import sys
input = sys.stdin.readline

# 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())
dogam = [0]*(N+1)
d_dict = {}
for i in range(1, N+1):
    dogam[i] = input().rstrip()
    d_dict[dogam[i]] = i

for _ in range(M):
    x = input().rstrip()
    if x[0] in '0123456789':
        print(dogam[int(x)])
    else:
        print(d_dict[x])
