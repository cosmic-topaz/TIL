from heapq import heappush, heappop
def solution(jobs):
    jobs.sort()
    answer = 0
    heap = []
    time = 0
    for job in jobs:
        while job[0] > time:
            if heap:
                next_job = heappop(heap)
                time += next_job[0]
                answer += time - next_job[1]
            else:
                time = job[0]
        heappush(heap, (job[1], job[0]))
        
    while heap:
        next_job = heappop(heap)
        time += next_job[0]
        answer += time - next_job[1]

    return answer//len(jobs)