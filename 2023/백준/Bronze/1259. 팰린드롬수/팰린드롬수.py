# 1259 팰린드롬수
from math import log
while True:
    x = int(input())
    if x == 0:
        exit()  
    # print(x, _)
    if x == sum([((x//(10**i))%10)*(10**int(log(x, 10)-i)) for i in range(int(log(x, 10))+1)[::-1]]):
        print('yes')
    else:
        print('no')