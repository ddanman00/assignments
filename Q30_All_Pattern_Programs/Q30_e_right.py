n = int(input("Enter rows: "))
k = 0
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + k), end=" ")
        k += 1
    print()
