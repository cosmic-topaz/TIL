def getFilp_words(S):
    result = ''
    words = S.split()
    for w in words:
        for c in reversed(w):
            result += c
        result += ' '
    return result.rstrip()

T = int(input())
for test_case in range(1, T+1):

    S = input()
    #print(test_case, S)
    print(getFilp_words(S))