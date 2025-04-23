T = int(input()) # 1 <= T <= 1000
for test_case in range(1, T+1):
    R, S = input().split()
    R = int(R)
    [print(s*R, end='') for s in S]
    print()