def card2(n):
    if n < 3:
        return n
    else:
        if n%2:
            return 2*((card2(n//2))%(n//2)+1)
        else:
            return 2*card2(n//2)
N = int(input())
print(card2(N))