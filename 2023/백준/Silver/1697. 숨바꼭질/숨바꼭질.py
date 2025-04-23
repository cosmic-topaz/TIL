def f(N, K):
    if N >= K :
        return abs(N-K)
    visited = set()
    set_ = [set(), ]
    i = 0
    set_[i].add(K)
    while True:
        if N in set_[i]:
            return i
        else:
            set_.append(set())
            for x in set_[i]-visited:
                if x%2 == 0:
                    set_[i+1].add(x+1)
                    set_[i+1].add(x-1)
                    set_[i+1].add(x//2)
                else:
                    set_[i+1].add(x+1)
                    set_[i+1].add(x-1)
                visited.add(x)
            i += 1
# :: Testing
import sys
input = sys.stdin.readline
inputs = sys.stdin.readlines
T = 1

for _ in range(T):
    N, K = map(int, input().split())
    rst = f(N, K)
    print(rst)