# Question 18: Count Even and Odd Numbers in a List
# Problem Statement: Given a list of integers nums = [1, 2, 3, 4, 5, 6, 7, 8, 9], count how many numbers are even and how many are odd. Print both counts.
# Example Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Example Output:
# text
# Even numbers: 4
# Odd numbers: 5
# Concept Tested: List iteration, Counters, Modulo condition inside loop
# Difficulty: Beginner+


# Question 18: Count Even and Odd Numbers in a List

nums = list(map(int, input("Enter a list number:").split(",")))

# Initialize counter variables
even_count = 0
odd_count = 0

# Loop through each number in the list
for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)