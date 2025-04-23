def solution(sizes):
    answer = 0
    max_width = max([max(w, h) for [w, h] in sizes])
    max_height = max([min(w,h) for [w, h] in sizes])
    answer = max_width * max_height
    return answer


# 제한사항
# sizes의 길이는 1 이상 10,000 이하입니다.
# sizes의 원소는 [w, h] 형식입니다.
# w는 명함의 가로 길이를 나타냅니다.
# h는 명함의 세로 길이를 나타냅니다.
# w와 h는 1 이상 1,000 이하인 자연수입니다.


# 가장 긴 길이를 구한다.

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]] # 4000
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]] # 120
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] # 133