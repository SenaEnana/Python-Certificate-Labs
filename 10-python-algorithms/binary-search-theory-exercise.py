# Questions

#1 What is the main difference between linear search and binary search?

# Linear search is faster than binary search.

# Binary search requires a sorted list, while linear search does not.

# Linear search can only be used with numbers.

# Binary search always returns the first occurrence of a target.

#2 What is the time complexity of linear search?

# O(1)

# O(log n)

# O(n)

# O(n²)

#3 In binary search, what happens if the target value is not found in the list?

# It returns the middle index.

# It returns -1.

# It returns the last index checked.

# It enters an infinite loop.

# /////////////////////////////////////////
# Two types of search algorithms
# Linear Search Algorithms

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# Binary Search Algorithms
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2  

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# We start by identifying a low and high index. This represents the range of the list we are searching through.

# We then check the condition of low being less than or equal to high. If low is greater than high, 
# we have searched through the entire list and the target value is not found. In that case we stop the search and return -1.

# If the low index is less than or equal to the high index, we calculate the middle index of the list, mid. 
# We then check if the target value is at the middle index. If it is, we return the middle index.

# Otherwise, we check if the value at the midpoint is less than the target. If it is, 
# we update the low index to be the middle index plus one. This means we will search the right half of the list.

# Lastly, if none of the other conditions are True, 
# we update the high index to be the middle index minus one. This means we will search the left half of the list.

# We continue to repeat this process until we find the target or determine that the target is not in the list.