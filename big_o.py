"""Examples of Big O Notations in action"""

def o_1():
    """O(1) -Objective: Find the 3rd element in any piece of data"""
    my_array = [1,2,3,4,5,6,7,8,9,10]
    my_array2 = ([1,2,3,4,5,6,7,8,9,10,
                 11,12,13,14,15,16,17,18,19,
                 20,21,22,23,24,25,26,27,28,29,
                 30,31,32,33,34,35,36,37,38,39,40])

    small_data = my_array[2]
    big_data = my_array2[2]
    print(small_data, big_data)
    # no matter how big the array is finding the 3rd element takes the same amount of steps.

def log_n_1(n):
    """O(log n)"""
    count = 0
    i = 1
    while i < n:
        count += 1
        i = i*2
    print(count)
    # 2 pieces of data takes 1 step 57899384843 pieces of data takes 36, a lot better than 1:1

def o_n(n):
    """O(n)"""
    count = 0
    for i in range(0, n):
        count += 1
    print(count)
    #amount of time/work needed to complete the for look depends on size of n 1:1 (data = 1 steps = 1, data = 100000 steps = 100000)


def o_n_squared(n):
    """O(n^2)"""
    for i in range(0, n):
        for j in range(0, n):
            print(i, j, end= ", ")
    # amount of n (data) takes n^2 steps to complete. n = 10, n x n size graph = 100

o_1()
log_n_1(100)
o_n(1000)
o_n_squared(10)
