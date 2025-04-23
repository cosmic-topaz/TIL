import sys
input_ = sys.stdin

N = int(input_.readline())
cnt1, cnt2 = 0, 0

grid = [input_.readline().rstrip() for i in range(N)]
grid1 = ['X'+x+'X' for x in grid]
grid2 = ['X'+ ''.join(x[i] for x in grid)+'X' for i in range(N)]

# [print(x, y) for x, y in zip(grid1, grid2)]

for i in range(N):
    x = grid1[i]
    while x.count('X.X')+ x.count('XX') > 0:
        x = x.replace('X.X', 'X')
        x = x.replace('XX', 'X')

    cnt1 += x.count('X')-1

for i in range(N):
    x = grid2[i]
    while x.count('X.X')+ x.count('XX') > 0:
        x = x.replace('X.X', 'X')
        x = x.replace('XX', 'X')

    cnt2 += x.count('X')-1

# [print(x, y) for x, y in zip(grid1, grid2)]

print(cnt1, cnt2)