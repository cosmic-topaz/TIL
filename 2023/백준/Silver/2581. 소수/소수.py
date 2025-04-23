M, N = int(input()), int(input())
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1
total = -1
mini = 0

for i in range(M, N+1):
    if isPrime(i):
        if total == -1:
            total = i 
            mini = i
        else:
            total += i

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
print(total)
if mini > 0:
    print(mini)