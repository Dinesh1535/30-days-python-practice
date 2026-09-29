# Question 3: AI Safety Score Flag
# Problem Statement: An AI moderation system gives a text safety score between 0.0 and 1.0. Given a variable safety_score:
# If the score is greater than or equal to 0.8: print "Status: Flagged - Unsafe"
# If the score is between 0.5 and 0.79 (inclusive): print "Status: Review Required"
# If the score is below 0.5: print "Status: Approved - Safe"
# Example Input 1: safety_score = 0.85 -> Output: Status: Flagged - Unsafe
# Example Input 2: safety_score = 0.30 -> Output: Status: Approved - Safe
# Concept Tested: if / elif / else, Float comparison
# Difficulty: Easy

safety_score = float(input("Enter a score:"))

if safety_score >=0.8:
    print("status: Flagged - unsafe")
elif safety_score >0.5:
    print("Status: Review Required")
elif safety_score <0.5:
    print("Status: Approved - Safe")

