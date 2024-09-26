height = int(input("Input the height of the triangle: "))
for column in reversed(range(1, height + 1)):       #--Generates the columns and reverses the range
    for row in range(column):                       #--Generates the rows
        print("*", end="")                          #--Prints the right triangle
    print()