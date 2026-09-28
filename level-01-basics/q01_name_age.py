# Question 1: Name and Future Age

# Problem Statement: Store a person's name in a variable called name and their current age in a variable called age. Calculate their age after 5 years and print a friendly message: "Hello [name], you will be [new_age] years old in 5 years!"
# Example Input: name = "Alex", age = 20
# Example Output: Hello Alex, you will be 25 years old in 5 years!
# Concept Tested: Variables, Integer addition, String formatting / printing
# Difficulty: Very Easy

name = input("Enter a name:")
age = int(input("Enter a age:"))

ages = age + 5

print("Hello "+ str(name),", you will be "+str(ages)+ " years old in 5 years!")