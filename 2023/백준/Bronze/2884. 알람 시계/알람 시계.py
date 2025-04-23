def advance45(H, M):
    M -= 45
    while M < 0:
        M += 60
        H -= 1
    while H < 0:
        H += 24
    return [H, M]

H, M = list(map(int, input().split()))
H, M = advance45(H,M)
print(H, M)
