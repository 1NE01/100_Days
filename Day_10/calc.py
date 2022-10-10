from calc_art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
calculate = {'+': add,'-': subtract, '*': multiply,'/': divide}
def calculator():
    print(logo)
    do_continue = True
    num1 = float(input('What is the first number?\n'))
    for operation_char in calculate:
        print(operation_char)
    while do_continue:
        operation_choice = input('Pick an operation: (+, -, *, /)\n')
        num2 = float(input('What is the next number?\n'))
        operation =  calculate[operation_choice]
        result = operation(num1, num2)
        print(f"{num1} {operation_choice} {num2} = {result} ")
        continued = input(f"Type 'y' to continue  {result}, or type 'n' to start a new calculation, or type 'q' to exit\n")
        if continued == 'n':
            do_continue = False
            calculator()
        elif continued == 'q':
            do_continue = False
        else:
            num1 = result
calculator()