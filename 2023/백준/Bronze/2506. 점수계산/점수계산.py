N = int(input())
OX = list(map(int, input().split()))

# 1번 문제는 맞추면1: 1점 틀리면0: 0점
# 2번 문제 부터는 맞추면1: 앞문제의 점수 + 1점 , 틀리면0: 0점
for n in range(1, N):
    if OX[n] :
        OX[n] = OX[n-1]+1

print(sum(OX))