def solution(number, k):
    answer = ''
    i = 0
    while len(number[i:]) > k:
        for digit in '9876543210':
            x = number.find(digit, i, i + k + 1)
            if x < 0: continue 
            else: break
        answer += number[x]
        i, k = x + 1, k - x + i
    
    return answer