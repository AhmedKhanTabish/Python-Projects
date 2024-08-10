n = 1
n = int(input("Size of pyramid:   ", ))
print(n)


while n not in range (1, 9):
    n = int(input("Size of pyramid:   ", ))
    print(n)


for i in range(0, n, 1):
    for j in range(0, n-i, 1):
        print(" ", end="")
    for j in range(0, i+1, 1):
        print("#")
    for j in range(0, n-i, 1):
        print(" ", end="")
    for j in range(0, i+1, j+1):
        print("#")
print("\n")
