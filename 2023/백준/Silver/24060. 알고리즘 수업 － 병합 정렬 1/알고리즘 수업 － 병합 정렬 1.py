import sys
def ms_c(p, r, k, c):
    if p < r:
        q = (p+r)//2
        c = ms_c(p, q, k, c)
        c = ms_c(q+1, r, k, c)
        c += r-p+1
        if c >= k:
            print(sorted(A[p:r+1])[-1-c+k])
            exit()
    return c


N, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
ms_c(0,N-1,k,0)
# merge_sort(A, 0, N-1, 0)
print(-1)