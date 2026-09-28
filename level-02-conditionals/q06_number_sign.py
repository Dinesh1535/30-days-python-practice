# Question 6: Positive, Negative, or Zero
# Problem Statement: Given a number stored in variable num, write an if-elif-else statement to print whether the number is "Positive", "Negative", or "Zero".
# Example Input 1: num = 14 -> Output: Positive
# Example Input 2: num = -7 -> Output: Negative
# Example Input 3: num = 0 -> Output: Zero
# Concept Tested: if / elif / else syntax, Comparison operators (>, <, ==)
# Difficulty: Easy

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

