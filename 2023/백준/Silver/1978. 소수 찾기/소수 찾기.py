def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1

N = int(input()) # 1 <= N <= 100
numbers = list(map(int, input().split()))
result = 0
for n in numbers:
    result += isPrime(n)

print(result)