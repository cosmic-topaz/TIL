# 10845 큐

class Queue():
    _queue = []

    def __init__(self):
        super().__init__()

    def push(self, X):
        self._queue.append(X)

    def pop(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue[0])
            self._queue = self._queue[1:]

    def size(self):
        print(len(self._queue))

    def empty(self):
        if len(self._queue) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue[0])
    
    def back(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue[-1])    

import sys
N = int(input())

my_queue = Queue()

for _ in range(N):
    input_ = sys.stdin.readline().rstrip()
    if input_[:4] == 'push':
        my_queue.push(int(input_[5:]))
    if input_[:3] == 'pop':
        my_queue.pop()
    if input_[:4] == 'size':
        my_queue.size()
    if input_[:5] == 'empty':
        my_queue.empty()
    if input_[:5] == 'front':
        my_queue.front()
    if input_[:4] == 'back':
        my_queue.back()
        
