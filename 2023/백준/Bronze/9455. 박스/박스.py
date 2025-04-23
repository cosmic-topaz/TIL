import sys
input_ = sys.stdin

def rotate(grid, n):
    return [[x[i] for x in grid[::-1]] for i in range(n)]

def box():
    input_ = sys.stdin
    m, n = map(int, input_.readline().split())
    grid = [list(map(int, input_.readline().split())) for i in range(m)]
    # [print(*line) for line in grid]
    grid = rotate(grid, n)
    # [print(*line) for line in grid]
    cnt = 0
    for line in grid:
        a = sum(i for i in range(m) if line[i] == 1)
        b = sum(line)
        cnt += a-b*(b-1)//2
    print(cnt)
    



T = int(input_.readline())
for test_case in range(T):
    box()