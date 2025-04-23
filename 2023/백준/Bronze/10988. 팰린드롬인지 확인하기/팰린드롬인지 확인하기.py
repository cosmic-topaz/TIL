S = input()
def isPalindrome(S):
    result = 1
    for i in range(0, len(S)//2):
        result *= (S[i]==S[(i+1)*-1])
    return result

print(isPalindrome(S))