import sys
input_ = sys.stdin

N, M = map(int, input().split())
x = list(map(int, input_.readline().split()))


a = 0
b = max(x)
h = b//2

while True:
    h = (a+b)//2
    d = sum([max(x[i]-h, 0) for i in range(N)]) - M
    if d < 0:
        if b == h:
            h -= 1
            break
        else:
            b = h
    elif d > 0:
        if a == h:
            a = b
        else:
            a = h
    else:
        break
print(h)