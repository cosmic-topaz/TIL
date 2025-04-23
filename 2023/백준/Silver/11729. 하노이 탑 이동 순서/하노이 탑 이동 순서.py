def hanoi(N, a, c, b):
    if N == 1:
        output = [1, str(f'\n{a} {c}')]
    else:
        output = [1, str(f'\n{a} {c}')]
        output = [ y + x for x, y in zip(output, hanoi(N-1, a, b, c))]
        output = [ x + y for x, y in zip(output, hanoi(N-1, b, c, a))]
    return output


N = int(input())
[print(x, end='') for x in hanoi(N, 1, 3, 2)]
print()