import sys

def f_count(n):
    if (n == 0):
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        c0, c1 = f_count(n-1)
        c0, c1 = c1, c0+c1
        return [c0, c1]

T = int(input())
for test_case in range(T):
    N = int(sys.stdin.readline().rstrip())
    c0, c1 = f_count(N)
    print(c0, c1)