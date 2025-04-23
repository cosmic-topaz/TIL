import sys
input = sys.stdin.readline

# Z

N, r, c = map(int, input().split())

x = 0
while N > 0:
    if r < 2**(N-1):
        if c < 2**(N-1):
            pass
        else:
            x += 2**(2*N-2)
            c -= 2**(N-1)
    else:
        if c < 2**(N-1):
            x += 2**(2*N-1)
            r -= 2**(N-1)
        else:
            x += 2**(2*N-1)+2**(2*N-2)
            r -= 2**(N-1)
            c -= 2**(N-1)
    N -= 1
print(x)