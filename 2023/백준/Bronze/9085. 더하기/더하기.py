# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
T = int(input())
# 각 테스트 케이스는 첫 줄에 자연수의 개수 N(1 ≤ N ≤ 100)이 주어지고,
for test_case in range(T):
    # 그 다음 줄에는 N개의 자연수가 주어진다. 각각의 자연수 사이에는 하나씩의 공백이 있다.
    N = int(input())
    numbers = list(map(int, input().split()))

    # 출력
    # 각 테스트 케이스에 대해서 주어진 자연수의 합을 한 줄에 하나씩 출력한다.
    print(sum(numbers))
