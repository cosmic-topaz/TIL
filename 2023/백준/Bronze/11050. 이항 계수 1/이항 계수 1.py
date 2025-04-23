# 11050 이항 계수 1

N, K = map(int, input().split())

def C(N, K):
    rst = 1
    for i in range(K):
        rst *= (N-i)
    for i in range(1, K+1):
        rst //= i
    return rst

print(C(N, K))
