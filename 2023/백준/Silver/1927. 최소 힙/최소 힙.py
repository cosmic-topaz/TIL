# :: Testing
import sys

input = sys.stdin.readline
inputs = sys.stdin.readlines
from heapq import heappush, heappop
# from collections import deque
# import random
T = int(input())
min_heap = []
for _ in range(T):
    x = int(input())
    # # N, M = map(int, input().split())
    # # N = random.randint(0, 1000)
    # # K = random.randint(N, 1000)
    # rst = f(x)
    # print(rst)
    if x == 0:
        if len(min_heap) > 0:
            print(heappop(min_heap))
        else:
            print(0)
    else:
        heappush(min_heap, x)