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
    user_input = user_input.split(" ")
    for i in range(1,len(user_input)):
        user_input[i] = int(user_input[i])
#     tokenize input
    if user_input[0] == "q":
#     if the first token is 'q'
        break
#         quit
    elif user_input[0] == "+":
        print add(user_input[1], user_input[2])
    elif user_input[0] == "-":
        print subtract(user_input[1], user_input[2])
    elif user_input[0] == "*":
        print multiply(user_input[1], user_input[2])
    elif user_input[0] == "/":
        print divide(user_input[1], user_input[2])
    elif user_input[0] == "square":
        print square(user_input[1])
    elif user_input[0] == "cube":
        print cube(user_input[1])
    elif user_input[0] == "power":
        print power(user_input[1], user_input[2])
    elif user_input[0] == "mod":
        print mod(user_input[1], user_input[2])
    else:
        print "That was not a valid choice. Please try again."






#     else
#         decide which math function to call based on first token
