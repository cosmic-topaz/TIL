def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (f(x),len(x)),  reverse = True)
    answer = ''.join(numbers)
    if int(answer):
        return answer
    else:
        return '0'

def f(x):
    if len(x) < 4:
        return (4*x)[:4]
    else:
        return x