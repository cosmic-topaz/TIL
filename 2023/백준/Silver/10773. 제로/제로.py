K = int(input())

stack_ = []
for i in range(K):
    x = int(input())
    if x:
        stack_.append(x)
    else:
        stack_.pop()

print(sum(stack_))