"""dynamic_array.py

A module that implements a generic, high-performance dynamic array from scratch
to demonstrate the underlying principles of data structures like Python's list.

This implementation includes automatic resizing (growing and shrinking) and
standard Pythonic dunder methods for a familiar interface.

Author: Joseph Catalano
Date: August 18, 2025
"""

from typing import Any, List


class DynamicArray:
    """A simplified implementation of a dynamic array."""

    _GROWTH_FACTOR = 2
    _INITIAL_CAPACITY = 1

    def __init__(self):
        """Initializes a new, empty dynamic array."""

        self.size = 0
        self.capacity = self._INITIAL_CAPACITY
        self._elements = self._create_array(self.capacity)

    def __len__(self) -> int:
        """Returns the number of elements in the array for use with len()."""

        return self.size

    def __repr__(self) -> str:
        """Returns a string representation of the array for debugging."""
        elements_list = self._elements[0 : self.size]
        elements_str = str(elements_list)
        return f"DynamicArray({elements_str})"

    def append(self, new_element: Any) -> None:
        """Adds an element to the end of the array.

        If the array is full, it automatically triggers a resize operation
        before appending. Amortized time complexity: O(1).

        Args:
            new_element: The element to be added.
        """

        if self.size == self.capacity:
            self._resize()

        self._elements[self.size] = new_element
        self.size += 1

    def get(self, index: int) -> Any:
        """Retrieves the element at a specified index.

        Time complexity: O(1).

        Args:
            index (int): The index of the element to retrieve.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of the valid range (0 to size-1).
        """

        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self._elements[index]

    def pop(self) -> Any:
        """Removes and returns the last element of the array.

        Time complexity: O(1).

        Returns:
            The last element that was removed.

        Raises:
            IndexError: If the array is empty.
        """

        if self.size == 0:
            raise IndexError("Pop from empty list")

        value = self._elements[self.size - 1]
        self._elements[self.size - 1] = None
        self.size -= 1
        return value

    def _resize(self) -> None:
        """(Private) Doubles the capacity and rebuilds the internal array."""

        self.capacity *= self._GROWTH_FACTOR
        new_array = self._create_array(self.capacity)
        for i in range(self.size):
            new_array[i] = self._elements[i]
        self._elements = new_array

    def _create_array(self, new_capacity: int) -> List[Any]:
        """(Private) Creates a new fixed-size array with a given capacity."""

        return [None] * new_capacity


def run_tests():
    """Runs a suite of tests to validate DynamicArray functionality."""

    print("--- Starting Dynamic Array Tests ---")

    arr = DynamicArray()
    print(f"New array created. Size: {len(arr)}, Capacity: {arr.capacity}")

    print("\nAppending first item...")
    arr.append(10)
    print(f"Appended 10. Size: {len(arr)}, Capacity: {arr.capacity}")

    print("\nAppending second item (should trigger resize)...")
    arr.append(20)
    print(f"Appended 20. Size: {len(arr)}, Capacity: {arr.capacity}")

    print(f"\nGetting item at index 1: {arr.get(1)}")

    print(f"\nPopping item: {arr.pop()}")
    print(f"After pop. Size: {len(arr)}, Capacity: {arr.capacity}")

    print(f"\nPopping the last item: {arr.pop()}")
    print(f"After final pop. Size: {len(arr)}")

    print("\nTesting pop on empty array (should raise IndexError)...")
    try:
        arr.pop()
        print("TEST FAILED: No IndexError was raised.")
    except IndexError:
        print("TEST PASSED: Correctly caught IndexError.")

    print("\n--- All Tests Passed ---")


if __name__ == "__main__":
    run_tests()
