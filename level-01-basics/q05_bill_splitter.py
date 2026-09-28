# Question 5: Simple Restaurant Bill Splitter
# Problem Statement: A restaurant bill amount is stored in total_bill, and the number of friends is stored in people_count. Calculate how much each person must pay. Print the share per person.
# Example Input: total_bill = 150.0, people_count = 3
# Example Output: Each person pays: 50.0
# Concept Tested: Float division (/), Variable assignment
# Difficulty: Very Easy

totalbill = float(input("enter a bill:"))
numberofperson = float(input("enter a number of person:"))

sharebill = totalbill/numberofperson

print("Each person pays:", sharebill)