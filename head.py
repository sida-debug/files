def head(filename, n):
    f = open(filename, "r")

    for i in range(n):
        print(f.readline())

print(head("C:\Users\sid\OneDrive\Documents\pythonTest.txt", 1))