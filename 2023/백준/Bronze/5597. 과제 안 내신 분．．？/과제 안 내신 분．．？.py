student = set()
for i in range(1, 31):
    student.add(i)
for j in range(0,28):
    student.discard(int(input()))

x = student.pop()
y = student.pop()

print(min(x,y))
print(max(x,y))


    