# 입력
# 첫째 줄에 x, y, w, h가 주어진다.
x, y, w, h = map(int, input().split())
# 출력
# 첫째 줄에 문제의 정답을 출력한다
print(min(w-x, x-0, h-y, y-0))
# 제한
# 1 ≤ w, h ≤ 1,000
# 1 ≤ x ≤ w-1
# 1 ≤ y ≤ h-1
# x, y, w, h는 정수