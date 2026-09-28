# Question 16: List Sum and Average
# Problem Statement: Given a list of numbers numbers = [10, 20, 30, 40, 50], write a program that calculates the sum of all elements using a loop, and then calculates and prints the average.
# Example Input: numbers = [10, 20, 30, 40, 50]
# Example Output:
# text
# Total: 150
# Average: 30.0
# Concept Tested: Iterating over lists, List length len(), Basic math
# Difficulty: Beginner+

numbers = list(map(int, input("Enter a 5 number:").split(",")))
total = 0
for i in numbers:
    total +=i
avg = total/len(numbers)

print(total)
print(avg)





