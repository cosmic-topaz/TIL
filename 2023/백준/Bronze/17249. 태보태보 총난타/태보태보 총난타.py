S = input()
def getPunch(Afterimage):
    return Afterimage.count('@')
L, R = map(getPunch, S.split('0'))

print(L, R)