"""two_pointers.py

This module shows implementations of common problems solved
by using the Two Pointers algorithmic pattern.

Author: Joseph Catalano
Date: August 22, 2025
"""

from typing import List, Any


def reverse_in_place(arr: List[Any]) -> List[Any]:
    """Reverses a list in place using the two-pointers pattern.

    Time Complexity: O(n) - Single pass through half the list.
    Space Complexity: O(1) - No new data structures are created.

    Args:
        arr (List[Any]): The list of items to be reversed.

    Returns:
        List[Any]: The same list object that was passed in, reversed.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def has_pair_with_sum(arr: List[int], target: int) -> bool:
    """Checks for a pair of elements that sum to a target in a sorted list

    Time Complexity: O(n) - Single pass through the list.
    Space Complexity: O(1) - Only two integer pointers are stored.

    Precondition:
        The input list 'arr' must be sorted in ascending order.

    Args:
        arr (List[int]): The sorted list of integers to search.
        target (int): The target sum to find.

    Returns:
        bool: True if a pair is found that sums to the target, False otherwise.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1
    return False


def is_palindrome_two_pointers(s: str) -> bool:
    """Checks if a string is a palindrome using the two-pointers pattern

    Time Complexity: O(n) - Single pass through half the string.
    Space Complexity: O(1) - Only two integer pointers are stored.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    """Defines and runs simple test cases for the implemented functions."""
    print("--- Testing Two Pointers Functions ---")

    # Test reverse_in_place
    list_to_reverse = [1, 2, 3, 4, 5]
    print(f"\nOriginal list: {list_to_reverse}")
    reverse_in_place(list_to_reverse)
    print(f"Reversed list: {list_to_reverse}")

    # Test has_pair_with_sum
    sorted_list = [1, 2, 4, 7, 11, 15]
    target_to_find = 9
    print(
        f"\nDoes {sorted_list} have a pair that sums to {target_to_find}? {has_pair_with_sum(sorted_list, target_to_find)}"
    )

    # Test is_palindrome_two_pointers
    palindrome_str = "racecar"
    print(
        f"\nIs '{palindrome_str}' a palindrome? {is_palindrome_two_pointers(palindrome_str)}"
    )
    non_palindrome_str = "hello"
    print(
        f"Is '{non_palindrome_str}' a palindrome? {is_palindrome_two_pointers(non_palindrome_str)}"
    )


if __name__ == "__main__":
    main()
