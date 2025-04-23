N, k = map(int, input().split())
x = list(map(int, input().split()))
k_th = sorted(x)[N-k]
print(k_th)