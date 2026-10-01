# Problem Statement: Given a potentially corrupted JSON string from an API: corrupt_data = '{"status": "ok", "result": ' (missing closing bracket). Write a function safe_parse_json(text) that tries to parse it with json.loads(). If a json.JSONDecodeError occurs, catch it and return an empty dictionary {} instead of crashing.
# Example Input: corrupt_data = '{"status": "ok", "result": '
# Example Output: {}
# Concept Tested: try...except json.JSONDecodeError, Return fallback value
# Difficulty: Easy

import json

corrupt_data = '{"status": "ok", "result": '


def safe_parse_json(text):
    """Parses a JSON string and returns an empty dictionary if decoding fails."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


# Test with the corrupted JSON string
parsed_result = safe_parse_json(corrupt_data)
print(parsed_result)