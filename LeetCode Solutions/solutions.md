## [Two Sum](https://leetcode.com/problems/two-sum/)

This solution achieves O(n) time complexity by using a hash map.  This avoids a nested loop (O(n^2)), by storing the value and index of each number as we iterate through the list. For each number, we calculate its required complement.  If the complement is already in the hash map, we have found our solution.  If not, we add the current number and its index to the map.

def two_sum(nums: List[int], target: int) -> List[int]:

    value_map = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in value_map:
            return [index, value_map[complement]]

        else:
            value_map[num] = index

Time Complexity: O(n) - We iterate through the list of n elements one time.

Space Complexity: O(n) - In the worst case, we store all n elements in the hash map.


## [Valid Palindrome](https://https://leetcode.com/problems/valid-palindrome/)

This solution achieves O(n) time complexity by iterating through s exactly one time

def is_palindrome(s: str) -> bool:

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

Time Complexity: O(n) - We iterate through the string of n elements one time.

Space Complexity: O(n) - In the worst case, we store all n elements in the new_string variable.