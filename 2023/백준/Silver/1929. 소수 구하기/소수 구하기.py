# 1 < n < 10
prime1000 = [2, 3, 5, 7]
# 10 < n < 100
n = 11
while n < 100:
    for x in [2, 3, 5, 7]:
        if n%x == 0:
            n *= (-1)
            break
    if n < 0:
        n *= -1
    else:
        prime1000.append(n)
    n += 2
# 100 < n < 1000
while n < 1000:
    for x in range(3, 33, 2):
        if n%x == 0:
            n *= (-1)
            break
    if n < 0:
        n *= -1
    else:
        prime1000.append(n)
    n += 2

def isPrime(n):
    if n < 1000:
        if n in prime1000:
            return 1
        else:
            return 0
    # 1000 < n
    root_n = n**(1/2)//1
    for x in prime1000:
        if x > root_n:
            return 1
        if n%x == 0:
            return 0
    return 1

M, N = map(int, input().split())

for x in range(M, N+1):
    if isPrime(x):
         print(x)