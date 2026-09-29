# Question 9: Prompt Template Builder Function
# Problem Statement: Write a reusable function called make_prompt(role, topic). It should take two string arguments and return a single formatted prompt string: "Act as an expert [role]. Explain [topic] in 2 simple sentences."
# Example Input: make_prompt("Data Scientist", "Neural Networks")
# Example Output: "Act as an expert Data Scientist. Explain Neural Networks in 2 simple sentences."
# Concept Tested: def keyword, Parameters, return statement, f-string
# Difficulty: Beginner

def make_prompt(role, topic):
    return f"Act as an expert {role}. Explain {topic} in 2 simple"
print(make_prompt("Data Scientist","Neural Networks"))
