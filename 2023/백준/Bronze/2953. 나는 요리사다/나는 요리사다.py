M, N = 4, 5
score = [sum(list(map(int, input().split()))) for j in range(N)]
print( score.index(max(score))+1, max(score))