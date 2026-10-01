# Question 5: Safe Document Reader (Missing File Defense)
# Problem Statement: Ask the user (or store in a variable) a filename target_file = "missing_data.txt". Try to open and read the file. If the file does not exist, do not crash! Catch FileNotFoundError and print: "Safe Error: The file 'missing_data.txt' was not found. Please check the path."
# Example Input: target_file = "missing_data.txt" (file does not exist on disk)
# Example Output: Safe Error: The file 'missing_data.txt' was not found. Please check the path.
# Concept Tested: try...except FileNotFoundError
# Difficulty: Easy

target_file = "missing_data.txt"

try:
    with open(target_file, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Safe Error: The file '{target_file}' was not found. Please check the path.")