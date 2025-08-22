"""two_pointers.py

This module shows implementations of common problems solved 
by using the Two Pointers algorithmic pattern.

Author: Joseph Catalano
Date: August 22, 2025
"""

from typing import List

def reverse_in_place(arr: List[any]) -> List:
    """Reverses a list in place using the two-pointers pattern.
    
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

def two_sum(nums: List[int], target: int) -> List[int]:
    """Finds the indices of two numbers in a list that add up to a target. (Hash Map)

    Args:
        nums (List[int]): A list of integers to search through.
        target (int): The integer value of the target sum.

    Returns:
        List[int]: A list containing the two indices of the numbers that add up to the target.
    """

    value_map = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in value_map:
            return [index, value_map[complement]]

        else:
            value_map[num] = index

def main():
    """Defines and runs simple test cases for the implemented functions."""

    print("\n--- Testing Reverse in Place Function ---")
    # Test reverse_in_place
    list_to_reverse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original list: {list_to_reverse}")
    reversed_list = reverse_in_place(list_to_reverse)
    print(f"Reversed list: {reversed_list}")

    print("\n--- Testing Pair With Sum Function ---")
    # Test has_pair_with_sum
    sorted_list = [1, 2, 4, 7, 11, 15]
    target_to_find = 9
    has_pair = has_pair_with_sum(sorted_list, target_to_find)
    print(
        f"Does the list {sorted_list} have a pair that sums to {target_to_find}? {has_pair}"
    )

    target_to_miss = 20
    has_pair = has_pair_with_sum(sorted_list, target_to_miss)
    print(
        f"Does the list {sorted_list} have a pair that sums to {target_to_miss}? {has_pair}"
    )

    # Test is_palindrome_two_pointers
    print("\n--- Testing Is Palindrome Function ---")

    palindrome_str = "racecar"
    is_pal = is_palindrome_two_pointers(palindrome_str)
    print(f"Is '{palindrome_str}' a palindrome? {is_pal}")

    non_palindrome_str = "hello"
    is_pal = is_palindrome_two_pointers(non_palindrome_str)
    print(f"Is '{non_palindrome_str}' a palindrome? {is_pal}")

    # --- Test Cases for two_sum ---
    print("\n--- Testing Two Sum Function ---")

    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")

    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")

    nums3 = [-3, 4, 3, 90]
    target3 = 0
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")

if __name__ == "__main__":
    main()
