#The Calculator App
#Task 1: Create functions for each arithmetic operation
#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use
#Task 3: Ensure code can handle division by zero & other potential errors

x = int(input("enter a number: "))
y = int(input("enter a number: "))
operation = input("enter desired operation: (add/subtract/multiply/divide)").lower()


def addition(x, y):
        if operation == "add":
            print(x + y)
def subtraction(x, y):
        if operation == "subtract":
            print(x - y)
def multiplication(x, y):
        if operation == "multiply":
            print(x * y)
def division(x, y):
        if y == 0:
                print("Cannot divide by 0")
        else:
            if operation == "divide":
                print(x / y)
       


addition(x, y)
subtraction(x, y)
multiplication(x, y)
division(x, y)