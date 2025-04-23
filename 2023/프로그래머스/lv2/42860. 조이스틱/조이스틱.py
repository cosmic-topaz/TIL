# return : 조이스틱 조작 횟수의 최솟값
def solution(name):
    answer = len(name) - 1
    
    # 순회의 수 구하기
    graph = [0]
    for char in name:
        if char == 'A':
            graph [-1] += 1
        else:
            answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
            graph.append(1)
    
    route_1 = graph[-1] - 1
    route_2 = graph[0] - 1
    route_3 = 0
    length_A = max(graph) - 1
    i = name.find('A'*length_A)
    j = len(name) - i - length_A
    if i != 0 and j != 0:
        route_3 = length_A - min(i-1, j)
    
    answer -= max(route_1, route_2, route_3)

    return answer