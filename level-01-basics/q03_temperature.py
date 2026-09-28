# Question 3: Celsius to Fahrenheit Converter
# Problem Statement: Given a temperature in Celsius stored in a variable celsius, convert it to Fahrenheit using the formula:
# Fahrenheit = (celsius×9/5)+32. Print the result.
# Example Input: celsius = 25
# Example Output: 25°C is equal to 77.0°F
# Concept Tested: Float arithmetic, Formula implementation
# Difficulty: Very Easy

celsius = float(input("enter a celsius:"))
fahrenheit = (celsius*9/5)+32

print(f"{celsius}\u00B0C is equal to {fahrenheit}\u00B0F")