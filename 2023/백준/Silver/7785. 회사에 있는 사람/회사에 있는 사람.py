import sys
N = int(input())
input_ = sys.stdin
members = {}
for i in range(1, N+1):
    data = input_.readline().rstrip()
    name, detail = data[:-6], data[-5:]
    # print(data, name, detail)
    members[name] = detail

current = [name for name in members.keys() if members[name] == 'enter'] # O(N)
current = sorted(current, reverse=True) # O(NlogN)
[print(name) for name in current] # O(N)