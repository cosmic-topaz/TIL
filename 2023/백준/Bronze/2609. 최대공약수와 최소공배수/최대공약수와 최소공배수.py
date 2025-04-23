# 2609 최대공약수와 최소공배수


def prime_N(N):
    N = int(N//1)
    if N > 10:
        rslt = prime_N(N**(1/2))
        for x in range(int((N**(1/2))//1), N+1):
            i = True
            for p in rslt:
                if x%p == 0:
                    i = False
                    break
            if i:
                rslt.append(x)
        N = int((N**(1/2))//1)
    else:
        rslt = [p for p in [2, 3, 5, 7] if p < N+1]
    return rslt

def factorize(N):
    N = int(N//1)
    rst = {}
    if N == 1:
        return rst
    P = prime_N(N**(1/2))
    # print(N, P)
    for p in P:
        if N%p == 0:
            rst = factorize(N//p)
            rst[p] = rst.get(p, 0) + 1
            return rst
    rst[N] = 1
    return rst

A, B = map(int, input().split())

dict_A = factorize(A)
dict_B = factorize(B)
# print(dict_A, dict_B)
dict_X = {}
dict_Y = {}
for p in dict_A.keys():
    dict_X[p] = max(dict_B.get(p, 0), dict_A.get(p, 0))
    dict_Y[p] = min(dict_B.get(p, 0), dict_A.get(p, 0))
for p in dict_B.keys():
    dict_X[p] = max(dict_B.get(p, 0), dict_A.get(p, 0))
    dict_Y[p] = min(dict_B.get(p, 0), dict_A.get(p, 0))
x, y = 1, 1
for p in dict_X.keys():
    x *= p**dict_X[p]
for p in dict_Y.keys():
    y *= p**dict_Y[p]

print(y)
print(x)