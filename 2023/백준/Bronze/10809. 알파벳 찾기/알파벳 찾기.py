az = [-1]*(ord('z')-ord('a')+1)
input_ = input()
for i in range(0, len(input_)):
    if az[ord(input_[i])-ord('a')] < 0:
        az[ord(input_[i])-ord('a')] = i

[print(x, end=' ') for x in az]
print()