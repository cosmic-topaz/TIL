import sys
n = int(input())

a = 0
s = [0]*n
output = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if s[x-1] == -1:
        print('NO')
        exit()
    else:
        while s[x-1] == 0:
            s[a] = 1
            b = a
            output.append('+')
            a += 1
        while s[x-1] == 1:
            while b >= x-1:
                if s[b] == 1:
                    output.append('-')
                    s[b] = -1
                    b -= 1
                else:
                    b -= 1
            
        


print(*output, sep='\n')