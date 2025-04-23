p = []
for i in range(250000):
    p.append('1')
for i in [0, 1, 4, 6, 8, 9]:
    p[i] = '0'
for i in [2, 3, 5, 7]:
    for j in range(i, 250000//i):
        p[i*j] = '0'
for i in [x for x in range(11, 100) if p[x] == '1']:
    for j in [x for x in range(i, 250000//i) if p[x] == '1']:
        p[i*j] = '0'
for i in [x for x in range(101, 10000) if p[x] == '1']:
    for j in [x for x in range(i, 250000//i) if p[x] == '1']:
        p[i*j] = '0'
for i in [x for x in range(10001, 250000) if p[x] == '1']:
    for j in [x for x in range(i, 250000//i) if p[x] == '1']:
        p[i*j] = '0'


def bertrand(n): # 1 ≤ n ≤ 123,456 / 246912
    result = 0
    for x in range(n+1, 2*n+1):
            result += int(p[x])
    print(result)

while True:
    test_case = int(input())
    if test_case:
        bertrand(test_case)
    else:
        exit()