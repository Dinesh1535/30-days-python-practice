# Question 15: Simple Star Staircase
# Problem Statement: Given an integer rows, use a loop to print a right-angled triangle made of stars *. Row 1 has 1 star, Row 2 has 2 stars, up to rows.
# Example Input: rows = 4
# Example Output:
# text
# *
# **
# ***
# ****
# Concept Tested: String repetition ("*" * i) or nested loops
# Difficulty: Beginner

n = int(input("enter a number:"))

for i in range(1,n+1):
    print("*"*i)
