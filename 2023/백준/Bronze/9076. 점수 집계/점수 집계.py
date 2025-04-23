import sys
input_ = sys.stdin

def f():
    N = list(map(int, input_.readline().split()))

    N = sorted(N)[1:-1]

    if N[-1]-N[0] >= 4:
        print('KIN')
    else:
        print(sum(N))

T = int(input_.readline())

for test_case in range(T):

    f()