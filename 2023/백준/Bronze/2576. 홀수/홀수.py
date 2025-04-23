N = 7
odd_n = []
for i in range(N): # 입력의 첫째 줄부터 일곱 번째 줄까지
    # 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.
    n = int(input())
    if n%2:
        odd_n.append(n)
if len(odd_n):
    print(sum(odd_n))
    print(min(odd_n))
else:
    print(-1)
