**Flashcard #1: Dynamic Array**
1. A dynamic array is an array that is able to change its size automatically when needed.  Where as a normal array has a fixed size.  This essentially turns an array into a list.
2. The key problem a dynamic array solves is that it is able to increase its memory capacity as well as its size whenever needed by performing a _resize operation method.

*Main steps of the _resize operation*
self.capacity *= 2
new_array = self._create_array(self.capacity)
for i in range(self.size):
   new_array[i] = self.elements[i]
self.elements = new_array


**Flashcard #2: Big O Notation**
1. Big O Notation describes how the performance of an algorithm (its time or space requirements) scales as the size of the input grows. It focuses on the rate of growth, not the raw speed in seconds.
2. The 2 main resources it is used to measure are the "Time complexity" & "Space Complexity"

*Function that demonstrates O(n) - Linear Time complexity*
total_operations = 0
for i in range(n):
    total_operations += 1
return total_operations

**Flashcard #3: The Two Pointers Pattern**
1. The Two Pointers pattern is a technique that uses two pointers (indices) to iterate through a data structure, typically an array, in a single pass. The pointers often start at opposite ends and move towards each other, or one moves faster than the other, to solve problems involving pairs or subsequences efficiently.
2. The key precondition for using it to find a pair that sums to a target is that the list must be sorted.

*Core logic for reversing an array in-place using two pointers*
left = 0
right = len(array) -1
while left < right:
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

**Flashcard #4: String Searching**
1. The goal of a string searching algorithm is to find a substring within a string.
2. The time complexity of a simple 'Naive' approach is O(n*m)