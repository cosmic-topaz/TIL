def getFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibonacci(n-1)+getFibonacci(n-2)

N = int(input())

print(getFibonacci(N))