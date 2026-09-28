# Question 19: User Profile Dictionary Lookup
# Problem Statement: Create a dictionary called user_profile containing keys: "name", "role", and "experience_years". Given a key name to check in a variable search_key, write an if-else statement to print its value if it exists, or print "Key not found" if it does not.
# Example Input 1: search_key = "role" -> Output: Role: GenAI Intern
# Example Input 2: search_key = "salary" -> Output: Key not found
# Concept Tested: Dictionary syntax, in keyword for dictionary keys
# Difficulty: Beginner+

user_profile = {
    "name": "Alex",
    "role": "GenAI Intern",
    "experience_years": 1
}
search_key = input("Enter A searchkey:")

# Check if the key exists using the 'in' keyword
if search_key in user_profile:
    print(f"{search_key.capitalize()}: {user_profile[search_key]}")
else:
    print("Key not found")