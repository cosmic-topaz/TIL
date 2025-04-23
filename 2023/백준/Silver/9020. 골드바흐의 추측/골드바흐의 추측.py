def genPrime100():
    p = [2, 3, 5, 7]
    n = 11
    while n < 100:
        for x in [2, 3, 5, 7]:
            if n%x == 0:
                n *= (-1)
                break
            
        if n < 0:
            n *= -1
        else:
            p.append(n)
        n += 2
    return p

def isPrime(N):
    if N < 100:
        if N in prime100:
            return 1
        else:
            return 0
    # 100 < n
    else:
        root_N = N**(1/2)//1
        for x in prime100:
            if x > root_N:
                return 1
            if N%x == 0:
                return 0
        return 1

def goldbach_partition(n):
    p = n//2
    q = n - p
    while q < n:
        if isPrime(p) and isPrime(q):
            return (p, q)
        p -= 1
        q += 1
    return (-1, -1)

T = int(input())
prime100 = genPrime100()
for test_case in range(T):
    n = int(input())
    print(*goldbach_partition(n))