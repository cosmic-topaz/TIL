import sys
N = int(input()) # (1 ≤ N ≤ 10,000,000)
input_ = sys.stdin
count_list = [0]*10000
for _ in range(N):
    x = int(input_.readline().rstrip())
    count_list[x-1] += 1

for x in range(10000):
    for _ in range(count_list[x]):
        print(x+1)
