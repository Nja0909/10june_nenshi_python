# Pattern printing using nested for loops

rows = 5  # number of rows

for i in range(1, rows + 1):  # outer loop for each row
    for j in range(i):        # inner loop for stars
        print("*", end="")
    print()  # new line after each row
