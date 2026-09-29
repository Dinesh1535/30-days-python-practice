# Question 4: Context Window Checker
# Problem Statement: An AI model has a maximum limit of 4,000 tokens. Given a variable current_tokens:
# If current_tokens is greater than 4000, calculate how many tokens exceeded the limit and print: "Warning: Exceeded limit by [excess] tokens!"
# Otherwise, print: "Success: Input is within limit ([current_tokens] / 4000 tokens)."
# Example Input 1: current_tokens = 4350 -> Output: Warning: Exceeded limit by 350 tokens!
# Example Input 2: current_tokens = 2100 -> Output: Success: Input is within limit (2100 / 4000 tokens).
# Concept Tested: if / else, Arithmetic subtraction inside conditional branch
# Difficulty: Easy

tokens = int(input("Enter a tokens:"))
limit= 4000
axcess = tokens-limit
if tokens>limit:
    print(f"Warning: Exceeded limit by {axcess} tokens!")
else:
    print(f"Success: Input is within {tokens}/{limit} tokens")
