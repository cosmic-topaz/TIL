T = int(input())
def getSize(a, b):
    return lst[a][b-1]

lst = []
lst.append([])
for j in range(1, 15):
    lst[0].append(j)
for i in range(1, 15):
    lst.append([])
    lst[i].append(1)
    for j in range(1, 14):
        lst[i].append(lst[i-1][j]+lst[i][j-1])

for t in range(1, T+1):
    k = int(input()) # 1 ≤ k, n ≤ 14
    n = int(input())
    print(getSize(k, n))
