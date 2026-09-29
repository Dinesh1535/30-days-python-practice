# Question 1: AI Token Cost Calculator
# Problem Statement: An AI service charges $0.02 for every 1,000 tokens processed. Given the number of tokens used in tokens_used = 2500 and the rate per thousand in rate_per_thousand = 0.02, calculate the total cost and print it formatted as: "Total Cost: $0.05".
# Example Input: tokens_used = 2500, rate_per_thousand = 0.02
# Example Output: Total Cost: $0.05
# Concept Tested: Variables, Integer division / multiplication, Float formatting
# Difficulty: Very Easy

token_used = int(input("Enter a Tokens:"))

rate_per_thousand = 0.02/1000
totalcost = rate_per_thousand*token_used

print("total Cost: ",totalcost)


