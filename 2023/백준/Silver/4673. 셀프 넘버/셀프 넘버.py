def d(n):
    return sum([int(x) for x in str(n)])+n

self_numbers = [0]*10000

for x in range(10001):
    dx = d(x)
    if dx < 10001:
        self_numbers[dx-1] = 1

[print(n) for n in range(1, 10001) if not self_numbers[n-1]]