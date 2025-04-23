import sys

N = int(input())
input = sys.stdin.readline()
A = list(map(int, input.split()))
print(min(A), max(A))