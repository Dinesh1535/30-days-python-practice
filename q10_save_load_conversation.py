# Question 10: Save & Load Conversation JSON File
# Problem Statement:
# Create a conversation list containing 2 dictionaries:
# python
# chat = [
#     {"role": "user", "content": "Explain gravity in one sentence."},
#     {"role": "assistant", "content": "Gravity is the force that pulls masses toward each other."}
# ]
# Save this list into a file named chat_session.json using json.dump() (with indent=2).
# Then, write code to read that file back using json.load() and print the assistant's reply.
# Example Output: Loaded Assistant Reply: Gravity is the force that pulls masses toward each other.
# Concept Tested: json.dump() with file pointer, json.load() with file pointer, Full round-trip
# Difficulty: Beginner+

import json

# 1. Define the conversation list
chat = [
    {"role": "user", "content": "Explain gravity in one sentence."},
    {"role": "assistant", "content": "Gravity is the force that pulls masses toward each other."}
]

# 2. Save the list to a file named chat_session.json
with open("chat_session.json", "w", encoding="utf-8") as file:
    json.dump(chat, file, indent=2)

# 3. Read the JSON file back
with open("chat_session.json", "r", encoding="utf-8") as file:
    loaded_chat = json.load(file)

# 4. Extract and print the assistant's reply
assistant_reply = loaded_chat[1]["content"]
print(f"Loaded Assistant Reply: {assistant_reply}")