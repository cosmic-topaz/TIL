score = int(input())

if score//10 >= 9:
    print('A')
elif score//10 == 8:
    print('B')
elif score//10 == 7:
    print('C')
elif score//10 == 6:
    print('D')
else:
    print('F')