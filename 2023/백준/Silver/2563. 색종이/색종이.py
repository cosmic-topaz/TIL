paper = [[False]*100 for i in range(100)]
def pp():
    count = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j]:
                count += 1
                # print('◼︎', end='')
            else:
                pass
                # print('◻︎', end='')
    print(count)

# for i in range(100):
#     for j in range(100):
#         if paper[i][j]:
#             print('◼︎', end='')
#         else:
#             print('◻︎', end='')
#     print()

N = int(input())
for p in range(N):
    col, row = map(int, input().split())
    for i in range(90-row, 100-row):
        for j in range(col, col+10):
            paper[i][j] = True

pp()
