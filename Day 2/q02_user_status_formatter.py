# Question 2: User Status Formatter
# Problem Statement: Store a user's name in user_name = "Aria", their query count in queries_count = 12, and their active subscription status in is_pro_member = True. Print a clean profile summary string using an f-string: "User Aria | Queries: 12 | Pro: True".
# Example Input: user_name = "Aria", queries_count = 12, is_pro_member = True
# Example Output: User Aria | Queries: 12 | Pro: True
# Concept Tested: Multiple data types (string, int, bool), f-string printing
# Difficulty: Very Easy

user_name = input(("Enter a name:"))
query_count = int(input("Enter a number:"))
is_pro_member = True

print(f"User {user_name} | Queries:{query_count} | pro:{is_pro_member}")