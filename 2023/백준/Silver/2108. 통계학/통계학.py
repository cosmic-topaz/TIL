import sys
N = int(input()) # (1 ≤ N ≤ 500,000)
input_ = sys.stdin
count_list = [0]*8001
for _ in range(N):
    # x = list(map(int, input().split())) 
    x = int(input_.readline().rstrip()) # (-4,000<=x<=4,000)
    count_list[x+4000] += 1

mean = round(sum([x*(count_list[4000+x]-count_list[4000-x]) for x in range(1, 4001)])/N)
# median = sum(sorted(x)[(N-1)//2:(N+2)//2])//2
x = -4000
cum_frq = count_list[4000+x]
while cum_frq < (N+1)//2:
    x += 1
    cum_frq += count_list[4000+x]
median = x
mode = count_list.index(max(count_list))
if count_list.count(max(count_list)) > 1:
    mode = count_list.index(max(count_list), mode+1)
mode -= 4000

x = [x-4000 for x in range(8001) if count_list[x] > 0 ]
x_range=(max(x)-min(x))
print(mean)
print(median)
print(mode)
print(x_range)