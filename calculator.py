"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Please enter an equation (or enter q to quite) > ").lower()
    token = user_input.split()
    if "q" in token:
        print("Exiting Program")
        break
#            (decide which math function to call based on first token)

    num1 = int(token[1])

    if len(token) == 3:
        num2 = int(token[2])

    if token[0] == "+":
        print(add(num1, num2))

    elif token[0] == "-":
        print(subtract(num1,num2))

    elif token[0] == "x":
        print(multiply(num1,num2))

    elif token[0] == "/":
        print(divide(num1,num2))

    elif token[0] == "square":
        print(square(num1))

    elif token[0] == "cube":
        print(cube(num1))

    elif token[0] == "power":
        print(power(num1, num2))
    
    elif token[0] == "mod":
        print(mod(num1, num2))