x = int(input())
i = 1
a = x
b = i
while i < 9:
    x = int(input())
    i += 1
    if x > a:
        a = x
        b = i

print(a)
print(b)
    