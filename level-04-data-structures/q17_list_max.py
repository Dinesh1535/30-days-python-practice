# Question 17: Find the Maximum Value in a List (Without max())
# Problem Statement: Given a list of positive numbers scores = [45, 88, 23, 91, 72], find and print the largest number using a for loop and an if condition. Do not use Python's built-in max() function.
# Example Input: scores = [45, 88, 23, 91, 72]
# Example Output: Largest score: 91
# Concept Tested: Tracking a state variable across iterations, Conditional update
# Difficulty: Beginner+

scores =list(map(int, input("Enter a numbers:").split(",")))
largest_score = scores[0]
for i in scores:
    if i> largest_score:
        largest_score = i
print("largest score:", largest_score)

