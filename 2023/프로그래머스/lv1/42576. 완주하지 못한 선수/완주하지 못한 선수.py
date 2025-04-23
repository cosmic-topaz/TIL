def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    while completion:
        p = participant.pop()
        c = completion.pop()
        if p != c:
            return p
    return participant.pop()