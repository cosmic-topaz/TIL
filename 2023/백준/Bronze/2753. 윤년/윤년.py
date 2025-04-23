def leap_year(year):
    if year%4 != 0:
        return 0
    elif year%400 == 0:
        return 1
    elif year%100 == 0:
        return 0
    else:
        return 1

x = int(input())
print(leap_year(x))
    