names = ['원섭', '세희', '상근', '숭', '강수']
scores = []
for students in names:
    score = int(input())
    if score < 40:
        score = 40
    scores.append(score)

print(int(sum(scores)/len(scores)))