# 시간 복잡도 O(V * E^2)
# 1: 모든 와이어(간선)에 대해 해당 와이어 절단 시, 두 전력망이 가지고 있는 송전탑의 개수의 차이를 구한다. (완전 탐색)
# 2: 인접 리스트(graph)를 그린다.
# 3: 각 간선(와이어)에 대해, v2를 미리 방문 처리 한 후 DFS 하여, v1에 연결된 정점(송전탑)의 개수를 구한다.
# 4: answer 에는 diff 가 가장 작은 경우의 diff를 담는다.

# 💡💡💡💡💡💡💡💡💡💡
# Reference : https://devuna.tistory.com/32
# 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)

# 💡DFS, BFS은 특징에 따라 사용에 더 적합한 문제 유형들이 있습니다.

# 1) 그래프의 모든 정점을 방문하는 것이 주요한 문제 -> DFS, BFS
# 단순히 모든 정점을 방문하는 것이 중요한 문제의 경우 DFS, BFS 두 가지 방법 중 어느 것을 사용하셔도 상관없습니다.
# 둘 중 편한 것을 사용하시면 됩니다.

# 2) 경로의 특징을 저장해둬야 하는 문제 -> DFS
# 예를 들면 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 
# 각각의 경로마다 특징을 저장해둬야 할 때는 DFS를 사용합니다. (BFS는 경로의 특징을 가지지 못합니다)

# 3) 최단거리 구해야 하는 문제 -> BFS
# 미로 찾기 등 최단거리를 구해야 할 경우, BFS가 유리합니다.
# 왜냐하면 깊이 우선 탐색으로 경로를 검색할 경우 처음으로 발견되는 해답이 최단거리가 아닐 수 있지만, 
# 너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.

# 이밖에도 
# - 검색 대상 그래프가 정말 크다면 DFS를 고려
# - 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS

# 💡DFS와 BFS의 시간복잡도 (인접 행렬 vs 인접 리스트)

# 두 방식 모두 조건 내의 모든 노드를 검색한다는 점에서 시간 복잡도는 동일합니다.
# DFS와 BFS 둘 다 다음 노드가 방문하였는지를 확인하는 시간과 각 노드를 방문하는 시간을 합하면 됩니다.

# N은 노드, E는 간선일 때

# 인접 리스트 : O(N+E)
# 인접 행렬 : O(N²)

# ∴ 
# V(정점)에 비해 상대적으로 E(간선)의 갯수가 많을 경우 : 인접 행렬
# V(정점)에 비해 상대적으로 E(간선)의 갯수가 적을 경우 : 인접 리스트
# 일반적으로 E(간선)의 크기가 N²에 비해 상대적으로 적기 때문에, 인접 리스트 방식이 효율적임

# 인접 행렬의 경우, 
# "정점의 개수 N만큼 도는 2중 for문"을 돌려 두 정점 간에 간선이 존재하는지를 확인해야 함.
# 이때 N의 제곱만큼 돌게 되므로 O(N²)의 시간 복잡도가 됩니다.

# 인접 리스트로 구현된 경우, 
# 존재하는 간선의 정보만 저장되어 있으므로 인접 행렬에서 사용한 2중 for문이 필요하지 않음. 
# "방문 확인에 간선의 개수인 E의 두 배만큼의 시간"이 걸리고, 
# (1번에서 2, 6번이 방문하였는지를 확인하고 2번에서 1,3,6번을 방문하였는지 확인합니다. 이때 1번과 2번의 간선 하나에 두 번의 확인을 하기 때문에 두배만큼 시간이 걸립니다.) 
# 각 노드를 방문할 때 정점의 개수인 N만큼 걸립니다. 
# 따라서 O(N+2*E) = O(N+E)가 됩니다.

# 💡 DFS와 BFS의 구현
# 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색	
# 스택 또는 재귀함수로 구현	
# 현재 정점에 연결된 가까운 점들부터 탐색
# 큐를 이용해서 구현