from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville) #O(len(scoville)))
    while scoville: #O(len(scoville)) : worst_case
        s1 = heappop(scoville)
        if s1 >= K:
            return answer
        if scoville:
            s2 = heappop(scoville)
            heappush(scoville, s1+2*s2)
            answer += 1
        else:
            return -1