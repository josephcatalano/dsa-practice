"""big_o_examples.py

A module demonstrating common Big O notation complexities.

Each function illustrates a specific complexity class by modeling an algorithm
and counting the operations it performs relative to the input size 'n'. This
provides a practical look at how algorithm performance scales.

Author: Joseph Catalano
Date: August 19, 2025
"""

from typing import List

N_SMALL = 16
N_LARGE = 1024


def demonstrate_constant_time(items: List[int]) -> None:
    """Demonstrates O(1) - Constant Time.

    An O(1) algorithm's execution time is constant; it does not change with
    the size of the input 'n'.

    Args:
        items: A list of items. The function will access the first element.
    """
    print("## O(1)   - Constant ##")

    operations = 0
    if items:
        _ = items[0]
        operations = 1

    print(f"  Input size (n): {len(items):,}")
    print(f"  Operations: {operations} (Constant regardless of n)")
    print("-" * 30)


def demonstrate_logarithmic_time(n: int) -> None:
    """Demonstrates O(log n) - Logarithmic Time.

    An O(log n) algorithm's execution time grows logarithmically with 'n'.
    This is highly efficient because the operational cost increases very
    slowly as the input size grows. This normally occurs when the problem
    size is halved at each step.

    Args:
        n: The size of the theoretical input.
    """
    print("## O(log n)   - Logarithmic ##")

    operations = 0
    i = 1
    while i < n:
        i *= 2
        operations += 1

    print(f"  Input size (n): {n:,}")
    print(f"  Operations: {operations} (Grows very slowly as n increases)")
    print("-" * 30)


def demonstrate_linear_time(n: int) -> None:
    """Demonstrates O(n) - Linear Time.

    An O(n) algorithm's execution time grows in direct proportion to the
    input size 'n'. If the input doubles, the work doubles.

    Args:
        n: The size of the input.
    """
    print("## O(n)   - Linear ##")

    operations = n
    print(f"  Input size (n): {n:,}")
    print(f"  Operations: {operations:,} (Grows 1-to-1 with n)")
    print("-" * 30)


def demonstrate_quadratic_time(n: int) -> None:
    """Demonstrates O(n^2) - Quadratic Time.

    An O(n^2) algorithm's execution time is proportional to the square of
    the input size. This is common in algorithms that compare every element
    of a collection to every other element (e.g., nested loops).

    Args:
        n: The size of the input.
    """
    print("## O(n^2)   - Quadratic ##")

    operations = 0
    for _ in range(n):
        for _ in range(n):
            operations += 1

    print(f"  Input size (n): {n:,}")
    print(f"  Operations: {operations:,} (Grows quadratically with n)")
    print("-" * 30)


def main():
    """Runs all the Big O demonstration functions with sample inputs."""

    print("--- Big O Notation Examples ---\n")

    small_list = list(range(N_SMALL))
    large_list = list(range(N_LARGE))

    demos = {
        "O(1)   - Constant": lambda: (
            demonstrate_constant_time(small_list),
            demonstrate_constant_time(large_list),
        ),
        "O(log n) - Logarithmic": lambda: (
            demonstrate_logarithmic_time(N_SMALL),
            demonstrate_logarithmic_time(N_LARGE),
        ),
        "O(n)   - Linear": lambda: (
            demonstrate_linear_time(N_SMALL),
            demonstrate_linear_time(N_LARGE),
        ),
        "O(n^2)  - Quadratic": lambda: (
            demonstrate_quadratic_time(N_SMALL),
            print("  (Skipping large input for O(n^2) as it would be 1,048,576 ops)"),
        ),
    }

    for func in demos.values():
        func()


if __name__ == "__main__":
    main()
