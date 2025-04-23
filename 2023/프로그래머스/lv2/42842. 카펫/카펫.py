def solution(brown, yellow):
    answer = []
    for width in range(brown//2, 2, -1):
        height = brown//2 - width + 2
        if yellow == (height-2)*(width-2):
            return [width, height]