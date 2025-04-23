def star(N):
    if N == 3:
        pattern = [['*' for i in range(N)] for i in range(N)]
        pattern[1][1] = ' '
        return pattern
    else:
        pattern = [['*' for i in range(N)] for i in range(N)]
        sub_pattern = star(N//3)
        for row in range(0, N, N//3):
            for col in range(0, N, N//3):
                for i in range(N//3):
                    for j in range(N//3):
                        pattern[i+row][j+col] = sub_pattern[i][j]
        for row in range(N//3, 2*N//3):
            for col in range(N//3, 2*N//3):
                pattern[row][col] = ' '
        return pattern

N = int(input())
[print(*x, sep='') for x in star(N)]