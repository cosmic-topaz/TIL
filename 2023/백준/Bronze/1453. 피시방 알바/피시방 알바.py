from collections import Counter
N = int(input())
x = map(int, input().split())
x_counter = dict(Counter(x))
n = [x_counter[x]-1 for x in x_counter.keys()]
print(sum(n))