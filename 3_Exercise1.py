# Introduction
greetingMessage = "Welcome to my calculator program!"
print(greetingMessage)

# Functions 
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Chose Operations 
print("Choose an Operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User choice
userChoice = int(input("Enter your choice: "))

# Taking input
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Conditionals for Calculator 
if userChoice == 1:
    print(add(num1, num2))

if userChoice == 2:
    print(subtract(num1, num2))

if userChoice == 3:
    print(multiply(num1, num2))

if userChoice == 4:
    print(divide(num1, num2))