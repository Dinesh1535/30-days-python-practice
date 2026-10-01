# Question 1: Save System Prompt to Disk
# Problem Statement: Write a Python program that takes a string stored in system_prompt = "You are a helpful customer support agent for an airline." and writes it to a file named system_prompt.txt using with open() and encoding="utf-8". Print "Prompt saved successfully!" after writing.
# Example Input: system_prompt = "You are a helpful customer support agent for an airline."
# Example Output: A file named system_prompt.txt created with that content, and terminal outputs: Prompt saved successfully!
# Concept Tested: with open(..., "w"), File writing, UTF-8 encoding
# Difficulty: Very Easy

system_prompt = "You are a helpful customer support agent for an airline."

# Write the string to system_prompt.txt using UTF-8 encoding
with open("system_prompt.txt", "w", encoding="utf-8") as file:
    file.write(system_prompt)

print("Prompt saved successfully!")
