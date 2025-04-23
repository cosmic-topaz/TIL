M, N = map(int, input().split())
matrix = [input() for m in range(M)]

# print(*matrix, sep='\n')
check = [[0 for n in range(N)] for m in range(M)]
i, j = 0, 0
for i in range(M):
    for j in range(N):
        if ((i+j)%2)*'B'+ ((i+j+1)%2)*'W' != matrix[i][j]:
            check[i][j] = 1

# pprint(matrix)
# pprint(check)
result = []

for i in range(M-7):
    for j in range(N-7):
        # print(i, j)
        x = sum([check[_][j:j+8].count(1) for _ in range(i, i+8)])
        # print(i, j, x)
        result.append(min(x, 64-x))

print(min(result))