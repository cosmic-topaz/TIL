def f(N, M):
    never_heard = set(input().strip() for _ in range(N))
    never_met = set(input().strip() for _ in range(M))
    return sorted(never_heard & never_met)


# :: Testing
import sys
input = sys.stdin.readline
inputs = sys.stdin.readlines

T = 1

for _ in range(T):
    N, M = map(int, input().split())
    rst = f(N, M)
    print(len(rst))
    print(*rst, sep='\n')