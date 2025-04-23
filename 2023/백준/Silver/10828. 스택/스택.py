class Stack():
    _stack = []

    def __init__(self):
        super().__init__()

    def push(self, X):
        self._stack.append(X)

    def pop(self):
        if len(self._stack) == 0:
            print(-1)
        else:
            print(self._stack.pop())

    def size(self):
        print(len(self._stack))

    def empty(self):
        if len(self._stack) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self._stack) == 0:
            print(-1)
        else:
            print(self._stack[-1])

import sys
N = int(input())
my_stack = Stack()

for _ in range(N):
    input_ = sys.stdin.readline().rstrip()
    if input_[:4] == 'push':
        my_stack.push(int(input_[5:]))
    if input_[:3] == 'pop':
        my_stack.pop()
    if input_[:4] == 'size':
        my_stack.size()
    if input_[:5] == 'empty':
        my_stack.empty()
    if input_[:3] == 'top':
        my_stack.top()