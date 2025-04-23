# 1676 팩토리얼 0의 개수
import math

N = int(input())
#print(N)

count = 0
i = 5
while(i <= N):
    count += N//i
    i *= 5

print(count)

# def factorial(n):
#     answer = 1
#     for i in range(1, n+1):
#         answer *= i
#     return answer

# print(factorial(N))