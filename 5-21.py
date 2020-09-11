for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        r = i * j
        print("%d*%d=%-3d" % (i, j, r), end=" ")
    print()