S = input()
i = 0
while len(S) - i > 10:
    print(S[i:i+10])
    i += 10
print(S[i:])