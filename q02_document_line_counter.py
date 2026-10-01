# Question 2: Document Line Counter
# Problem Statement: Given a file named notes.txt containing 4 lines of text, write a program that opens and reads the file, calculates how many lines exist in the file, and prints: "Total lines in document: [count]".
# Example File Content:
# text
# Introduction to AI
# Machine Learning basics
# Deep Learning architectures
# Generative AI applications
# Example Output: Total lines in document: 4
# Concept Tested: with open(..., "r"), .readlines() or looping over file object, len()
# Difficulty: Easy


# Optional: Ensure the file exists with sample content
sample_content = """Introduction to AI
Machine Learning basics
Deep Learning architectures
Generative AI applications"""

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write(sample_content)

# Read and count lines
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(f"Total lines in document: {len(lines)}")