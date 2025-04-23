pieceWood = list(map(int, input().split()))
while pieceWood != [1,2,3,4,5]:
    i = 0 
    while i < 4:
        if pieceWood[i] > pieceWood[i+1]:
            pieceWood.append(pieceWood[i+1])
            pieceWood.append(pieceWood[i])
            pieceWood = pieceWood[:i] + pieceWood[5:7] + pieceWood[i+2:5]
            print(*pieceWood)
        i += 1
