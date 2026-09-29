# Question 5: Long Word Finder (for loop)
# Problem Statement: Given a list of words extracted from an AI document: words = ["AI", "neural", "data", "intelligence", "bot", "transformer"]. Use a for loop to check each word. If a word has more than 4 letters (use len(word)), print: "Long word: [word]".
# Example Input: words = ["AI", "neural", "data", "intelligence", "bot", "transformer"]
# Example Output:
# text
# Long word: neural
# Long word: intelligence
# Long word: transformer
# Concept Tested: for loop over list, String length len(), Condition inside loop
# Difficulty: Beginner

words = input("Enter a words:").split(",")

for word in words:
    if len(word)>4:
        print(f"Long word: {word}")


