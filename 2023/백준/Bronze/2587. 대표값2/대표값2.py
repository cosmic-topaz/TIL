numbers = []
for _ in range(5):
    numbers.append(int(input()))

mean = int(sum(numbers)/len(numbers))
median = sorted(numbers)[2]

print(mean)
print(median)