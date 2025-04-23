# 86971_전력망을 둘로 나누기

# 제한사항
# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
# wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
# 1 ≤ v1 < v2 ≤ n 입니다.
# 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

# n :송전탑의 개수
# wires :전선 정보
# return :두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)
def solution(n, wires):
    answer = n
    # graph를 그린다.
    graph = [[] for i in range(n+1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 해당 와이어 절단 시, 두 전력망이 가지고 있는 송전탑 개수의 차이를 구한다.
    for wire in wires:
        v1, v2 = wire
        # v1에 연결된 송전탑 개수 구하기 DFS
        power_grid = set()
        visited = [False]*(n+1)
        stack = [v1]
        visited[v2] = True
        while stack:
            v1 = stack.pop()
            power_grid.add(v1)
            for v in graph[v1]:
                if not visited[v]:
                    stack.append(v)
            visited[v1] = True
        diff = n - len(power_grid) - len(power_grid)
        answer = min(answer, abs(diff))
    return answer

# 1: 완전탐색이니까 완전 탐색을 하자 
