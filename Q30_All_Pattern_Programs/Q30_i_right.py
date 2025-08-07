n = int(input("Enter rows: "))
digit = 1
for i in range(n):
    for j in range(i + 1):
        print(digit, end=" ")
        digit += 1
    print()
