import sys
N = int(input()) # (1 ≤ N ≤ 1,000,000)
input_ = sys.stdin
x = (int(input_.readline().rstrip()) for _ in range(N)) # (-1,000,000 ≤ x ≤ 1,000,000)

x = sorted(list(x))

for _ in x:
    print(_)