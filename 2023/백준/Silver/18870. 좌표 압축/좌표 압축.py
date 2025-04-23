import sys

N = int(input())
input_ = sys.stdin
my_dict = {}
xi = [-1 for i in range(N)]
x = list(map(int, input_.readline().split()))
for _ in range(N):
    p_key = x[_]//(10**5)
    s_key = x[_]%(10**5)
    my_dict[p_key] = my_dict.get(p_key, dict())
    my_dict[p_key][s_key] = my_dict[p_key].get(s_key, list())
    my_dict[p_key][s_key].append(_)


i = 0
for p_key in sorted(my_dict.keys()):

    for s_key in sorted(my_dict[p_key].keys()):
        for _ in my_dict[p_key][s_key]:
            xi[_] = i
        i += 1

print(*xi)