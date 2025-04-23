def what_quad(x,y):
    if x*y > 0 and x > 0:
        return 1
    elif x*y > 0:
        return 3
    elif x > 0:
        return 4
    else:
        return 2

x = int(input())
y = int(input())

print(what_quad(x,y))
