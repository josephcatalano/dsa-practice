"""big_o_examples.py

A module demonstrating common Big O notation complexities with simple,
illustrative Python functions. Each function counts its primary operations
to show how the workload scales with the input size 'n'.

Author: Joseph Catalano
Date: August 17, 2025
"""

from typing import List

## O(1) - Constant Time

def demonstrate_constant_time(items: List[int]) -> None:
    """Demonstrates O(1) - Constant Time complexity.

    An algorithm is O(1) if the number of operations it performs does not
    change, regardless of the size of the input. Accessing an element by
    its index in an array is the classic example.

    Args:
        items (List[int]): A list of items to operate on.
    """
    operations = 0
    if items:
        operations = 1

    print("O(1) - Constant Time:")
    print(f"  Input size (n): {len(items)}")
    print(f"  Operations: {operations} (This will always be 1 or 0)")
    print("-" * 20)

## O(log n) - Logarithmic Time

def demonstrate_logarithmic_time(n: int) -> None:
    """Demonstrates O(log n) - Logarithmic Time complexity.

    An algorithm is O(log n) if the number of operations grows in proportion
    to the logarithm of the input size. This means the time it takes grows
    very slowly. A common example is repeatedly halving the input size, as
    seen in a binary search.

    Args:
        n (int): The size of the input.
    """
    operations = 0
    i = 1
    while i < n:
        i *= 2
        operations += 1

    print("O(log n) - Logarithmic Time:")
    print(f"  Input size (n): {n}")
    print(f"  Operations: {operations} (Note how slowly this number grows)")
    print("-" * 20)

## O(n) - Linear Time

def demonstrate_linear_time(n: int) -> None:
    """Demonstrates O(n) - Linear Time complexity.

    An algorithm is O(n) if the number of operations grows in a direct,
    1-to-1 relationship with the size of the input. Iterating through
    all elements of a list is the classic example.

    Args:
        n (int): The size of the input.
    """
    operations = 0
    for _ in range(n):
        operations += 1

    print("O(n) - Linear Time:")
    print(f"  Input size (n): {n}")
    print(f"  Operations: {operations} (A direct 1-to-1 relationship)")
    print("-" * 20)

## O(n^2) - Quadratic Time

def demonstrate_quadratic_time(n: int) -> None:
    """Demonstrates O(n^2) - Quadratic Time complexity.

    An algorithm is O(n^2) if the number of operations is proportional to
    the square of the input size. This is common when an operation must be
    performed for every element in combination with every other element,
    such as in a nested loop.

    Args:
        n (int): The size of the input.
    """
    operations = 0
    for _ in range(n):
        for _ in range(n):
            operations += 1

    print("O(n^2) - Quadratic Time:")
    print(f"  Input size (n): {n}")
    print(f"  Operations: {operations} (Grows very quickly: n*n)")
    print("-" * 20)


def main():
    """Runs all the Big O demonstration functions."""
    print("--- Big O Notation Examples ---")

    small_list = [i for i in range(10)]
    large_list = [i for i in range(1000)]
    n_small = 10
    n_large = 1000

    # O(1) Demo
    demonstrate_constant_time(small_list)
    demonstrate_constant_time(large_list)

    # O(log n) Demo
    demonstrate_logarithmic_time(n_small)
    demonstrate_logarithmic_time(n_large)

    # O(n) Demo
    demonstrate_linear_time(n_small)
    demonstrate_linear_time(n_large)

    # O(n^2) Demo
    demonstrate_quadratic_time(n_small)
    # Note: We use a small n here because this grows so fast!
    # demonstrate_quadratic_time(n_large) # This would be 1,000,000 operations!


if __name__ == "__main__":
    main()
