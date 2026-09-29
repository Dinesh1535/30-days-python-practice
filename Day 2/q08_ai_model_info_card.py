# Question 8: AI Model Info Card (Dictionary)
# Problem Statement: Create a dictionary named model_info containing:
# "name": "Gemini-Pro"
# "context_window": 32000
# "is_multimodal": True
# Write code to print each item on a separate line in this exact format:
# Model Name: Gemini-Pro
# Context Window: 32000 tokens
# Supports Images: True
# Example Input: The dictionary described above
# Example Output:
# text
# Model Name: Gemini-Pro
# Context Window: 32000 tokens
# Supports Images: True
# Concept Tested: Creating dictionaries, Accessing values using keys (dict["key"]), f-strings
# Difficulty: Beginner

model_name = input("Enter a modal name:")
context_window = input("Enter a context window:")
supports_images = input("Enter a supports image:")

print(f"Model Name:{model_name}")
print(f"context window:{context_window}tokens")
print(f"supports image:{supports_images}")