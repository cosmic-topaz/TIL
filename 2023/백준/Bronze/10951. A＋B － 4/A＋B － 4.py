import sys

output = ''
input = sys.stdin.readline()
while input:
    A, B = list(map(int, input.split()))
    output += f'{A+B}\n'
    input = sys.stdin.readline()
sys.stdout.write(output)
        
    