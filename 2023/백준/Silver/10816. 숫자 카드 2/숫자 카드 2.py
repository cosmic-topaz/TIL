# 10816 숫자 카드 2
from collections import Counter
N = int(input())
CARD= list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))
Y = []
count_card = Counter(CARD)
for x in X:
    Y.append(count_card.get(x, 0))
print(*Y)