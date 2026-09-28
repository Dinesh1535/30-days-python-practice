# Question 7: Even or Odd Checker
# Problem Statement: Given an integer number, check whether it is even or odd using the modulo operator (%). Print "Even" if divisible by 2, otherwise print "Odd".
# Example Input 1: number = 8 -> Output: Even
# Example Input 2: number = 15 -> Output: Odd
# Concept Tested: Modulo operator (%), Boolean condition checking
# Difficulty: Easy

num = int(input("Enter a number:"))

if num % 2 == 0:
    print("Even")
elif num % 2 != 0:
    print("odd")
else:
    print("Zero")
