#  (0 < A,B < 10^10000)
A, B = input().split()

def printAddition(A, B):
    result = '0'
    if len(A) > len(B):
        B = '0'*(len(A)-len(B)) + B
    else:
        A = '0'*(len(B)-len(A)) + A
    for a, b in zip(reversed(A), reversed(B)):
        c = int(a)+int(b)+int(result[-1])
        result = result[:-1] + str(c%10) + str(c//10)
    for digit in reversed(result.rstrip('0')):
        print(digit, end='')
    print()

printAddition(A, B)
