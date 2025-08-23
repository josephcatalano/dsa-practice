"""valid_palindrome.py

This Module provides the Valid Palindrome LeetCode solution.

Author: Joseph Catalano
Date: August 22, 2025
"""

def is_palindrome(s: str) -> str:
    """Checks if a string is a palindrome after cleaning it.
    
    Args:
        s (str): The input string, which can include punctuation and mixed case.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise
    """

    new_string = []

    for i in s:
        if i.isalnum():
            new_string.append(i.lower())

    if new_string == new_string[::-1]:
        return True

    return False


def main():
    """Defines and runs test cases for the is_palindrome function."""

    test_cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "Hello World",
        "12321",
        "Was it a car or a cat I saw?",
    ]

    for case in test_cases:
        result = is_palindrome(case)
        print(f"\nInput: '{case}'")
        print(f"Is it a palindrome? -> {result}")

if __name__ == "__main__":
    main()
