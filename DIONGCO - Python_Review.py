#**************************************
# Lab Assignment #1: Python Review
# Programmed by: Lance Raven F. Diongco
# Course, Year, and Section: BSCpE 2-3
# Instructor: Engr. Godofredo T. Avena
# Date Submitted: September 19, 2024
#**************************************

#-- TEMPERATURE CONVERTER -- 
def Temperature_Converter():
    print(f"""

CHOSEN PROGRAM --->> [ TEMPERATURE CONVERTER ] <<---
|
|""")                        
    while True:                                     #--Filters user input
        user_input = input(f"\nPlease input a temperature --> ")
        try: 
            user_input = float(user_input)
            break   
        except ValueError:
            print(f"\nError: Please enter only the value of the temperature.")
    
    while True:                                     #--Filters user input
        conversion_type = input(f"\nPlease select a conversion type:\n[1] Celcius to Fahrenheit\n[2] Fahrenheit to Celcius\n--> ")
        try:
            conversion_type = int(conversion_type)
            if conversion_type in range(1,2+1):
                break                               #--Only accepts 1 or 2
            else:
                print(f"\nError: Please enter [1] or [2] only.")
        except ValueError:
            print(f"\nError: Please enter [1] or [2] only.")

    if conversion_type == 1:                        #--Formula implementation & output generation
        result = (user_input * 1.8) + 32
        print(f"\n\n[1] Conversion from Celcius to Fahrenheit:\nResult --> [ {result:.2f}°F ]")
    elif conversion_type == 2:
        result = (user_input - 32) / 1.8
        print(f"\n\n[2] Conversion from Fahrenheit to Celcius:\nResult --> [ {result:.2f}°C ]")
    
    #--Asks the user if they want to use the program again
    while True:                                     
        repeat = input(f"\nWould you like to try again? --> ")
        if repeat.lower() == "yes":
            Temperature_Converter()                  #--Calls out the Main Program
        elif repeat.lower() == "no":
            main()
        else:
            print(f"\nError: Please input only 'yes' or 'no'.")
#-- END OF TEMPERATURE CONVERTER -- 

    
#-- OHM'S LAW CALCULATOR --
def voltage_calc():                                 #--Calculates VOLTAGE with user input
    print(f"[1] Voltage | Formula: V = I * R")
    while True:                                     #--Filters user input
        current = input(f"\nPlease input CURRENT value --> ")
        try: 
            current = float(current)
            break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    while True:                                     #--Filters user input
        resistance = input(f"\nPlease input RESISTANCE value --> ")
        try:
            resistance = float(resistance)
            break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    result = current * resistance                   #--Formula Implementation
    print(f"\n[1] Voltage:\nResult --> [ {result:.2f}V ]")

def current_calc():                                 #--Calculates CURRENT with user input
    print(f"[2] Current | Formula: I = V / R")
    while True:                                     #--Filters user input
        voltage = input(f"\nPlease input VOLTAGE value --> ")
        try: 
            voltage = float(voltage)
            break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    while True:                                     #--Filters user input
        resistance = input(f"\nPlease input RESISTANCE value --> ")
        try:
            resistance = float(resistance)
            if resistance == 0.0:                   #--Rejects the value, 0
                print(f"\nError: Division by 0 is NOT possible. Please enter another value.")
            else:
                break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    result = voltage / resistance                   #--Formula implementation
    print(f"\n[2] Current:\nResult --> [ {result:.2f}A ]")

def resistance_calc():                              #--Calculates RESISTANCE with user input
    print(f"[3] Resistance | Formula: R = V / I")
    while True:                                     #--Filters user input
        voltage = input(f"\nPlease input VOLTAGE value --> ")
        try: 
            voltage = float(voltage)
            break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    while True:                                     #--Filters user input
        current = input(f"\nPlease input CURRENT value --> ")
        try:
            current = float(current)
            if current == 0.0:                      #--Rejects the value, 0
                print(f"\nError: Division by 0 is NOT possible. Please enter another value.")
            else:
                break
        except ValueError:
            print(f"\nError: Please enter a numerical value")
    
    result = voltage / current                      #--Formula Implementation
    print(f"\n[1] Voltage:\nResult --> [ {result:.2f}Ω ]")

def Ohms_Law_Calc():
    print(f"""

CHOSEN PROGRAM --->> [ OHM'S LAW CALCULATOR ] <<---
|
|""")                                 
    while True:                                     #--Filters the responses
        result_type = input(f"\nPlease select what you want to calculate?\n[1] Voltage, [2] Current, [3] Resistance\n --> ")
        try:
            result_type = int(result_type)
            break
        except ValueError:
            print(f"\nError: Please choose between [1], [2], or [3] only.")

    #--Links and calls the appropriate calculators with user input
    if result_type == 1:    
        voltage_calc()
    elif result_type == 2:
        current_calc()
    elif result_type == 3:
        resistance_calc()
    
    #--Asks the user if they want to use the program again
    while True:
        repeat = input("\nWould you like to try again? --> ")
        if repeat.lower() == "yes":
            Ohms_Law_Calc()
        elif repeat.lower() == "no":
            main()
        else:
            print("\nError: Please enter only 'yes' or 'no'.")
#-- END OF OHM'S LAW CALCULATOR -- 

#-- DIAMOND SHAPE -- 
def Diamond_Shape():
    print(f"""

CHOSEN PROGRAM --->> [ DIAMOND SHAPE ] <<---
|
|""")   
    while True:                                     #--Filters user input
        n = input(f"\nPlease input the size of your Diamond.\nIt should be an ODD number --> ")
        try:
            n = int(n)
            if n % 2 == 0:                          #--Rejects user input if not odd
                print(f"\nError: Please enter only ODD numbered values.")
            elif n % 2 == 1:
                break
        except ValueError:                          #--Checks for Value Errors
            print(f"\nError: Please enter only ODD numbered values.")

    nhalf = int(n/2)

    print(f"Generated Diamond:\n")

    #--Generates the Top-Half of the Diamond.
    for rows in range(nhalf):
        for columns in range(rows, nhalf):          #--Generates the Spaces 
            print(" ", end="")
        for columns in range(rows):                 #--Completes the First Block
            print("*", end="")
        for columns in range(rows + 1):             #--Generates the Missing Half of the Top-Half
            print("*", end="")
        print()

    #--Generates the Bottom-Half of the Diamond.
    for rows in range(nhalf + 1):
        for columns in range(rows):                 #--Generates the Spaces
            print(" ", end="")
        for columns in range(rows, nhalf):          #--Completes the First Block
            print("*",end="")
        for colums in range(rows, nhalf + 1):       #--Generates the Missing Half of the Bottom-Half
            print("*", end="")
        print()
    
    #--Asks the user if they want to use the program again
    while True:
        repeat = input("\nWould you like to try again? --> ")
        if repeat.lower() == "yes":
            Diamond_Shape()
        elif repeat.lower() == "no":
            main()
        else:
            print("\nError: Please enter only 'yes' or 'no'.")
#-- END OF DIAMOND SHAPE -- 

#-- MAIN PROGRAM -- 
def main():
    while True:
        program = input(f"""
Which program would you like to use?\n
[1] Temperature Converter
 |
[2] Ohm's Law Calculator
 |
[3] Diamond Shape
 |
 |
[0] Exit Program
--> """)
        try:
            program = int(program)
            if program in range(0,3+1):
                break
            else:
                print("Error: Please choose between [0], [1], [2], or [3] only.")
        except ValueError:
            print("Error: Please choose between [0], [1], [2], or [3] only.")
    
    if program == 1:
        Temperature_Converter()
    elif program == 2:
        Ohms_Law_Calc()
    elif program == 3:
        Diamond_Shape()
    elif program == 0:
        exit()
#-- END OF MAIN PROGRAM --


main()                                              #-- CALLS OUT MAIN PROGRAM -- 
