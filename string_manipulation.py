"""_"""

import time

def reverse_string(s: str) -> str:
    """_"""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome by comparing it to its reverse"""
    return s == s[::-1]

def char_count(s: str) -> dict:
    """_"""
    chars = {}

    for character in s:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars


def main():
    """_"""
    print(reverse_string("hello"))
    print(is_palindrome("racecar"))
    print(char_count("hello world"))

    # Performance Test
    print("\nStarting Performance Test")

    long_string = "a" * 10000000 + "b"

    start_time = time.time()

    is_palindrome(long_string)

    end_time = time.time()

    duration = end_time - start_time
    print(f"Palindrome check on a long string took: {duration:.6f} seconds")

if __name__ == "__main__":
    main()
