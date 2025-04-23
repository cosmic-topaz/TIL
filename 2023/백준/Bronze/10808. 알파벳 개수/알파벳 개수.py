import sys
input = sys.stdin.readline


from collections import Counter
S = input().strip()

def f(S):
    data = Counter('abcdefghijklmnopqrstuvwxyz'+S)
    return ' '.join(map(str, (v-1 for v in data.values())))

print(f(S))