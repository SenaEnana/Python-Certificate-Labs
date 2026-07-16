# Implement the Selection Sort Algorithm
# Selection sort is another popular sorting algorithm taught in most computer science courses.

# This algorithm works by repeatedly finding the smallest element from the unsorted portion of 
# the list and swapping it with the first unsorted element. 
# It begins by selecting the minimum value in the entire list and swapping it with the first element. 
# Then it moves to the second position, finds the smallest value in the remaining unsorted elements, and swaps it with the second element. 
# This process continues, moving through the list one element at a time, until the entire list is sorted.

# Selection sort results in a quadratic time complexity in the best, 
# average, and worst case scenarios. The space complexity will be constant O(1) 
# because the sorting is done in place and a constant amount of memory is being used regardless of the size of the list.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named selection_sort.
# Your selection_sort function should have one parameter that represents the list of items.
# Your selection_sort function should take a list and sort the items in place from smallest to largest.
# Your selection_sort function should modify the input list in-place, and return it once it's sorted.
# Your selection_sort function should follow the selection sort algorithm, swapping the smallest element from the unsorted portion of the list with the first unsorted element.
# Your selection_sort function should not perform unnecessary swaps when the smallest element is already in the correct position.
# Your selection_sort function should not use either the built-in sort() method or sorted() function.
# Tests:
# Waiting:1. You should have a function named selection_sort.
# Waiting:2. Your selection_sort function should have one parameter.
# Waiting:3. You should not import any module or use built-in sorting methods in your code.
# Waiting:4. Your selection_sort should return the same list as the input list.
# Waiting:5. Your selection_sort should modify the input list in-place. You should not use any method adding, or removing items from the list.
# Waiting:6. Your selection_sort function should follow the selection sort algorithm, swapping the minimum value in the unsorted part of the list with the first unsorted element. Avoid unnecessary swaps when the minimum value is already in the correct position.
# Waiting:7. selection_sort([33, 1, 89, 2, 67, 245]) should return [1, 2, 33, 67, 89, 245].
# Waiting:8. selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]) should return [3, 5, 12, 15, 16, 23, 72, 99, 567].
# Waiting:9. selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]) should return [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643].
# Waiting:10. Your selection_sort function should sort correctly any list of numbers.