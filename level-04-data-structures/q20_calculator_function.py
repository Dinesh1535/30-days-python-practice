# Question 20: Simple Calculator Function
# Problem Statement: Write a function named calculate(a, b, operation) that takes two numbers and a string operation ("add", "subtract", "multiply", "divide"). The function should return the calculated result. Handle division by zero safely by returning "Error: Cannot divide by zero".
# Example Input 1: calculate(10, 5, "add") -> Output: 15
# Example Input 2: calculate(10, 0, "divide") -> Output: Error: Cannot divide by zero
# Concept Tested: Function definition def, Parameters, Return values, Conditionals inside functions
# Difficulty: Beginner+

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Error: Invalid operation"

# Example Tests
print(calculate(10, 5, "add"))
print(calculate(10, 0, "divide"))
print(calculate(10, 2, "multiply"))

