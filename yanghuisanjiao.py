def triangles():
    L = [1]
    while True:
        yield L
        L.append(0) #补完0后L的状态 [1,0]
        L = [L[i - 1] + L[i] for i in range(len(L))] #生成第1行

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break