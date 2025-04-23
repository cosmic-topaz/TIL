import sys

T = int(input())

for t in range(1, T+1):
    input = sys.stdin.readline()
    A, B = list(map(int, input.split()))
    sys.stdout.write(f'{A+B}\n')