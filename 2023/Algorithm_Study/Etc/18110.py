# https://www.acmicpc.net/problem/18110

# 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.
# 제외되는 사람의 수는 위, 아래에서 각각 반올림한다.
# 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.

import sys
# 첫 번째 줄에 난이도 의견의 개수 n이 주어진다. (0 ≤ n ≤ 3 × 10^5)
n = int(input())

# 이후 두 번째 줄부터 1 + n번째 줄까지 사용자들이 제출한 난이도 의견 n개가 한 줄에 하나씩 주어진다.
# 모든 난이도 의견은 1 이상 30 이하이다.
level = 0

if n == 0:
    print(level)
    exit()


def round(a):
    a *= 10
    c = (a) % 10
    if c < 5:
        c = 0
    else:
        c = 1
    return int(a//10+c)


margin = round(n*0.15)
# print("margin: ", margin)
rate = [0]*30

margin_top = margin_bottom = margin
population = n - margin*2

for i in range(0, n):
    input = int(sys.stdin.readline())
    rate[input-1] += 1

min_rate = 1
max_rate = 30

while margin_top:
    margin_top -= rate[max_rate-1]
    if margin_top >= 0:
        rate[max_rate-1] = 0
        max_rate -= 1
    else:
        rate[max_rate-1] = 0 - margin_top
        margin_top = 0

while margin_bottom:
    margin_bottom -= rate[min_rate-1]
    if margin_bottom >= 0:
        rate[min_rate-1] = 0
        min_rate += 1
    else:
        rate[min_rate-1] = 0 - margin_bottom
        margin_bottom = 0

for i in range(min_rate, max_rate+1):
    if rate[i-1]:
        level += rate[i-1]*i

level = round(level/population)

print(level)
