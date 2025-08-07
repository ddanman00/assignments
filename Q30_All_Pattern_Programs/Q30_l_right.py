n = int(input("Enter rows: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()
