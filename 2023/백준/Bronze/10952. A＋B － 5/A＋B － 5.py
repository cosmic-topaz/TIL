import sys

input = sys.stdin.readline()
A, B = list(map(int, input.split()))
output = ''

while (A != 0)+(B != 0):
    output += f'{A+B} \n'
    input = sys.stdin.readline()
    A, B = list(map(int, input.split()))

sys.stdout.write(output)
    