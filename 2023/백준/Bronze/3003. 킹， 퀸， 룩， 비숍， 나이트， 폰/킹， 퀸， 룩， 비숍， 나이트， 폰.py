# 킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8
numbers = list(map(int, input().split()))
pieces = (1, 1, 2, 2, 2, 8)
for i in range(len(pieces)):
    print(pieces[i]-numbers[i], end=' ')
print()