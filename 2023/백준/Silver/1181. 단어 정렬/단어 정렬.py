import sys

input_ = sys.stdin
N = int(input_.readline().rstrip())
my_dict = {}
for i in range(N):
    s = input_.readline().rstrip()
    my_dict[len(s)] = my_dict.get(len(s), set())
    my_dict[len(s)].add(s)
for i in sorted(my_dict.keys()):
    [print(x) for x in sorted(my_dict[i])]
