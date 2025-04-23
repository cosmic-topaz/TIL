def solution(relationships, target, limit):
    answer = 0

    friend_map = [[False]*101 for _ in range(101)]
    for person_A, person_B in relationships:
        friend_map[person_A][person_B] = True
        friend_map[person_B][person_A] = True

    # 친구의 수 구하기 
    friend_set = set(person for person, is_friend in enumerate(friend_map[target]) if is_friend) # 원래 알 던 친구
    reward = len(friend_set)*5

    friend_set.add(target)
    new_friends = 0
    for _ in range(1, limit):
        new_friend_set = set()
        for friend in friend_set:
            new_friend_set.update(set(person for person, is_friend in enumerate(friend_map[friend]) if is_friend and person not in friend_set ))
        new_friends += len(new_friend_set)
        reward += len(new_friend_set)*10
        friend_set.update(new_friend_set)

        
    friend_set.remove(target)

    return new_friends + reward

# 사람 : 100명
# 관계 : 최대 4000개 


relationships = [[1,2], [2,3], [2,6], [3,4], [4,5]]
target = 2
limit = 3
result = 37
print(solution(relationships, target, limit), result)


# 프로그래밍 2번 문제 정정 공지 드립니다.

# [수정 전]
# 출력
# 보상을 받을 사람이 받을 보상 금액을 출력합니다.

# [수정 후]
# 출력
# 특정 사람 ( target ) 이 새롭게 알게 된 친구 수와 받을 보상 금액의 합을 출력합니다.