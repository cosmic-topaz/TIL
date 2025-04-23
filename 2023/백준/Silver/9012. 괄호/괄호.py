T = int(input())
for test_case in range(T):
    S = input()
    x = []
    for char in S:
        if char == '(':
            x.append(char)
        else:
            if len(x) > 0:
                x.pop()
            else:
                x.append('NO')
                break
    if len(x) > 0 :
        print('NO')
    else:
        print('YES')