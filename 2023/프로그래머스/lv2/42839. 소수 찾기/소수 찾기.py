from itertools import permutations
def solution(numbers):
    arr = set()
    for i in range(1, len(numbers)+1):
        arr.update(isPrime(''.join(x)) for x in permutations(numbers, i))
    arr = arr.difference([-1])
    return len(arr)

def isPrime(x): # O(x^(1/2))
    x = int(x)
    if x in [0, 1, 4, 6, 8, 9]:
        return -1
    if x in [2, 3, 5, 7]:
        return x
    for i in range(2, int(x**(1/2)+1)):
        if not x%i:
            return -1
    return x