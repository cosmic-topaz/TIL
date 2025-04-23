N = int(input())
for i in range(min(N, 55), 0, -1):
    # print('M', N-i, i)
    if i == sum(int(x) for x in str(N-i)):
        print(N-i)
        exit()
print(0)