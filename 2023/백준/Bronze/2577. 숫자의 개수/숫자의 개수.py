A, B, C = int(input()), int(input()), int(input())

from collections import Counter
count = Counter('0123456789'+str(A*B*C))
[print(i-1) for i in count.values()]