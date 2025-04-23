# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 
# 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

# 네번째 점 찾기
# 직사각형의 네 점의 좌표는 
# (x, y) (x, y') (x', y) (x', y')

if A[0] == B[0]:
    dx = C[0]
    if A[1] == C[1]:
        dy = B[1]
    else:
        dy = A[1]
elif A[0] == C[0]:
    dx = B[0]
    if A[1] == B[1]:
        dy = C[1]
    else:
        dy = A[1]
else:
    dx = A[0]
    if A[1] == B[1]:
        dy = C[1]
    else:
        dy = B[1]

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.
print(dx, dy)