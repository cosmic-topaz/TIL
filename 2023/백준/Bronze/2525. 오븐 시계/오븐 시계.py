def end_time(hh, mm, t):
    mm += t
    while mm > 59:
        hh += 1
        mm -= 60
    while hh > 23:
        hh -= 24
    return [hh, mm]

hh, mm = list(map(int, input().split()))
t = int(input())

hh, mm = end_time(hh, mm, t)
print(hh, mm)

