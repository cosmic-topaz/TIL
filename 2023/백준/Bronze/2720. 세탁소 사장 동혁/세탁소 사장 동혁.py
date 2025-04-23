T = int(input())
for test_case in range(T):
    C = int(input())
    Q, C = divmod(C, 25)
    D, C = divmod(C, 10)
    N, C = divmod(C, 5)
    P = C
    print(Q, D, N, P)