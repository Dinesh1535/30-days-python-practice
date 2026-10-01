# Question 8: Document Preview (Head and Tail Slicing)
# Problem Statement: You have a document broken into 6 paragraph chunks:
# python
# chunks = ["Chunk 1: Intro", "Chunk 2: Background", "Chunk 3: Data", "Chunk 4: Analysis", "Chunk 5: Results", "Chunk 6: Conclusion"]
# Print the first 2 chunks as "Document Header:" and the last 2 chunks as "Document Footer:".
# Example Input: chunks list above
# Example Output:
# text
# Document Header: ['Chunk 1: Intro', 'Chunk 2: Background']
# Document Footer: ['Chunk 5: Results', 'Chunk 6: Conclusion']
# Concept Tested: Positive slice ([:2]) and negative slice ([-2:])
# Difficulty: Easy

chunks = [
    "Chunk 1: Intro",
    "Chunk 2: Background",
    "Chunk 3: Data",
    "Chunk 4: Analysis",
    "Chunk 5: Results",
    "Chunk 6: Conclusion",
]

# First 2 elements (positive slicing)
doc_header = chunks[:2]

# Last 2 elements (negative slicing)
doc_footer = chunks[-2:]

print(f"Document Header: {doc_header}")
print(f"Document Footer: {doc_footer}")