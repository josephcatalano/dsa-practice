"""valid_palindrome.py

This Module provides the Valid Palindrome LeetCode solution.

Author: Joseph Catalano
Date: August 22, 2025
"""

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome after cleaning it.
    
    Args:
        s (str): The input string, which can include punctuation and mixed case.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise
    """

    cleaned_chars = []
    for char in s:
        if char.isalnum():
            cleaned_chars.append(char.lower())

    cleaned_s = "".join(cleaned_chars)

    left = 0
    right = len(cleaned_s) - 1

    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1

    return True


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
