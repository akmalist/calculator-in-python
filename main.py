from art import logo
from replit import clear
print(logo)

#math functions


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add, 
    "-": substract, 
    "/": divide, 
    "*": multiply
    }



def calculator():

    num1 = float(input("What's the number?\n"))
    for element in operations: 
        print(element)
    gameOn = True
    while gameOn:      
        oper_symbol = input("Which operation would you like to use?\n")
        num2 = float(input("What is the number? \n"))

        symbol_picked = operations[oper_symbol]

        answer = symbol_picked(num1,num2)

        print(f"{num1}{oper_symbol}{num2} = {answer}")
        continueValue = input(f"Type 'y' to continue calculator with {answer}, or type 'n' to exit: \n")
        if continueValue == "y":    
            num1=answer
        else:
            clear()
            gameOn=False
            calculator()

calculator()
    