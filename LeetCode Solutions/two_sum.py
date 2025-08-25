"""two_sums.py

This module provides the Two Sum LeetCode solution.

Author: Joseph Catalano
Date August 22, 2025
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Finds the indices of two numbers in a list that add up to a target. (Hash Map)

    Time Complexity: O(n) - Single pass through the input list.
    Space Complexity: O(n) - In the worst case, the hash map stores all n elements.

    Args:
        nums (List[int]): A list of integers to search through.
        target (int): The integer value of the target sum.

    Returns:
        List[int]: A list containing the two indices of the numbers that add up to the target.
    """

    num_to_index_map = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index_map:
            return [index, num_to_index_map[complement]]

        else:
            num_to_index_map[num] = index

    return []


def main():
    """Test Cases for Validation"""

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
