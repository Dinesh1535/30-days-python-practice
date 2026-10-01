# Question 4: Extract Answer from API Response (json.loads)
# Problem Statement: An AI server returned the following raw JSON string:
# python
# raw_response = '{"id": "chat-101", "model": "gemini", "choices": [{"text": "Python is awesome!"}]}'
# Parse this string back into a Python dictionary using json.loads(), and print only the text message: "AI says: Python is awesome!".
# Example Input: The raw_response string above
# Example Output: AI says: Python is awesome!
# Concept Tested: json.loads(), Nested dictionary & list indexing
# Difficulty: Easy

import json

raw_response = '{"id": "chat-101", "model": "gemini", "choices": [{"text": "Python is awesome!"}]}'

# Parse the JSON string into a Python dictionary
data = json.loads(raw_response)

# Extract the nested text value
text = data["choices"][0]["text"]

# Print formatted result
print(f"AI says: {text}")