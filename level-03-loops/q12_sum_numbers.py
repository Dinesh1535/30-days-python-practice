# Question 12: Sum of First N Numbers
# Problem Statement: Given an integer n, use a loop to calculate the sum of all numbers from 1 up to n. Print the final sum.
# Example Input: n = 5 (Calculation: 1 + 2 + 3 + 4 + 5)
# Example Output: Sum: 15
# Concept Tested: Loop accumulator variable (total += i)
# Difficulty: Beginner

n = int(input("Enter a number:"))
total =0
for i in range(1,n+1):
    total +=i
print(total)