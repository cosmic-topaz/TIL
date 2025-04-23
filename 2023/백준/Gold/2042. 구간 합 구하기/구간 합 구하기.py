import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0]*(N+1)
tree = [0]*(N+1)

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += i & -i

def prefix_sum(i):
    sum = 0
    while i > 0:
        sum += tree[i]
        i -= i & -i
    return sum

for _ in range(N):
    i = _+1
    arr[i] = int(input())
    # tree를 업데이트 한다
    update(i, arr[i])

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        # arr[b]를 c 로 바꾼다
        diff = c-arr[b]
        arr[b] = c
        update(b, diff)
    else: # a == 2:
        # b~c 까지의 합 구한다
        sum = prefix_sum(c) - prefix_sum(b-1)
        print(sum)