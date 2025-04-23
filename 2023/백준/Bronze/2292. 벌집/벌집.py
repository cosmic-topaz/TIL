N = int(input())
n = 1
an = 1
while an < N:
    n += 1
    an = 3*n*(n-1)+1
print(n)
