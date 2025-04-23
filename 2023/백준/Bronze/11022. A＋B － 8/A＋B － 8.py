import sys

T = int(input())
output = ''
for t in range(1, T+1):
    input = sys.stdin.readline()
    A, B = list(map(int, input.split()))
    output += f'Case #{t}: {A} + {B} = {A+B}\n'
sys.stdout.write(output)