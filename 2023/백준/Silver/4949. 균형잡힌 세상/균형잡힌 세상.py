import sys


def f(s):
    opener = ['(', '[']
    closer = [')', ']']
    stack_ = [-1]
    for char in input_:
        if char in opener:
            stack_.append(opener.index(char))
        if char in closer:
            if stack_.pop() == closer.index(char):
                pass
            else:
                return 'no'
    if stack_[-1] == -1:
        return 'yes'
    else:
        return 'no'

input_ = sys.stdin.readline().rstrip()
while input_ != '.':
    print(f(input_))
    input_ = sys.stdin.readline().rstrip()