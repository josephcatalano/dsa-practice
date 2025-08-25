"""string_manipulation.py

This module provides simple, efficient functions for common string operations
including reversing a string, checking for palindromes, and counting character
frequency.

Author: Joseph Catalano
Date: August 19, 2025
"""

import time


def reverse_string(s: str) -> str:
    """Reverses a given string.

    Args:
        s: The string to be reversed.

    Returns:
        The string in reverse order.
    """

    return s[::-1]  # start:stop:step


def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """

    return s == s[::-1]


def char_count(s: str) -> dict:
    """Counts the frequency of each character in a string.

    Args:
        s: The string in which to count characters.

    Returns:
        A dictionary-like object where keys are characters and values are
        their frequencies.
    """

    chars = {}

    for character in s:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars


def main():
    """Main function to demonstrate and test the string utility functions."""
    # --- Function Demonstrations ---
    print("--- Function Demonstrations ---")
    print(f"Reversing 'hello': {reverse_string('hello')}")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Character count for 'hello world': {char_count('hello world')}")

    # --- Performance Test ---
    print("\n--- Performance Test ---")
    long_string = "a" * 10_000_000 + "b"  # Using underscores for readability
    print(f"Checking a string with {len(long_string):,} characters.")

    # time.perf_counter() is more precise for measuring short durations
    start_time = time.time()
    is_palindrome(long_string)
    end_time = time.time()

    duration = end_time - start_time
    print(f"Palindrome check took: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
