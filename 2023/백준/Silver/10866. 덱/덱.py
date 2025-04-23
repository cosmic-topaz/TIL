
class Deque():
    _deque = []

    def __init__(self):
        super().__init__()

    def push_front(self, X):
        _front = [X]
        _front.extend(self._deque)
        self._deque = _front

    def push_back(self, X):
        self._deque.append(X)

    def pop_front(self):
        if len(self._deque) == 0:
            print(-1)
        else:
            print(self._deque[0])
            self._deque = self._deque[1:]
    
    def pop_back(self):
        if len(self._deque) == 0:
            print(-1)
        else:
            print(self._deque.pop())

    def size(self):
        print(len(self._deque))

    def empty(self):
        if len(self._deque) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self._deque) == 0:
            print(-1)
        else:
            print(self._deque[0])
    
    def back(self):
        if len(self._deque) == 0:
            print(-1)
        else:
            print(self._deque[-1])   


import sys
N = int(input())

my_deque = Deque()

for _ in range(N):
    input_ = sys.stdin.readline().rstrip()
    if input_[:4] == 'push':
        if input_[5] == 'f':
            my_deque.push_front(int(input_[11:]))
        if input_[5] == 'b':
            my_deque.push_back(int(input_[10:]))
    if input_[:3] == 'pop':
        if input_[4] == 'f':
            my_deque.pop_front()
        if input_[4] == 'b':
            my_deque.pop_back()
    if input_[:4] == 'size':
        my_deque.size()
    if input_[:5] == 'empty':
        my_deque.empty()
    if input_[:5] == 'front':
        my_deque.front()
    if input_[:4] == 'back':
        my_deque.back()
        
