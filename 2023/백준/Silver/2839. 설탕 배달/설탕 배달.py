N = int(input())

def getNumber(n):
    # 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
    y = 0
    if n%5:
        while (n%5+5*y)%3:
            y += 1
            if n-5*y < 0:
                return -1
    x = n//5 -y
    y = (n%5+5*y)//3
    return x + y

print(getNumber(N))