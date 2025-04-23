import sys
f = sys.stdin

def solution(s):
    rst = [0] * 4
    for c, uc in zip(s, s.upper()):
        if c == ' ':
            rst[3] += 1
        elif c in '0123456789':
                rst[2] += 1
        elif c == uc:
             rst[1] += 1
        else: # c == lc
             rst[0] += 1
    return ' '.join(map(str, rst))
         
answer = []
for line in f:
    s = line.rstrip('\n')
    if s:
        answer.append(solution(s))
    else:
        break
print(*answer, sep='\n')