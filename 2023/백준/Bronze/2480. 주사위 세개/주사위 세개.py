def prize(x, y, z):
    if x == z:
        return 10000+x*1000
    elif y == z:
        return 1000+y*100
    elif x == y:
        return 1000+y*100
    else:
        return z*100

[x, y, z] = sorted(list(map(int, input().split())))
print(prize(x,y,z))