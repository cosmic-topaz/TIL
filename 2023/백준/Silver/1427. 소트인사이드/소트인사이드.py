
N = int(input())
n = [0]*10
while N > 9:
    n[N%10] += 1
    N = N//10
n[N] += 1
[print(str(i)*n[i], end='') for i in reversed(range(10))]
print()