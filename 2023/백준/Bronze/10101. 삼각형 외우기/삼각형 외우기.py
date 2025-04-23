a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print('Error')
else:
    if max(a,b,c)== 60:
        print('Equilateral')
    else:
        if 180 - min(a,b,c) - max(a,b,c) in (min(a, b, c), max(a, b, c)):
            print('Isosceles')
        else:
            print('Scalene')