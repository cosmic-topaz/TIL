import sys
C = int(input())
output = ''
for c in range(1, 1+C):
    input = sys.stdin.readline()
    scores = list(map(int, input.split()))
    avg = sum(scores)/scores[0] - 1
    n = 0
    for i in range(1, scores[0]+1):
        n += int(scores[i] > avg)
    ratio = round(n/scores[0]*100, 3)
    output += f'{ratio:.3f}%\n'
sys.stdout.write(output)

