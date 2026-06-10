# Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("Result:", result)

print("It is working fine!")

print("I am Purusharth:")

print("Day 2 of the GitHub")

print("I can do it no matter how difficult it is.")

print("Banana, vegitables, fruits, cat, dog.")