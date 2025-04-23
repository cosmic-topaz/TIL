T = int(input())
output = ''
for t in range(1, T+1):
    ox = input().split('X')
    point = 0
    for o in ox:
        point += sum(range(1,len(o)+1))
    output += f'{point}\n'
print(output)