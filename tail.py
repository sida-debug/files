def head(filename, n):
    f = open(filename, "r")

    for i in range(n):
        print(f.readline())