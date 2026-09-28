# Question 14: Countdown Timer (While Loop)
# Problem Statement: Given a starting number count, use a while loop to print a countdown from count down to 1. After the loop ends, print "Liftoff!".
# Example Input: count = 3
# Example Output:
# text
# 3
# 2
# 1
# Liftoff!
# Concept Tested: while loop condition, Loop decrement (count -= 1)
# Difficulty: Beginner

count = int(input("Enter a number:"))
i = 0
while i<count:
    print(count)
    count -= 1
print("Liftoff!")