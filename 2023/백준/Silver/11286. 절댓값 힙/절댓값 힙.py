import sys


def f(x):
    if x == 0:
        # print('pop')
        # pop
        if len(n) == 1:
            print(0)
            return
        n[1], n[-1] = n[-1], n[1]
        print(n.pop())
        p = 1
        while True:
            if 2*p+1 < len(n):
                if abs(n[2*p+1]) > abs(n[2*p]):
                    c = 2*p
                elif abs(n[2*p+1]) == abs(n[2*p]):
                    if n[2*p+1] >= n[2*p]:
                        c = 2*p
                    else:
                        c = 2*p+1
                else:
                    c = 2*p+1
            elif 2*p < len(n):
                c = 2*p
            else:
                break
            if abs(n[p]) > abs(n[c]):
                n[p], n[c] = n[c], n[p]
                p = c
            elif abs(n[p]) == abs(n[c]):
                if n[p] > n[c]:
                    n[p], n[c] = n[c], n[p]
                    p = c
                else:
                    break
            else:
                break
    else:
        # print('push', x)
        # push x
        n.append(x)
        c = len(n)-1
        # sort
        while True:
            if c > 1:
                p = c//2
            else:
                break
            if abs(n[p]) > abs(n[c]):
                n[p], n[c] = n[c], n[p]
                c = p
            elif abs(n[p]) == abs(n[c]):
                if n[p] > n[c]:
                    n[p], n[c] = n[c], n[p]
                    c = p
                else:
                    break
            else:
                break


N = int(input())
n = [0]

for i in range(N):
    f(int(sys.stdin.readline().rstrip()))