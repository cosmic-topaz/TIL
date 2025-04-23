from collections import Counter
N = 10
x = [int(input()) for i in range(N)]
a = sum(x)//N
b = Counter(x).most_common()[0][0]
print(a)
print(b)