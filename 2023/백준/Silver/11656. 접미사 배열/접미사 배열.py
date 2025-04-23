S = input().rstrip()
postfix = sorted([S[-i:] for i in range(1, len(S)+1)])
print(*postfix, sep='\n')