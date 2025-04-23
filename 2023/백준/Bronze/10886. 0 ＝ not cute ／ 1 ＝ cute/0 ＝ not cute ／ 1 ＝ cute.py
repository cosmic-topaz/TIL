N = int(input()) # 설문조사를 한 사람의 수 N : (1 ≤ N ≤ 101, N은 홀수)
CUTE = 0
for n in range(1, N+1): # 조사결과 수집
    if int(input()): # true if 응답 = 1 (준희는 귀여워)
        CUTE += 1
    else: # 응답 = 0 (준희는 안 귀여워)
        CUTE -= 1
if CUTE > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")