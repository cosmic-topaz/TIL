N, M = map(int, input().split())
card = list(map(int, input().split()))
# N!/(N-3)!
card = sorted(card, reverse=True)
# print(card)
result = sum(card[-3:])

for i in range(N-2):
    if card[i] > M-sum(card[-2:]):
        continue
    for j in range(i+1, N-1):
        if card[i]+card[j] > M-card[-1]:
            continue
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] > M:
                continue
            else:
                result = max(result, card[i]+card[j]+card[k])
                break
print(result)