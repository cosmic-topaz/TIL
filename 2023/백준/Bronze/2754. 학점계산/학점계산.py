grade = input()
x = len(grade)//2
y = (70-ord(grade[0]))
z = ((ord(grade[-1])+1)%4*-3-7)/10
point  = abs(x*(y+z))
print(point)