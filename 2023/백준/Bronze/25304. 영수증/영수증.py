X = int(input())
N = int(input())
for n in range(1, N+1):
    a, b = list(map(int, input().split()))
    X -= a*b

answer = 'No'
if X == 0:
    answer = 'Yes'

print(answer)