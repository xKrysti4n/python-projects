import os
from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

end = False
print(logo)
print("Welcome to the calculator")
n1 = float(input("Write first number: "))
print("Choose operation (+, -, *, /)")
operation = input("Pick an operation from the line above: ").lower()
n2 = float(input("Write second number: "))

while not end:
    if operation == "+":
        num = add(n1,n2)
    elif operation == "-":
        num = subtract(n1,n2)
    elif operation == "*":
        num = multiply(n1,n2)
    elif operation == "/":
        num = divide(n1,n2)
    else:
        print("Invalid operation")
    print(f"{n1} {operation} {n2} = {num}")
    decision = input("Do you want to continue with current answer? (yes/no): ").lower()
    if decision == "no":
        end = True
        print("Goodbye")
    elif decision == "yes":
        os.system('cls')
        print(logo)
        n1 = num
        print("Choose operation (+, -, *, /)")
        operation = input("Pick an operation from the line above: ").lower()
        n2 = float(input("Write second number: "))
    else:
        print("Invalid decision")
        end = True