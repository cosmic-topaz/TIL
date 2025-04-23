import heapq 
def solution(operations):
    heap = []
    for s in operations:
        cmd, x = s.split()
        eval(f'{cmd}(heap, {x})')
    
    if heap:
        answer = [heap[-1], heap[0]]
    else:
        answer = [0, 0]
    return answer

def I(heap, item):
    if heap and heap[-1] > item:
        maxitem = heap.pop()
        heapq.heappush(heap, item)
        heap.append(maxitem)
    else:
        heap.append(item)
        
def D(heap, x):
    if heap:
        if x > 0:
            heap.pop()
            if heap:
                maxitem = max(heap)
                lastitem = heap.pop()
                if lastitem < maxitem:
                    pos = len(heap)-heap[::-1].index(maxitem)-1
                    while pos > 0:
                        parentpos = (pos-1) >> 1
                        parent = heap[parentpos]
                        if lastitem < parent:
                            heap[pos] = parent
                            pos = parentpos
                            continue
                        break
                    heap[pos] = lastitem
                heap.append(maxitem)
        else:
            heapq.heappop(heap)            
            
input_data = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]     
print(solution(input_data))