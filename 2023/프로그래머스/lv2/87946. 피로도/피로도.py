# 87946_피로도시스템

# 제한사항
# k는 1 이상 5,000 이하인 자연수입니다.
# dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
# dungeons의 가로(열) 길이는 2 입니다.
# dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
# "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
# "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
# 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.

from itertools import permutations
# k: 유저의 현재 피로도
# dungeons: 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열
# return: 유저가 탐험할수 있는 최대 던전 수
def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    plans = permutations(range(n), n) # 8!
    for plan in plans:
        remaining_fatigue, cnt = k, 0
        for i in plan:
            min_required_fatigue, consumed_fatigue = dungeons[i]
            if remaining_fatigue >= min_required_fatigue:
                remaining_fatigue -= consumed_fatigue
                cnt += 1
        answer = max(answer, cnt)
    return answer