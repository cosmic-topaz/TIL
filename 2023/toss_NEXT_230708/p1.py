from collections import deque
def solution(s, N):
    answer = []

    n = str(N)

    for i in range(1, N+1):
        if str(i) not in s:
            return -1

    sub_strings = list(s.split('0'))
    deq = deque()
    deq.extend(sub_strings)

    i, j = len(sub_strings), N + 1

    while (deq and j <= 10):
        for _ in range(i):
            sub_string = deq.popleft()
            if len(sub_string) < N:
                continue
            flag = False
            for _ in range(1, N+1):
                if str(_) not in sub_string:
                    flag = True
            if flag:
                continue
            else:
                deq.extend(sub_string.split(str(j)))
        i, j = len(deq), j+1
    if deq:
        for _ in range(i):
            sub_string = deq.popleft()
            for _ in range(0, len(sub_string)-N+1):
                deq.append(sub_string[_:_+N])
    else:
        return -1
    
    print(deq)

    while (deq):
        sub_string = deq.popleft()
        flag = False
        for _ in range(1, N+1):
            if str(_) not in sub_string:
                flag = True
        if flag:
            continue
        else:
            answer.append(int(sub_string))

    return max(answer)


    
# s, N, result = "1451232125", 2, 21
# print(solution(s, N), result)
s, N, result = "313243123", 3, 321
print(solution(s, N), result)
s, N, result = "12412415", 4, -1
print(solution(s, N), result)

