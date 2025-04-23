def solution(array, commands):
    answer = []
    array = [0]+array+[999]
    for cmd in commands:
        i, j, k = cmd
        answer.append(sorted(array[i:j+1], reverse=True)[-k])
    return answer
