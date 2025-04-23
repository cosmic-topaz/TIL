N, X = map(int, input().split())
A = list(map(int, input().split()))
for n in range(0, N):
    if A[n] < X:
        print(A[n], end=' ')
print()