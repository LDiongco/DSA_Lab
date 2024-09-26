def compute_cube(number):                   #--Function that computes and returns the cube of the given argument
    return number * number * number

array_size = int(input("Enter the size: "))
array_list = input("Enter the elements separated by space: ").split(" ")        #--Makes the input into a list

if array_size == len(array_list):           #--Checks if the size aligns with the number of items in the list
    for item in array_list:
        print(compute_cube(int(item)))      #--Computes for the cube of each item from the list
else:
    print("! Error: Array size should be equal to the number of elements !")
