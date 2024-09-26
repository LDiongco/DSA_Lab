length = int(input("Enter the side length of the square: "))
for i in range(1, length + 1):
    if i == 1:
        print("*" * length)                     #--Prints the top part of the square
    elif i == length:
        print("*" * length)                     #--Prints the bottom part of the square
    else:
        print(f"*{" " * (length - 2)}*")        #--Hollows the area of the square