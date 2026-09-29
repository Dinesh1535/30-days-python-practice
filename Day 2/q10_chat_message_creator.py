# Question 10: Chat Message Creator Function
# Problem Statement: Write a function called create_chat_turn(role, text). It should accept a role (like "user" or "assistant") and a text message, and return a Python dictionary with keys "role" and "content".
# Example Input: create_chat_turn("user", "Hello AI!")
# Example Output: {"role": "user", "content": "Hello AI!"}
# Concept Tested: Function returning a dictionary, Parameter mapping
# Difficulty: Beginner

def create_chat_turn(role,text):
    return {
        "role": role,
        "content": text
    }
print(create_chat_turn("user","Hello AI"))