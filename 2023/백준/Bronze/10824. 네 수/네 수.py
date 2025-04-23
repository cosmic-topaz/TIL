A, B, C, D = map(int, input().split())

# A와 B를 붙인 수 
# (1) B < 10 : 10*A+B
# (2) B//10 < 10 : 10*10*A+B
# (3) ...
# (4) B//10*(log10B//1) < 10 : 10*(log10B//1)*A+B
a, b, c, d = A, B, C, D
while b//10:
    b //= 10
    a *= 10
while d//10:
    d //= 10
    c *= 10
AB = 10*a + B
CD = 10*c + D
# 출력
# A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.
print(AB+CD)