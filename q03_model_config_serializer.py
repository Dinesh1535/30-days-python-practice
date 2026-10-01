# Question 3: Model Configuration Serializer (json.dumps)
# Problem Statement: You have a Python dictionary with model settings:
# python
# config = {
#     "model": "gemini-1.5-flash",
#     "temperature": 0.2,
#     "max_tokens": 512,
#     "stream": False
# }
# Convert this dictionary into a formatted JSON string with an indentation of 2 spaces using json.dumps() and print the result.
# Example Input: The dictionary above
# Example Output:
# json
# {
#     "model": "gemini-1.5-flash",
#     "temperature": 0.2,
#     "max_tokens": 512,
#     "stream": false
# }
# Concept Tested: import json, json.dumps(..., indent=2)
# Difficulty: Very Easy

import json

config = {
    "model": "gemini-1.5-flash",
    "temperature": 0.2,
    "max_tokens": 512,
    "stream": False,
}

# Convert dictionary to formatted JSON string with 2-space indentation
json_string = json.dumps(config, indent=2)

print(json_string)