def multiplication():
    x = input("enter num : ")
    x = int(x)
    l = []
    for i in range(1, x + 1):
        v = []
        for j in range(1, i + 1):
            v.append(i * j)
        l.append(v)
    print(l)
multiplication()




