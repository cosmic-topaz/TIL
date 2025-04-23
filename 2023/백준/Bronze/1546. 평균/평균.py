N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
avg = sum(scores)/M*100/N
print(avg)