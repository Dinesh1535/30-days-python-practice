# Question 13: Multiplication Table
# Problem Statement: Given a number num, use a for loop to print its multiplication table from 1 to 10 in the format: [num] x [i] = [result].
# Example Input: num = 4
# Example Output:
# text
# 4 x 1 = 4
# 4 x 2 = 8
# ...
# 4 x 10 = 40
# Concept Tested: for loop, Formatted string printing inside a loop
# Difficulty: Beginner

num =int(input("Enter a number:"))

for i in range(1,11):
    result = num*i
    print(f"{num}*{i} = {result}")
