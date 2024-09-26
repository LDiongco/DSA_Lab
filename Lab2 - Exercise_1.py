def compute_power(result, power, base = 0):
    if power > 1:                           
        if base == 0:                 #--Makes the base equal to the result for the first iteration
            base = result
        new_result = result * base        #--Generates a new result
        new_power = power - 1               #--Decrements the power by 1
        compute_power(result = new_result, power= new_power, base = base)     #--Reuses the function with new values from the previous function
    elif power == 1:
        print(f"The computed result is: {result}")      #--Ouputs the result
    elif power == 0:
        print("The computed result is: 1")              #--Handles bases raised to 0

base = int(input("Input your base number >> "))
exponent = int(input("Input your exponent >> "))

compute_power(base, exponent)