"""
Day 3 - Student Assignment: Loops, List Comprehensions, Functions, and Lambdas
File: day3_tasks.py
Author: Dinesh (Python 30 Days Practice)

This module implements all 6 tasks described in Day 3/Student.md:
- Task 1: Number Guessing Game (while loop practice)
- Task 2: List Comprehensions
- Task 3: Function Basics (area, even check, grading, string reversal, vowel count)
- Task 4: Function with Multiple Returns (analyze_numbers)
- Task 5: Lambda Functions (doubling, positive check, map, filter, sorted)
- Task 6: Combining Concepts (Student Score Processing & Statistics)
"""

import random
import sys
from typing import List, Tuple, Dict, Any, Optional, Union


# ==============================================================================
# TASK 1: while Loop Practice (Number Guessing Game)
# ==============================================================================

def guess_number_game(secret_number: Optional[int] = None) -> int:
    """
    Interactive number guessing game using a while loop.

    Requirements:
    1. Prompts the user to guess a number between 1 and 100.
    2. Keeps asking using a while loop until the correct number is guessed.
    3. Provides hints ("too high" or "too low").
    4. Counts the number of attempts.
    5. Displays a congratulatory message with the total attempt count.

    Args:
        secret_number: Optional fixed number for testing. If None, generates a random integer (1-100).

    Returns:
        int: Total number of attempts taken to guess the secret number.
    """
    if secret_number is None:
        secret_number = random.randint(1, 100)

    attempts = 0
    guessed_correctly = False

    print("\n--- Task 1: Number Guessing Game ---")
    print("I have picked a secret number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        user_input = input("Enter your guess (1-100) or 'quit' to exit: ").strip()

        if user_input.lower() in ("quit", "exit", "q"):
            print(f"Game cancelled. The secret number was: {secret_number}")
            return attempts

        # Input validation
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if guess < 1 or guess > 100:
            print("Out of range! Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print(f"Attempt {attempts}: Too low! Try a higher number.")
        elif guess > secret_number:
            print(f"Attempt {attempts}: Too high! Try a lower number.")
        else:
            guessed_correctly = True
            print("=" * 50)
            print(f"Congratulations! You guessed the secret number {secret_number}!")
            print(f"Total attempts: {attempts}")
            print("=" * 50)

    return attempts


# ==============================================================================
# TASK 2: List Comprehensions
# ==============================================================================

def task2_list_comprehensions(numbers: Optional[List[int]] = None) -> Dict[str, Any]:
    """
    Demonstrates list comprehensions on a list of numbers.

    Given list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Creates:
    1. Squares of all numbers
    2. Even numbers only
    3. Numbers greater than 5, each multiplied by 2
    4. String representations of each number
    5. Tuples of (number, square)

    Args:
        numbers: List of integers (defaults to 1 to 10 if None).

    Returns:
        Dict[str, Any]: Dictionary containing all transformed lists.
    """
    if numbers is None:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 1. A list of squares
    squares = [x ** 2 for x in numbers]

    # 2. A list of even numbers only
    evens = [x for x in numbers if x % 2 == 0]

    # 3. Numbers greater than 5, each multiplied by 2
    greater_than_5_doubled = [x * 2 for x in numbers if x > 5]

    # 4. A list of strings
    string_numbers = [str(x) for x in numbers]

    # 5. A list of tuples: (number, square)
    number_square_tuples = [(x, x ** 2) for x in numbers]

    print("\n--- Task 2: List Comprehensions ---")
    print(f"Original list:                    {numbers}")
    print(f"1. Squares:                       {squares}")
    print(f"2. Even numbers only:             {evens}")
    print(f"3. Numbers > 5 multiplied by 2:   {greater_than_5_doubled}")
    print(f"4. List of strings:               {string_numbers}")
    print(f"5. Tuples (number, square):       {number_square_tuples}")

    return {
        "original": numbers,
        "squares": squares,
        "evens": evens,
        "greater_than_5_doubled": greater_than_5_doubled,
        "string_numbers": string_numbers,
        "number_square_tuples": number_square_tuples,
    }


# ==============================================================================
# TASK 3: Function Basics
# ==============================================================================

def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle (non-negative).
        width: The width of the rectangle (non-negative).

    Returns:
        float: Area of the rectangle.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return float(length * width)


def is_even(number: int) -> bool:
    """
    Checks if a number is even.

    Args:
        number: The integer to test.

    Returns:
        bool: True if even, False otherwise.
    """
    return number % 2 == 0


def get_grade(score: float) -> str:
    """
    Returns the letter grade (A-F) based on a numeric score (0-100).

    Grading scale:
        90 - 100 : A
        80 - 89  : B
        70 - 79  : C
        60 - 69  : D
        0  - 59  : F

    Args:
        score: Numeric score between 0 and 100.

    Returns:
        str: Letter grade corresponding to the score.
    """
    if score < 0 or score > 100:
        raise ValueError(f"Score {score} is out of valid range (0-100).")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def reverse_string(text: str) -> str:
    """
    Reverses the given text string.

    Args:
        text: The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (A, E, I, O, U) in the given text string.

    Args:
        text: Input string.

    Returns:
        int: Total number of vowels found.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


def task3_function_basics() -> None:
    """
    Demonstrates and tests all 5 functions defined in Task 3.
    """
    print("\n--- Task 3: Function Basics ---")

    # 1. calculate_area tests
    print("1. calculate_area:")
    area1 = calculate_area(10, 5)
    area2 = calculate_area(7.5, 4.2)
    print(f"   calculate_area(10, 5)     -> {area1}")
    print(f"   calculate_area(7.5, 4.2)  -> {area2:.2f}")

    # 2. is_even tests
    print("\n2. is_even:")
    for num in [4, 7, 0, -2, 13]:
        print(f"   is_even({num:2d}) -> {is_even(num)}")

    # 3. get_grade tests
    print("\n3. get_grade:")
    for score in [98, 85, 73, 62, 45, 90, 80, 59]:
        print(f"   get_grade({score:2d}) -> {get_grade(score)}")

    # 4. reverse_string tests
    print("\n4. reverse_string:")
    for word in ["Python", "OpenAI", "radar", "Generative AI"]:
        print(f"   reverse_string('{word}') -> '{reverse_string(word)}'")

    # 5. count_vowels tests
    print("\n5. count_vowels:")
    for phrase in ["Hello World", "Artificial Intelligence", "rhythm", "AEIOU"]:
        print(f"   count_vowels('{phrase}') -> {count_vowels(phrase)}")


# ==============================================================================
# TASK 4: Function with Multiple Returns
# ==============================================================================

def analyze_numbers(numbers: List[Union[int, float]]) -> Optional[Dict[str, Any]]:
    """
    Analyzes a list of numbers and returns key statistical metrics.

    Args:
        numbers: List of numeric values (ints or floats).

    Returns:
        dict: A dictionary containing:
            - "sum": sum of all numbers
            - "average": average of numbers
            - "max": maximum value
            - "min": minimum value
            - "count": number of items
            - "evens": count of even numbers (for integers)
            - "odds": count of odd numbers (for integers)
        None: If numbers list is empty.
    """
    if not numbers:
        return None

    total_sum = sum(numbers)
    count = len(numbers)
    avg = total_sum / count
    max_val = max(numbers)
    min_val = min(numbers)

    # Count evens and odds for integer values
    evens_count = sum(1 for n in numbers if isinstance(n, int) and n % 2 == 0)
    odds_count = sum(1 for n in numbers if isinstance(n, int) and n % 2 != 0)

    return {
        "sum": total_sum,
        "average": avg,
        "max": max_val,
        "min": min_val,
        "count": count,
        "evens": evens_count,
        "odds": odds_count,
    }


def task4_analyze_numbers() -> Dict[str, Any]:
    """
    Demonstrates Task 4 using the assignment test list:
    [12, 45, 8, 23, 56, 9, 34, 67, 3, 91]
    """
    test_list = [12, 45, 8, 23, 56, 9, 34, 67, 3, 91]
    result = analyze_numbers(test_list)

    print("\n--- Task 4: Function with Multiple Returns ---")
    print(f"Input numbers: {test_list}")
    print("Analysis results:")
    if result:
        for key, value in result.items():
            if isinstance(value, float):
                print(f"  - {key:<8}: {value:.2f}")
            else:
                print(f"  - {key:<8}: {value}")

    return result or {}


# ==============================================================================
# TASK 5: Lambda Functions
# ==============================================================================

def task5_lambda_functions() -> Dict[str, Any]:
    """
    Demonstrates usage of lambda functions:
    1. Lambda to double a number
    2. Lambda to check if a number is positive
    3. map() with lambda on [1, 2, 3, 4, 5]
    4. filter() with lambda on [-2, -1, 0, 1, 2, 3]
    5. sorted() with lambda to sort strings by length
    """
    # 1. Lambda that doubles a number
    double = lambda x: x * 2

    # 2. Lambda that checks if a number is positive
    is_positive = lambda x: x > 0

    # 3. map() with lambda to convert [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10]
    nums1 = [1, 2, 3, 4, 5]
    doubled_list = list(map(lambda x: x * 2, nums1))

    # 4. filter() with lambda to get only positive numbers from [-2, -1, 0, 1, 2, 3]
    nums2 = [-2, -1, 0, 1, 2, 3]
    positives = list(filter(lambda x: x > 0, nums2))

    # 5. sorted() with lambda to sort ["apple", "banana", "cherry"] by length
    fruits = ["apple", "banana", "cherry"]
    sorted_by_length = sorted(fruits, key=lambda s: len(s))

    # Additional demonstration with mixed lengths
    more_fruits = ["watermelon", "fig", "banana", "kiwi", "apple"]
    sorted_more = sorted(more_fruits, key=lambda s: len(s))

    print("\n--- Task 5: Lambda Functions ---")
    print(f"1. Double lambda test (7 * 2):       {double(7)}")
    print(f"2. Positive lambda test:              is_positive(5) -> {is_positive(5)}, is_positive(-3) -> {is_positive(-3)}")
    print(f"3. map() to double [1, 2, 3, 4, 5]:  {doubled_list}")
    print(f"4. filter() positive numbers:        {positives}")
    print(f"5. sorted() by length (fruits):      {sorted_by_length}")
    print(f"   sorted() by length (extra test):  {sorted_more}")

    return {
        "doubled_sample": double(7),
        "doubled_list": doubled_list,
        "positive_list": positives,
        "sorted_fruits": sorted_by_length,
    }


# ==============================================================================
# TASK 6: Combining Concepts (Student Score Processor & Mini Project)
# ==============================================================================

def process_scores(scores: List[float]) -> List[Tuple[float, str]]:
    """
    Processes a list of scores (0-100) and returns a list of tuples containing (score, grade).

    Uses list comprehension to determine letter grades.

    Args:
        scores: List of numeric scores between 0 and 100.

    Returns:
        List[Tuple[float, str]]: List of (score, letter_grade) tuples.
    """
    # Uses list comprehension to calculate letter grades
    return [(score, get_grade(score)) for score in scores]


def task6_combining_concepts(interactive: bool = True, sample_scores: Optional[List[float]] = None) -> None:
    """
    Task 6 / Mini Project: Student Score Management System.

    Workflow:
    1. Collects scores from user using a while loop until they type "done".
    2. Validates that scores are between 0-100.
    3. Calls process_scores() to compute grades using list comprehension.
    4. Uses lambda to find the highest score.
    5. Displays complete statistics (average, max, min, score-to-grade mapping).

    Args:
        interactive: If True, asks for input from stdin. If False, uses sample_scores.
        sample_scores: Optional fallback list of scores when not interactive.
    """
    print("\n" + "=" * 60)
    print("   TASK 6: COMBINING CONCEPTS (STUDENT SCORE PROCESSOR)   ")
    print("=" * 60)

    scores: List[float] = []

    if interactive:
        print("Enter student scores (0-100). Type 'done' when finished:\n")
        while True:
            entry = input("Enter score (or 'done'): ").strip()
            if entry.lower() == "done":
                break

            try:
                score = float(entry)
            except ValueError:
                print("[!] Invalid input! Please enter a numeric score or 'done'.")
                continue

            if 0 <= score <= 100:
                scores.append(score)
                print(f"   [+] Added score: {score}")
            else:
                print(f"[!] Score {score} is invalid! Must be between 0 and 100.")
    else:
        # Non-interactive mode using sample data
        scores = sample_scores if sample_scores is not None else [95.0, 82.5, 67.0, 45.0, 88.0, 73.5, 91.0]
        print(f"Running in automated mode with sample scores: {scores}")

    if not scores:
        print("\n[!] No valid scores were entered. Task complete.")
        return

    # Process scores with list comprehension
    graded_scores = process_scores(scores)

    # Use lambda to identify the highest score tuple
    highest_entry = max(graded_scores, key=lambda item: item[0])

    # Calculate statistics
    total = sum(scores)
    average = total / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    # Display results cleanly
    print("\n" + "-" * 40)
    print("STUDENT SCORE REPORT")
    print("-" * 40)
    print(f"{'#':<4}{'Score':<10}{'Grade':<6}")
    print("-" * 25)
    for idx, (score, grade) in enumerate(graded_scores, start=1):
        print(f"{idx:<4}{score:<10.1f}{grade:<6}")

    print("\n" + "-" * 40)
    print("STATISTICAL SUMMARY")
    print("-" * 40)
    print(f"* Total Students Processed: {len(scores)}")
    print(f"* Class Average:           {average:.2f}")
    print(f"* Maximum Score:           {max_score:.1f} (Grade: {highest_entry[1]})")
    print(f"* Minimum Score:           {min_score:.1f}")
    print(f"* Highest Student Record:  Score: {highest_entry[0]}, Grade: {highest_entry[1]} (Found using lambda)")
    print("=" * 60)


# ==============================================================================
# MAIN RUNNER & MENU
# ==============================================================================

def run_all_tasks(interactive: bool = False) -> None:
    """
    Runs all tasks 1 through 6 sequentially.

    Args:
        interactive: If True, prompts for user input in Tasks 1 and 6.
                     If False, runs automated demonstrations.
    """
    print("==================================================")
    print("  RUNNING ALL DAY 3 TASKS & ASSIGNMENTS")
    print("==================================================")

    # Task 1
    if interactive:
        guess_number_game()
    else:
        print("\n--- Task 1: Number Guessing Game (Automated Demonstration) ---")
        secret = random.randint(1, 100)
        print(f"[Automated Demo] Secret number picked: {secret}")
        print("Simulating binary search guesses:")
        low, high = 1, 100
        demo_attempts = 0
        while low <= high:
            demo_attempts += 1
            mid = (low + high) // 2
            print(f"  Attempt {demo_attempts}: Guess {mid} -> ", end="")
            if mid == secret:
                print("Correct!")
                break
            elif mid < secret:
                print("Too low!")
                low = mid + 1
            else:
                print("Too high!")
                high = mid - 1
        print(f"Guessed secret {secret} in {demo_attempts} attempts.")

    # Task 2
    task2_list_comprehensions()

    # Task 3
    task3_function_basics()

    # Task 4
    task4_analyze_numbers()

    # Task 5
    task5_lambda_functions()

    # Task 6
    task6_combining_concepts(interactive=interactive)

    print("\n[SUCCESS] All 6 tasks have been successfully executed!")


def main() -> None:
    """
    Main entry point with interactive command-line menu.
    Allows testing individual tasks or running all tasks together.
    """
    # Check for CLI arguments (e.g., `python day3_tasks.py --test` or `python day3_tasks.py 2`)
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower().strip("-")
        if arg in ("test", "demo", "all-auto"):
            run_all_tasks(interactive=False)
            return
        elif arg in ("all", "run-all"):
            run_all_tasks(interactive=True)
            return
        elif arg == "1":
            guess_number_game()
            return
        elif arg == "2":
            task2_list_comprehensions()
            return
        elif arg == "3":
            task3_function_basics()
            return
        elif arg == "4":
            task4_analyze_numbers()
            return
        elif arg == "5":
            task5_lambda_functions()
            return
        elif arg == "6":
            task6_combining_concepts(interactive=True)
            return
        elif arg in ("h", "help"):
            print("Usage: python day3_tasks.py [1|2|3|4|5|6|all|demo]")
            return

    # Interactive Menu
    while True:
        print("\n" + "=" * 52)
        print("          DAY 3: PYTHON PRACTICE TASKS              ")
        print("=" * 52)
        print("1. Task 1: Number Guessing Game (while loop)")
        print("2. Task 2: List Comprehensions")
        print("3. Task 3: Function Basics")
        print("4. Task 4: Function with Multiple Returns")
        print("5. Task 5: Lambda Functions")
        print("6. Task 6: Combining Concepts (Score Processor)")
        print("7. Run All Tasks (Interactive)")
        print("8. Run All Tasks (Automated Demo)")
        print("0. Exit")
        print("=" * 52)

        choice = input("Enter choice (0-8): ").strip()

        if choice == "1":
            guess_number_game()
        elif choice == "2":
            task2_list_comprehensions()
        elif choice == "3":
            task3_function_basics()
        elif choice == "4":
            task4_analyze_numbers()
        elif choice == "5":
            task5_lambda_functions()
        elif choice == "6":
            task6_combining_concepts(interactive=True)
        elif choice == "7":
            run_all_tasks(interactive=True)
        elif choice == "8":
            run_all_tasks(interactive=False)
        elif choice in ("0", "exit", "quit", "q"):
            print("Goodbye! Happy coding!")
            break
        else:
            print("Invalid choice! Please select 0 through 8.")


if __name__ == "__main__":
    main()
