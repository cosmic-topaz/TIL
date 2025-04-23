while True:
    numbers = list(map(int, input().split()))
    d = (sum([x*x for x in numbers])/2)**(1/2)
    if d == 0:
        exit()
    elif (sum([x*x for x in numbers])//2)**(1/2) in numbers:
        print('right')
    else:
        print('wrong')
