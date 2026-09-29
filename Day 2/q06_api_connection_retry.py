# Question 6: API Connection Retry (while loop)
# Problem Statement: Simulate retrying a failed AI connection. Start with attempt = 1. Use a while loop that runs while attempt <= 3. Inside the loop, print "Connecting to AI... Attempt [attempt]", and then increase attempt by 1. After the loop finishes, print "Connection failed. Please check your API key."
# Example Input: attempt = 1
# Example Output:
# text
# Connecting to AI... Attempt 1
# Connecting to AI... Attempt 2
# Connecting to AI... Attempt 3
# Connection failed. Please check your API key.
# Concept Tested: while loop, Loop counter increment (attempt += 1), Code execution after loop
# Difficulty: Beginner


attempt = int(input("Enter a number:"))

while attempt<=3:
    print(f"Connecting to AI... Attempt{attempt}")
    attempt +=1
print("Connection failed. Please check your API key")


