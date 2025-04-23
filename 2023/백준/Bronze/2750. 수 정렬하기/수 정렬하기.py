# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
N = int(input())
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
numbers = [0]*2001
for i in range(1, N+1): # O(N)
    n = int(input())+1000
    numbers[n] += 1
# numbers[i] = i+1000 의 갯수

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
for n in range(2000+1):
    for i in range(numbers[n]):
        print(n-1000)