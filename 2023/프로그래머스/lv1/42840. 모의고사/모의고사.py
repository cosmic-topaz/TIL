def solution(answers):
    answer = []
    scores = []
    estimates = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    n = len(answers)
    for sequence in estimates:
        d, m = divmod(n, len(sequence))
        score = sum(int(answer == guess) for answer, guess in zip(answers, sequence*(d+1)))
        scores.append(score)
    
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)
    return answer

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

answers = [1,2,3,4,5] #	[1]
answers = [1,3,2,4,2] #	[1,2,3]