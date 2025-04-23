def G(word):
    set_S = set(word)
    for s in set_S:
        # print(s, word.find(s), word.count(s))
        if len(set(word[word.find(s):word.count(s)+word.find(s):1]))>1:
            # print(word, 0)
            return 0
    # print(word, 1)
    return 1
N = int(input())
result = 0
for n in range(1, N+1):
    result += G(input())
print(result)