**Aug 17 2025**

*BIG O NOTATION (How code slows as data grows)*
    - Formal way to describe how the resources required by an algorithm are affected by the size of its input. 
    - Big O doesn't measure performance in seconds but measures the Rate Of Growth of the number of operations.
    - Big O answers the question "As the input to my algorithm gets bigger, how much longer will it take to run?"

    O(1) - Constant Time
        - The amount of data does not matter algorithm will be completed in the same amount of steps
        EX. "Get me the 3rd item in the list" (my_list[2]), doesn't matter how big the list is the amount of work stayed constant
    
    O(log n) - Logarithmic Time
        - As the amount of data increases the amount of steps increases but by a less amount as the data increases (more data there is more efficient it becomes)
        Ex. binary search

    O(n) - Linear Time
        - As the amount of data increases the amount of steps increase by the amount of data (n).
        Ex. a four loop that iterates over 10 numbers in a list vs a four loop that iterates over 1000000 numbers in a list

    O(n log n) - Quasilinear Time
        - As the amount of data increases the amount increases but by a larger amount as the data increase (more data there is less efficient it becomes)
        Ex. Quicksort, Mergesort, Heapsort

    O(n^2) - Quadratic Time
        - As the amount of data increases the number of steps increases by n*n operations. 1 operation for 1 item, 4 operations for 2 items, 9 operations for 3 items. 
        Ex. Intersection sort, Selection sort, Bubblesort

    O(n!) - Factorial Time
        - As the amount of data increases the number of steps increases by a factorial of the amount of data. (VERY INEFFICIENT AND SLOW)
        Ex. 5! = 5 * 4 * 3 * 2 * 1 = 120
            3! = 3 * 2 * 1 = 6
            1! = 1

    Big O tells you the "worst-case" scenario, like the longest it could possibly take.
    Big Omega tells you the "best-case" scenario, like the shortest it could possibly take.
    Big Theta tells you the "average-case" scenario, giving you a good idea of how it will usually perform. 

**AUGUST 18 2025**

*Arrays & Dynamic Arrays*
    - An array stores a collection of elements in contiguous which means elements are stored one after another in a single, unbroken block of mem.
    Ex of Contiguous Memory:
        - A row of houses on a street that are all built right next to each other.  If you know the address of the first house and you want to get to the 5th house, you can instantly calculate where it is. You don't have to visit houses 1 through 4 to find it.
    - Contiguous layout is the reason why accessing an element by its index is O(1) (Constant Time). The computer knows the starting address in memory and the size of each element, it can do a simple calculation (start_address + index * element_size) to jump to any element in one calculation.

    What happens when you want to insert an element at the beginning of an array?
        - Every element must shift one position to the right to make space for the new one.
        - This means the time complexity of insertion for an array is O(n) (Linear Time).
        - The amount of work required to insert an element grows in a direct, linear relationship with the number of items in the array.
    
    The Limit of a Fixed-Size Array
        - Fast O(1) reads, but slow O(n) insertions.
        - They are created with a fixed size.
    - What happens when you have an array size 10 and its full and you try to add an 11th element? (Overflow Error)

    The Dynamic Array (List)
        - An array that automatically grows itself when it runs out of space.
        - Under the hood, its just a regular array but with some extra space reserved at the end.
        - When you "append" an item and the array if full, Python performs a resize:
          - It creates a new, bigger array in memory (usually about double the size of the old one)
          - It copies all of the elements from the old, full array over to the new, bigger one.
          - It adds your new element at the end.
          - Finally, it deletes the old array
    - If there are n elements in the full array at the moment it needs to be resized, what is the Big O time complexity of that one specific "append" operation? (O(n))
    
    The Append Puzzle
        - Most of the time: append is fast and just placed the new item into one of the empty reserved slots (O(1))
        - Once in a while: append is very slow, as it triggers the O(n) resize and copy operation.
    - If someone asks for the Big O complexity of append, whats the correct answer? Is it O(1) or O(n)?

    Amortized Time
        - Since the O(n) resize happens so rarely compared to the O(1) operations, it becomes insignificant.
        - For this reason the complexity of a append on a dynamic array is described as amortized O(1).

    | Operation                  | Big O Notation     | Reasoning                                                   |
    | -------------------------- | :----------------: | ----------------------------------------------------------- |
    | Access (by index)          |        O(1)        | Direct memory calculation due to contiguous layout.         |
    | Search (by value)          |        O(n)        | Must check every element in the worst case.                 |
    | Insertion (at start/middle)|        O(n)        | Must shift all subsequent elements to make space.           |
    | Deletion (at start/middle) |        O(n)        | Must shift all subsequent elements to close the gap.        |
    | Append (add to end)        | `Amortized O(1)`   | Usually O(1), but occasionally O(n) when resizing is needed.|

    Build your own dynamic array
        - When creating a class to represent your array the two most important numbers you need to keep track of as internal variables are:
          - Size: The number of elements you are currently storing in the array. This is what a user of your class would consider its "length".
          - Capacity: The total number of slots the underlying array has available before it needs to be resized.
    
        The __init__ Method
          - When you initialize an empty dynamic array, size and capacity should be 0.
            The Zero-Capacity Edge Case
              - If you initialize an array with a capacity of 0, what happens when you append the first element?
              - The array would have to perform a resize.
              - To avoid this many real-world implementations actually start with a small default capacity, like 4 or 8 as minor optimization.
        
        The append Method
            - The first check that needs to happen is to compare the two variables (size and capacity) to decide if it has enough room or if it needs to perform the resize operation.
              - If they are equal, the array is full, we must trigger the resize operation
              - If they are not equal, there's empty space, and we can simply add the new element.
  
*Strings and Immutability*
    - Strings in python are immutable, this means once a string is created, it can never be changed in place.
    - How to "Change" a string
        my_string = "hello"
        new_string = "H" + my_string[1:]
    
    String Searching
        - The goal is to find all occurrences of a smaller string (pattern) within a larger string (text)
        - The goal is simple the real challenge is to do it efficiently
  
        The "Naive" Approach OR The "Sliding Window" Approach
          - This is the most basic algorithm
          - Suppose you have the text [ABABC] and you're searching for the patter [ABC].
          - Naive starts at the first character of the text and asks "Does the pattern [ABC] start here?
          - If not the algorithm moves its starting position (window) one character to the right and tries again
          - Time complexity of this is O(n*m) n = starting position (window), m = characters

        Knuth-Morris-Pratt (KMP) Algorithm
            - Ex. Text: ABCABCABD
                Pattern:   ABCABD
                - Sliding Window would start at index 0 and match [ABCAB] then fail on the cast character (C vs D)
                - KMP algorithm is smart enough to know that after seeing [ABCAB] then failing, theres no possible way a match could start at index 1, 2, or 3.
                - It uses a pre-computed table to know it can safely jump its window all the way to index 3 to continue the search.
                - This is what makes it much faster, often approaching O(n) time.

**AUGUST 22 2025**

*The Two Pointers Pattern*
    - Involves using two separate pointers (var holding array indices) that move through an array until they meet or satisfy a condition.
    - Allows you to process the array in a single pass rather than a nested loop.
    - Time complexity for a nested loop = O(n^2)

    Two Pointers Logic
        - For a sorted array:
          - current_sum = array[left] + array[right]
          - if current sum is less than the target value move the right pointer to the right
          - if current sum is more that the target value move the left pointer to the left
          - while left < right
          - left, right = right, left
          - left++, right--

    Value-to-Index Mapping
        - By using a dictionary to map values to indicies, you can find the index of any value in O(1) time.
        - value -> inde map can solve the problem in a single pass.
        - Create empty dictionary, loop through input (nums), and for each element you ask "Is the number i need to complete the pair already in my dictionary?"
        - y = target - x
          - Check if the complement (target - x) is already in the dictionary. (you do this in case for ex.
          - nums = [3,5,2] and target = 6)
          - Add the current number x and its index i to the dictionary
