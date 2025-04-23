N1 = int(input())
N2 = int(input())
N3 = N1*(N2%10)
N4 = N1*((N2//10)%10)
N5 = N1*((N2//100)%10)
N6 = N3 + N4*10 + N5*100

print(N3)
print(N4)
print(N5)
print(N6)

