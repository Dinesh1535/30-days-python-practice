# Question 9: Find the Greater of Two Numbers
# Problem Statement: Given two numbers a and b, print which number is greater, or print "Both numbers are equal" if they are the same.
# Example Input 1: a = 25, b = 40 -> Output: b is greater (40)
# Example Input 2: a = 50, b = 50 -> Output: Both numbers are equal
# Concept Tested: Nested or multi-way comparisons
# Difficulty: Easy

a = int(input("Enter a number1:"))
b = int(input("Enter a number2:"))

if a>b:
    print(f"a is greater ({a})")
elif b>a:
    print(f"b is greater ({b})")
else:
    print("Both number are equal")
