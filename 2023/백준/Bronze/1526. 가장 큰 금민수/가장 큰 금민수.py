import sys
input_ = sys.stdin.readline
N = input_().rstrip()
s = ['4', '7']
for i in range(len(N)-1):
    ss = []
    for x in s:
        ss.append(x+'4')
        ss.append(x+'7')
    s = ss
s = sorted(s)
for i in range(len(s)):
    if int(N) < int(s[i]):
        if i == 0:
            print('7'*(len(N)-1))
            exit()
        else:
            print(s[i-1])
            exit()
print(s[-1])
exit()