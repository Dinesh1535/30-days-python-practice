# Question 9: Chat Logger (Append Mode)
# Problem Statement: Write a function log_chat_message(filename, role, message) that opens chat_log.txt in append mode ("a"), writes a new line in the format "[ROLE]: MESSAGE\n", and closes the file cleanly using with.
# Call the function twice (once with "USER" and once with "AI").
# Then read and print the entire file content.
# Example Output in file:
# text
# [USER]: Hello AI!
# [AI]: Hello! How can I assist you today?
# Concept Tested: File append mode ("a"), Function parameters, File I/O
# Difficulty: Beginner+

def log_chat_message(filename, role, message):
    """Appends a formatted chat message to the specified file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"[{role}]: {message}\n")


# 1. Call the function twice
log_chat_message("chat_log.txt", "USER", "Hello AI!")
log_chat_message("chat_log.txt", "AI", "Hello! How can I assist you today?")

# 2. Read and print the entire file content
with open("chat_log.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)