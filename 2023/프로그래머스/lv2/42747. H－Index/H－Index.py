def solution(citations):
    n = len(citations)
    citations.sort() # [0, 1, 3, 5, 6]
    h = n
    while h > 0 and citations[-h] < h:
        h -= 1
    return h