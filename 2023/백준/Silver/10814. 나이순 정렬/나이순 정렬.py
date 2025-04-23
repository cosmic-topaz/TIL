import sys
N = int(input())
input_ = sys.stdin
my_dict = {}
for _ in range(N):
    my_key, my_value = input_.readline().split()
    my_key = int(my_key)
    my_dict[my_key] = my_dict.get(my_key, list())
    my_dict[my_key].append(my_value)
for my_key in sorted(my_dict.keys()):
    for my_value in my_dict[my_key]:
        print(my_key, my_value)