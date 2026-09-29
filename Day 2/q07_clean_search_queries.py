# Question 7: Clean and Standardize Search Queries (List)
# Problem Statement: You have a list of raw search queries typed by users with messy spaces and mixed cases: raw_queries = ["  WHAT IS RAG?  ", "python FOR ai", "  prompt ENGINEERING  "]. Use a for loop to clean each query using .strip() (removes extra spaces) and .lower() (converts to lowercase), and print each cleaned query.
# Example Input: raw_queries = ["  WHAT IS RAG?  ", "python FOR ai", "  prompt ENGINEERING  "]
# Example Output:
# text
# what is rag?
# python for ai
# prompt engineering
# Concept Tested: List iteration, String methods (.strip(), .lower())
# Difficulty: Beginner

raw_queries = input("Enter a raw_queries:").split(",")

for query in raw_queries:
    query = query.strip().lower()
    print(query)



