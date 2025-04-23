def factorize(n):
    # print('factorize', n)
    lst = []

    i = int(n**(1/2))
    while n > 1 and i > 1:
        if i > 1 and n%i == 0:
            # print(i, n//i)
            lst += factorize(i) 
            lst += factorize(n//i)
            return lst
        i -= 1
    if n == 1:
        return []
    return [n]

N = int(input()) # (1 ≤ N ≤ 10,000,000)
rst = sorted(factorize(N))
[print(p) for p in rst]