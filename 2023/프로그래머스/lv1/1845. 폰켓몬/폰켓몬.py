def solution(nums):
    num_choose = len(nums)//2
    num_kinds = len(set(nums))
    answer = min(num_choose, num_kinds)
    return answer