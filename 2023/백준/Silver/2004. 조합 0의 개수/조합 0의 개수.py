import sys
input = sys.stdin.readline
from math import log, floor

def zero_in_nCm(n, m):
    five, two = 0, 0
    pp_five = [5**i for i in range(1, floor(log(n, 5))+1)]
    pp_two = [2**i for i in range(1, floor(log(n, 2))+1)]
    for p in pp_five:
        five += n//p -m//p -(n-m)//p
    for p in pp_two:
        two += n//p -m//p -(n-m)//p     
    return min(five, two)
n, m = map(int, sys.stdin.readline().split())
answer = zero_in_nCm(n, m)
print(answer)