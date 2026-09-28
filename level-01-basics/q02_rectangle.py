# Question 2: Rectangle Area and Perimeter
# Problem Statement: Given the length and width of a rectangle as variables, calculate and print both its area (length * width) and its perimeter (2 * (length + width)).
# Example Input: length = 10, width = 5
# Example Output:
# text
# Area: 50
# Perimeter: 30
# Concept Tested: Numerical variables, Basic arithmetic operators
# Difficulty: Very Easy

len = int(input("Enter a length:"))
wid = int(input("Enter a width:"))

area = len*wid
perimeter = 2*(len+wid)

print("Area:",area)
print("Perimetr:",perimeter)