S = input()
set_C = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
result = len(S)
for x in set_C:
    result -= S.count(x)
print(result)