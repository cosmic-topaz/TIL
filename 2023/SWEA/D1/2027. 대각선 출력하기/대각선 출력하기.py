n = 5
t = '#'+'+'*(n-1)
for i in range(0,n):
    print(t)
    t = t.replace('#+', '+#')