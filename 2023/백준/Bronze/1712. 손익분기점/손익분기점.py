def BEP(FC, VC, P):
    if VC < P:
        return FC//(P-VC)+1
    else:
        return -1

A, B, C = list(map(int, input().split()))
print(BEP(A, B, C))