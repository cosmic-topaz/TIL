import sys
size_a, size_b = map(int, input().split())
A = { x: 1 for x in map(int, sys.stdin.readline().split())}
B = { x: 1 for x in map(int, sys.stdin.readline().split()) if x in A}
size_i = len(B)
print(size_a+size_b-2*size_i)