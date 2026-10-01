# Question 7: Sliding Memory Window (Last N Messages)
# Problem Statement: Given a list representing a long chat history:
# python
# history = ["Turn 1", "Turn 2", "Turn 3", "Turn 4", "Turn 5", "Turn 6", "Turn 7"]
# Write a program that uses negative list slicing to extract and print only the last 3 turns to fit into an AI's context window.
# Example Input: history list above
# Example Output: Recent turns: ['Turn 5', 'Turn 6', 'Turn 7']
# Concept Tested: Negative list slicing (list[-n:])
# Difficulty: Easy

history = ["Turn 1", "Turn 2", "Turn 3", "Turn 4", "Turn 5", "Turn 6", "Turn 7"]

# Extract the last 3 elements using negative list slicing
recent_turns = history[-3:]

print(f"Recent turns: {recent_turns}")