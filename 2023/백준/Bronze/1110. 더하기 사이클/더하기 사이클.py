N = int(input())
M = (N%10)*10 + (N//10+N%10)%10
count = 1

while M != N:
    M = (M%10)*10 + (M//10+M%10)%10
    count += 1

print(count)
    