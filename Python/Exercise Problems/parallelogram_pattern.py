num = int(input("Enter the number:"))

for i in range(0, num):
    for j in range(0, num-i-1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()
