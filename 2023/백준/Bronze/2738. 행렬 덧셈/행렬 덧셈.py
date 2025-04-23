N, M = map(int, input().split())

A = []
B = []
C = []

for i in range(N):
    A.append([])
    A[i]=list(map(int, input().split()))

for i in range(N):
    B.append([])
    B[i]=list(map(int, input().split()))

for i in range(N):
    C.append([])
    for j in range(M):
        C[i].append(A[i][j]+B[i][j])


for i in range(N):
    print(*C[i])
