import sys
input = sys.stdin.readline
N = int(input())
P = [0]+list(map(int, input().split()))
Q = [0]*(N+1)

for i in range(1, N+1):
    if i > 1:
        if P[i] > P[i-1]:
            Q[i] = P[i] - P[i-1] + Q[i-1]
            Q[i-1] = 0
    
print(max(Q))