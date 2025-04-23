# 영화감독 숌
n = 3
title = set()
title.add(666)

while len(title) < 10000:
    new_title = set()
    for x in title:
        for i in range(10):
            new_title.add(x*10+i)
            new_title.add(i*(10**n)+x)
    n += 1
    title = sorted(new_title)

N = int(input())
print(title[N-1])