"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
# repeat forever:
    user_input = raw_input("Please enter a calculation: ")
#     read input
    user_input = user_input.lower()
#put user_input into lowercase letters
    user_input = user_input.split(" ")
#splits user_input into separate strings in a single list - "tokenizes"
    for i in range(1,len(user_input)):
#iterates through the list starting with index 1 (skipping operator)
        if user_input[i].isdigit() == False:
            print "Incorrect input - enter correct information."
            continue
        user_input[i] = int(user_input[i])
#changes type from string to integer
    if user_input[0] == "q":
#     if the first token is 'q'
        break
#         quit
    elif user_input[0] == "+":
        add_value = 0
        for i in range(1, len(user_input)):
            add_value = add(add_value, user_input[i])
        print add_value
            # print current_value
#if user_input starts with "+", call add function and print output
    elif user_input[0] == "-":
        subtract_value = user_input[1]
        for i in range(2, len(user_input)):
            subtract_value = subtract(subtract_value, user_input[i])
        print subtract_value
#if user_input starts with "-", call subtract function and print output
    elif user_input[0] == "*":
        multiply_value = 1
        for i in range(1, len(user_input)):
            multiply_value = multiply(multiply_value, user_input[i])
        print multiply_value        
#if user_input starts with "*", call multiply function and print output
    elif user_input[0] == "/":
        divide_value = user_input[1]
        for i in range(2, len(user_input)):
            divide_value = divide(divide_value, user_input[i])
        print divide_value    
#if user_input starts with "/", call divide function and print routput
    elif user_input[0] == "square":
        print square(user_input[1])
#if user_input starts with "square", call square function and print output
    elif user_input[0] == "cube":
        print cube(user_input[1])
#if user_input starts with "cube", call cube function and print output
    elif user_input[0] == "power":
        power_value = user_input[1]
        for i in range(2, len(user_input)):
            power_value = power(power_value, user_input[i])
        print power_value   
#if user_input starts with "power", call power function and print output
    elif user_input[0] == "mod":
        print mod(user_input[1], user_input[2])
#if user_input starts with "mod", call mod function and print output
    else:
        print "That was not a valid choice. Please try again."
#provides response if user inputs invalid selection





#     else
#         decide which math function to call based on first token
