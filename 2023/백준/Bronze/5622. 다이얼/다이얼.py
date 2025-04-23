S = input()
T = 0
for s in S:
    if ord(s) < ord('S'):
        T += ((ord(s)+1)//3-19)
    elif ord(s) < ord('Z'):
        T += ord(s)//3 -19
    else:
        T += (ord(s)-1)//3 -19
print(T)