N = int(input())

if N in range(1, 100):
    print(N)
else:
    count = 99
    for n in range(100, N+1):
        x1, x2, x3 = n//100, n//10%10, n%10
        if x1 - 2*x2 + x3 == 0:
            count += 1
    print(count)