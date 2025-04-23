N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0
for x in numbers:
    count += int(x==v)
print(count)