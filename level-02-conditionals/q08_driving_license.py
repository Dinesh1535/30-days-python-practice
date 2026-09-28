# Question 8: Driving License Eligibility
# Problem Statement: Given an age variable, print "Eligible for Driving License" if age is 18 or older. If younger, print "Not Eligible. Please apply after [years_left] years."
# Example Input 1: age = 21 -> Output: Eligible for Driving License
# Example Input 2: age = 15 -> Output: Not Eligible. Please apply after 3 years.
# Concept Tested: Relational operators (>=), Simple subtraction inside conditional branch
# Difficulty: Easy

age = int(input("Enter a number:"))

if age >= 18:
    print("Eligible for Driving License")
elif age < 18:
    age = 18-age
    print(f"please apply after {age} years")