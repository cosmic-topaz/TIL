import sys
input_ = sys.stdin

S = ['고무오리 디버깅 시작', '문제', '고무오리', '고무오리 디버깅 끝']
X = ['고무오리야 사랑해', '힝구']
p = []

while True:
    s = input_.readline().rstrip()
    x = S.index(s)
    if x == 0:
        p = []
    elif x == 1:
        p.append(x)
    elif x == 2:
        if len(p):
            p.pop()
        else:
            p.append(x)
            p.append(x)
    elif x == 3:
        if len(p):
            print(X[1])
        else:
            print(X[0])
        exit()
    else:
        exit()
