import sys

T = int(sys.stdin.readline())
for test_case in range(T):
    N, m = map(int, sys.stdin.readline().split())
    que_ = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    i = 0
    que_[m]
    while True:
        x = que_[i]
        if i%N == m:
            if max(que_[i:]) == que_[m]:
                cnt += 1
                print(cnt)
                break
        if x == max(que_[i:]):
            que_.append(0)
            cnt += 1
        else:
            que_.append(x)
        i += 1