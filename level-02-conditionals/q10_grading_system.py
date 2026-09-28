# Question 10: Simple Grading System
# Problem Statement: Given a student's score from 0 to 100 in variable score:
# 90 and above: Print "Grade: A"
# 80 to 89: Print "Grade: B"
# 70 to 79: Print "Grade: C"
# Below 70: Print "Grade: F"
# Example Input 1: score = 85 -> Output: Grade: B
# Example Input 2: score = 62 -> Output: Grade: F
# Concept Tested: Chained relational expressions (and or sequential elif)
# Difficulty: Easy

score = int(input("enter a score:"))

if score >= 90:
    print("Grade: A")
elif score > 80:
    print("Grade: B")
elif score > 70:
    print("Grade: c")
elif score < 70:
    print("Grade: F ")
