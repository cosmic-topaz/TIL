S = input().lower()
A = [0]*(ord('z')-ord('a')+1)
set_S = list(set(S))
for s in set_S:
    A[ord(s)-ord('a')] += S.count(s)

x = A.index(max(A))
if A.count(max(A)) > 1:
    x = ord('?')-ord('A')

print(chr(x+ord('A')))
