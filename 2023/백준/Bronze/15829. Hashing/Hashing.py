L = int(input())
r = 31
M = 1234567891

def H(s):
    return sum((ord(s[i])-ord('a')+1)*(r**i) for i in range(L))%M

print(H(input().rstrip()))